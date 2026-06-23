# Mobile access: REE explorer + Claude Code from the iPhone over WireGuard

Reach two things from the phone, over the WireGuard network you already run:

1. **The REE claims explorer** — `http://10.8.0.11:8000/explorer` in Safari.
2. **This Claude Code instance** — SSH into the Mac and attach a persistent
   `tmux` session.

Both ride the existing `10.8.0.0/24` WireGuard net. Nothing is exposed to the
public internet.

---

## The secret-isolation model (read this first)

**Every private key is generated on the device that keeps it, and only public
keys ever cross.** That is how WireGuard and SSH are designed to work, and it
means the server side can be provisioned without anyone (including an assistant)
ever seeing a secret.

| Secret | Generated on | Lives only on | What the hub/Mac sees |
|--------|--------------|---------------|-----------------------|
| iPhone WireGuard private key | iPhone WireGuard app | iPhone | its **public** key |
| iPhone SSH private key | iPhone SSH app | iPhone | its **public** key |
| Hub WireGuard private key | hub (pre-existing) | hub | — (untouched) |
| Mac SSH keys | Mac (pre-existing) | Mac | — (untouched) |

Give each key a memorable **label** in its app (tunnel `REE-net`, SSH key
`REE-mac`) so you refer to them by name. The only things you ever read back out
to anyone are **public** keys and IP/host assignments.

---

## Network facts (verified 2026-06-23)

| Thing | Value |
|-------|-------|
| WireGuard subnet | `10.8.0.0/24` |
| Hub (`ree-cloud-1`) WG IP | `10.8.0.1` |
| Hub public endpoint | `91.98.130.117:51820` |
| Hub WireGuard **public** key | `qp3fuadZ8ZmyPp9RQK7Aayy3adMC6bMBpR79H54K/Ak=` |
| Mac (`DLAPTOP-4`) WG IP | `10.8.0.11` |
| Cloud workers | `10.8.0.12`, `.13`, `.14` |
| **Free IP for the iPhone** | **`10.8.0.20`** |
| Explorer | `serve.py` on `:8000` (binds `0.0.0.0`, no auth — WireGuard is the boundary) |

> **Why a hub change is needed.** The WG net is a pure *star*: every peer talks
> only to the hub, and the hub currently has IPv4 forwarding **off**
> (`net.ipv4.ip_forward=0`). So an iPhone peer cannot reach the Mac until the hub
> is told to forward between them. `scripts/wg_enable_forwarding.sh` turns this on
> **scoped to just the iPhone↔Mac pair** (not the whole subnet), so the hub's
> role as a router stays minimal.

---

## Part 1 — Put the iPhone on the WireGuard network (explorer access)

### 1a. On the iPhone (you keep the secret)

WireGuard app → **Add a tunnel → Create from scratch**. The app generates the
keypair on-device. Fill in:

- **Name:** `REE-net`
- **Interface → Addresses:** `10.8.0.20/32`
- (leave Private key as generated; leave DNS empty)
- **Add peer:**
  - **Public key:** `qp3fuadZ8ZmyPp9RQK7Aayy3adMC6bMBpR79H54K/Ak=`
  - **Endpoint:** `91.98.130.117:51820`
  - **Allowed IPs:** `10.8.0.0/24`
  - **Persistent keepalive:** `25`

Save. At the top of the tunnel screen the app shows the **Public key** for this
tunnel — that is the only thing you read back to provision the hub.

### 1b. On the hub (public-key-only)

Add the peer using its public key (`<IPHONE_PUBKEY>` is what you read off the
app), then enable the scoped forwarding. Pipe the repo scripts over SSH so the
hub's git checkout is never touched:

```bash
# from the Mac, in REE_assembly/
ssh ree@91.98.130.117 'sudo bash -s' < scripts/wg_add_peer.sh -- iphone '<IPHONE_PUBKEY>' 10.8.0.20
ssh ree@91.98.130.117 'sudo bash -s' < scripts/wg_enable_forwarding.sh -- 10.8.0.20 10.8.0.11
```

Both scripts are idempotent and print the resulting state. `wg_add_peer.sh`
refuses a duplicate key/IP; `wg_enable_forwarding.sh` only opens the single
peer pair.

### 1c. On the Mac (one check, needs sudo)

The Mac must route replies back to the iPhone. Confirm its peer (the hub) covers
the whole subnet:

```bash
sudo wg show wg0 allowed-ips
```

The hub-peer line should include `10.8.0.0/24` (not just `10.8.0.1/32`). If it is
narrower, widen it in `/etc/wireguard/wg0.conf` (`AllowedIPs = 10.8.0.0/24` on the
hub `[Peer]`) and `sudo wg-quick down wg0 && sudo wg-quick up wg0`.

### 1d. Test

Turn the `REE-net` tunnel **on** in the iPhone WireGuard app, then in Safari:

