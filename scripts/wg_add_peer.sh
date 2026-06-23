#!/usr/bin/env bash
# wg_add_peer.sh -- add a WireGuard peer to the REE hub (ree-cloud-1 / 10.8.0.1).
#
# PUBLIC-KEY-ONLY. This script never generates, reads, or transmits a private
# key. The peer's keypair is generated on the peer device (e.g. the WireGuard
# iOS app); you pass only its PUBLIC key here. The hub's own private key is
# untouched.
#
# Run ON the hub, or pipe it in over SSH from the Mac:
#   ssh ree@91.98.130.117 'sudo bash -s' < scripts/wg_add_peer.sh -- <name> <pubkey> <ip>
#
# Args:
#   <name>    short label written as a comment above the [Peer] block (e.g. iphone)
#   <pubkey>  the peer's WireGuard PUBLIC key (44-char base64, ends with '=')
#   <ip>      the peer's address inside the WG net, no mask (e.g. 10.8.0.20)
#
# Idempotent: refuses to add a pubkey or IP that is already present, and prints
# the current allowed-ips table so you can confirm.
set -euo pipefail

IFACE="wg0"
CONF="/etc/wireguard/${IFACE}.conf"

# Allow a leading '--' so `bash -s -- a b c` works cleanly over SSH.
[ "${1:-}" = "--" ] && shift

NAME="${1:-}"
PUBKEY="${2:-}"
IP="${3:-}"

if [ -z "$NAME" ] || [ -z "$PUBKEY" ] || [ -z "$IP" ]; then
    echo "usage: wg_add_peer.sh <name> <pubkey> <ip>" >&2
    echo "  e.g. wg_add_peer.sh iphone 'AbC...=' 10.8.0.20" >&2
    exit 2
fi

# Validate the public key shape (WireGuard keys are 32 bytes -> 44 base64 chars).
if ! printf '%s' "$PUBKEY" | grep -Eq '^[A-Za-z0-9+/]{43}=$'; then
    echo "ERROR: '$PUBKEY' does not look like a WireGuard public key (expected 44-char base64 ending in '=')." >&2
    exit 2
fi

# Validate the IP shape.
if ! printf '%s' "$IP" | grep -Eq '^10\.8\.0\.[0-9]{1,3}$'; then
    echo "ERROR: '$IP' is not a 10.8.0.x address." >&2
    exit 2
fi

SUDO=""
[ "$(id -u)" -ne 0 ] && SUDO="sudo"

echo "[wg_add_peer] hub interface: $IFACE   config: $CONF"

# Refuse duplicates -- pubkey already a peer?
if $SUDO wg show "$IFACE" peers 2>/dev/null | grep -Fxq "$PUBKEY"; then
    echo "[wg_add_peer] peer pubkey already present -- nothing to do."
    $SUDO wg show "$IFACE" allowed-ips
    exit 0
fi

# Refuse duplicates -- IP already allocated?
if $SUDO wg show "$IFACE" allowed-ips 2>/dev/null | awk '{print $2}' | grep -Fxq "${IP}/32"; then
    echo "ERROR: ${IP}/32 is already allocated to another peer:" >&2
    $SUDO wg show "$IFACE" allowed-ips | grep -F "${IP}/32" >&2
    exit 1
fi

# 1) Apply live (survives until next interface restart).
echo "[wg_add_peer] wg set $IFACE peer <pubkey> allowed-ips ${IP}/32"
$SUDO wg set "$IFACE" peer "$PUBKEY" allowed-ips "${IP}/32"

# 2) Persist to the config (survives reboot / wg-quick restart).
echo "[wg_add_peer] appending [Peer] block to $CONF"
$SUDO tee -a "$CONF" >/dev/null <<EOF

# ${NAME} (added $(date -u +%Y-%m-%dT%H:%M:%SZ))
[Peer]
PublicKey = ${PUBKEY}
AllowedIPs = ${IP}/32
EOF

echo "[wg_add_peer] done. Current peers/allowed-ips:"
$SUDO wg show "$IFACE" allowed-ips
echo "[wg_add_peer] NOTE: to let this peer reach another peer (e.g. the Mac at"
echo "             10.8.0.11), run scripts/wg_enable_forwarding.sh on the hub."
