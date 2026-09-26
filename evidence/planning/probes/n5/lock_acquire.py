"""Acquire the Mac probe lock (mkdir). Retries every 30 s AND immediately when the lock's
parent directory changes (kqueue), so a waiter gets the next hold instead of being starved by
a holder that re-acquires back-to-back. Requires >= 800 MB free+inactive memory. Writes the
owner file only after its own mkdir succeeded. Exit 0 once held."""
import os, select, subprocess, sys, time
L = "/Users/dgolden/REE_Working/.scratch/breakthrough-20260924/mac_probe.lock"
label = sys.argv[1]
def freemb():
    out = subprocess.run(["vm_stat"], capture_output=True, text=True).stdout
    ps = int(out.split("page size of")[1].split()[0]); f = i = 0
    for ln in out.splitlines():
        if ln.startswith("Pages free"): f = int(ln.split()[-1].rstrip("."))
        if ln.startswith("Pages inactive"): i = int(ln.split()[-1].rstrip("."))
    return (f + i) * ps // 1048576
fd = os.open(os.path.dirname(L), os.O_RDONLY)
kq = select.kqueue()
ev = select.kevent(fd, filter=select.KQ_FILTER_VNODE, flags=select.KQ_EV_ADD | select.KQ_EV_CLEAR,
                   fflags=select.KQ_NOTE_WRITE | select.KQ_NOTE_LINK)
kq.control([ev], 0, 0)
while True:
    if freemb() >= 800:
        try:
            os.mkdir(L)
            break
        except FileExistsError:
            pass
    kq.control(None, 1, 30.0)
with open(os.path.join(L, "owner"), "w") as fh:
    fh.write("%s bt0926-n5 %s pid %d\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), label, os.getppid()))
print("LOCK ACQUIRED %s %s freeMB %d" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), label, freemb()), flush=True)