- `http://10.8.0.11:8000/explorer` — the explorer should render.
- Tap into a live tab (e.g. **Machines**) to confirm the `/api/*` calls return data.

From the Mac, `sudo wg show wg0` should list the iPhone peer with a recent
handshake.

> The explorer is a dense desktop dashboard; it works on mobile Safari but is
> cramped. Pinch-zoom is expected. A responsive layout is out of scope here.

---

## Part 2 — Claude Code from the iPhone (SSH + tmux)

### 2a. Pick a terminal app

- **Blink Shell (recommended).** Supports **mosh**, which — combined with `tmux`
  — survives the phone sleeping or switching networks (the #1 mobile-SSH
  annoyance). Generates SSH keys on-device.
- **Termius (friendly free option).** On-device key generation, saved host
  aliases, simple UI. Plain SSH (no mosh) is fine over a stable WireGuard tunnel.

### 2b. On the Mac (one-time setup)

```bash
brew install tmux        # required by claude_mobile.sh
brew install mosh        # only if you use Blink + mosh
sudo systemsetup -setremotelogin on    # enable Remote Login (SSH); or System
                                        # Settings > General > Sharing > Remote Login
```

Recommend key-only SSH (no passwords) once your key is installed.

### 2c. On the iPhone (you keep the secret)

In the terminal app: generate an SSH key named `REE-mac`, and add a host:

- **Alias:** `mac`  **Host:** `10.8.0.11`  **User:** `dgolden`  **Key:** `REE-mac`

Read the **public** key back out (e.g. Blink: `config` → keys → copy public key;
Termius: key → export public key).

### 2d. On the Mac (public-key-only)

Append the iPhone's SSH **public** key to authorized_keys:

```bash
mkdir -p ~/.ssh && chmod 700 ~/.ssh
printf '%s\n' '<IPHONE_SSH_PUBLIC_KEY>' >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

### 2e. Use it

With the `REE-net` tunnel on, from the iPhone terminal:

```bash
mosh mac        # or:  ssh mac
bash /Users/dgolden/REE_Working/REE_assembly/scripts/claude_mobile.sh
# you are now attached to the persistent tmux session "ree"; run:
claude
```

`claude_mobile.sh` keeps a detached `tmux` session named `ree` alive in
`REE_Working`. Lock the phone, lose signal, come back later, re-run the same
command (or `tmux attach -t ree`) and you are back in the **same** Claude Code
session. Detach without killing it with **Ctrl-b** then **d**.

---

## Part 3 — Optional hardening (recommended)

`serve.py` binds `0.0.0.0` (all interfaces) by default — which also exposes the
explorer on your home Wi-Fi LAN. Once the iPhone peer works, restrict it to
**WireGuard + localhost** with the new `--bind` flag:

```bash
# via the launcher (space-separated -> one --bind each):
REE_BIND="10.8.0.11 127.0.0.1" "/Users/dgolden/REE_Working/REE_assembly/Start Explorer.command"

# or directly:
python3 serve.py --bind 10.8.0.11 --bind 127.0.0.1
```

With no `--bind`, behaviour is unchanged (`0.0.0.0`). Restart `serve.py` after
changing this.

---

## Troubleshooting

| Symptom | Likely cause / fix |
|---------|--------------------|
| iPhone tunnel shows no handshake | Wrong hub public key or endpoint; check `91.98.130.117:51820` and the key above. `PersistentKeepalive 25` helps through NAT. |
| Tunnel up, but explorer won't load | Hub forwarding not enabled — re-run `wg_enable_forwarding.sh 10.8.0.20 10.8.0.11`; confirm `ssh ree@91.98.130.117 sudo sysctl -n net.ipv4.ip_forward` is `1`. |
| Explorer loads but API tabs are empty | Mac peer `AllowedIPs` too narrow (Part 1c) — reply traffic to `10.8.0.20` isn't entering the Mac's tunnel. Widen to `10.8.0.0/24`. |
| `ssh mac` refused | Remote Login off (`sudo systemsetup -setremotelogin on`) or `~/.ssh/authorized_keys` perms wrong (dir `700`, file `600`). |
| `claude_mobile.sh: tmux not installed` | `brew install tmux` on the Mac. |
| mosh won't connect | `brew install mosh` on the Mac; mosh's UDP runs inside the WG tunnel, so no extra firewall holes are needed. Fall back to `ssh mac`. |

## Reverting

- Remove the iPhone from the net: delete its `[Peer]` block in the hub's
  `/etc/wireguard/wg0.conf` and `sudo wg set wg0 peer '<IPHONE_PUBKEY>' remove`.
  With no peer at `10.8.0.20`, the scoped forwarding rules are inert.
- Disable forwarding entirely: `sudo sysctl -w net.ipv4.ip_forward=0` and remove
  `/etc/sysctl.d/99-ree-wg-forward.conf` + the two `FORWARD` rules.
- Revert the explorer to all-interfaces: just start `serve.py` with no `--bind`.
