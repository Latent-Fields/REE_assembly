#!/usr/bin/env bash
# wg_enable_forwarding.sh -- let two WireGuard peers reach each other THROUGH
# a hub.
#
# WHY THIS IS NEEDED: in a star-shaped WireGuard net, peers may talk only to
# the hub. A mobile peer cannot reach a workstation peer until the hub forwards
# between those two peer addresses.
#
# This enables forwarding SCOPED to the single peer pair you name (not the whole
# subnet), so the hub's blast radius stays minimal -- it becomes a router only
# for <ipA> <-> <ipB>, both directions, on the wg0 interface.
#
# Run ON the hub, or pipe over SSH:
#   ssh <HUB_SSH_TARGET> 'sudo bash -s' < scripts/wg_enable_forwarding.sh -- <PHONE_WG_IP> <MAC_WG_IP>
#
# Reverse it later with:  sudo iptables -D FORWARD ... (rules printed below), or
# just delete the mobile peer -- with no peer at that address the rules are inert.
#
# Idempotent: -C checks before -A, sysctl drop-in is overwritten in place.
set -euo pipefail

IFACE="wg0"

[ "${1:-}" = "--" ] && shift
IPA="${1:-}"   # mobile peer IP
IPB="${2:-}"   # workstation peer IP

if [ -z "$IPA" ] || [ -z "$IPB" ]; then
    echo "usage: wg_enable_forwarding.sh <ipA> <ipB>" >&2
    exit 2
fi
for ip in "$IPA" "$IPB"; do
    if ! printf '%s' "$ip" | grep -Eq '^([0-9]{1,3}\.){3}[0-9]{1,3}$'; then
        echo "ERROR: '$ip' is not an IPv4 address." >&2
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
