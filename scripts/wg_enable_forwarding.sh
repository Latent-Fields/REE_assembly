#!/usr/bin/env bash
# wg_enable_forwarding.sh -- let two WireGuard peers reach each other THROUGH
# the hub (ree-cloud-1).
#
# WHY THIS IS NEEDED: the REE WG net is a pure star -- every peer talks only to
# the hub (10.8.0.1), and the hub has IPv4 forwarding OFF (net.ipv4.ip_forward=0
# as of 2026-06-23). So an iPhone peer cannot reach the Mac's explorer at
# 10.8.0.11 until the hub is told to forward between them.
#
# This enables forwarding SCOPED to the single peer pair you name (not the whole
# subnet), so the hub's blast radius stays minimal -- it becomes a router only
# for <ipA> <-> <ipB>, both directions, on the wg0 interface.
#
# Run ON the hub, or pipe over SSH:
#   ssh ree@91.98.130.117 'sudo bash -s' < scripts/wg_enable_forwarding.sh -- 10.8.0.20 10.8.0.11
#
# Reverse it later with:  sudo iptables -D FORWARD ... (rules printed below), or
# just delete the iPhone peer -- with no peer at 10.8.0.20 the rules are inert.
#
# Idempotent: -C checks before -A, sysctl drop-in is overwritten in place.
set -euo pipefail

IFACE="wg0"

[ "${1:-}" = "--" ] && shift
IPA="${1:-}"   # e.g. 10.8.0.20 (iPhone)
IPB="${2:-}"   # e.g. 10.8.0.11 (Mac)

if [ -z "$IPA" ] || [ -z "$IPB" ]; then
    echo "usage: wg_enable_forwarding.sh <ipA> <ipB>   (e.g. 10.8.0.20 10.8.0.11)" >&2
    exit 2
fi
for ip in "$IPA" "$IPB"; do
    if ! printf '%s' "$ip" | grep -Eq '^10\.8\.0\.[0-9]{1,3}$'; then
        echo "ERROR: '$ip' is not a 10.8.0.x address." >&2
        exit 2
    fi
done

SUDO=""
[ "$(id -u)" -ne 0 ] && SUDO="sudo"

# 1) Enable IPv4 forwarding live + persist.
echo "[wg_fwd] enabling net.ipv4.ip_forward (live + persistent)"
$SUDO sysctl -w net.ipv4.ip_forward=1 >/dev/null
echo 'net.ipv4.ip_forward=1' | $SUDO tee /etc/sysctl.d/99-ree-wg-forward.conf >/dev/null

# 2) Scoped FORWARD ACCEPT rules, both directions, only on the wg interface.
add_rule() {
    # $@ = the match spec after -A/-C FORWARD
    if $SUDO iptables -C FORWARD "$@" 2>/dev/null; then
        echo "[wg_fwd] rule already present: $*"
    else
        $SUDO iptables -A FORWARD "$@"
        echo "[wg_fwd] added rule: $*"
    fi
}
add_rule -i "$IFACE" -o "$IFACE" -s "${IPA}/32" -d "${IPB}/32" -j ACCEPT
add_rule -i "$IFACE" -o "$IFACE" -s "${IPB}/32" -d "${IPA}/32" -j ACCEPT

# 3) Persist iptables across reboot if the tooling is available.
if command -v netfilter-persistent >/dev/null 2>&1; then
    $SUDO netfilter-persistent save >/dev/null && echo "[wg_fwd] iptables persisted via netfilter-persistent"
elif command -v iptables-save >/dev/null 2>&1 && [ -d /etc/iptables ]; then
    $SUDO sh -c "iptables-save > /etc/iptables/rules.v4" && echo "[wg_fwd] iptables persisted to /etc/iptables/rules.v4"
else
    echo "[wg_fwd] WARNING: no netfilter-persistent / /etc/iptables -- rules are LIVE but"
    echo "         will NOT survive a reboot. Install iptables-persistent or add the two"
    echo "         FORWARD rules to a wg0.conf PostUp to make them durable."
fi

echo "[wg_fwd] done. ip_forward=$($SUDO sysctl -n net.ipv4.ip_forward)"
echo "[wg_fwd] FORWARD rules touching $IFACE:"
$SUDO iptables -S FORWARD | grep -- "-i $IFACE" || true
