---
nav_exclude: true
---

# Mobile access: public overview

This repository supports mobile access to the REE explorer and to a persistent
Claude Code terminal session through a private WireGuard network plus SSH/tmux.

This file is intentionally sanitized for GitHub. It does not contain real
endpoints, WireGuard addresses, public keys, SSH users, device labels, or host
names. Keep those values in the local-only runbook:

```text
docs/mobile_access.local.md
```

That file is ignored by git. Do not commit it.

## Model

- The explorer is reachable only after the phone joins the private WireGuard
  network.
- Claude Code access is through SSH to the workstation, then attaching to a
  persistent `tmux` session.
- WireGuard and SSH private keys must be generated and kept on the device that
  owns them.
- Only public keys should be copied between devices.
- The explorer has no application-layer authentication, so the WireGuard tunnel
  and local bind settings are the boundary.

## Public Setup Shape

Use the private local runbook to fill in these placeholders:

```text
<WG_SUBNET>
<HUB_PUBLIC_ENDPOINT>
<HUB_WG_PUBLIC_KEY>
<HUB_WG_IP>
<MAC_WG_IP>
<PHONE_WG_IP>
<LOCAL_SSH_USER>
<SSH_HOST_ALIAS>
<EXPLORER_URL>
```

The provisioning sequence is:

1. Generate the phone WireGuard keypair on the phone.
2. Add the phone as a WireGuard peer on the hub using only the phone public key.
3. Enable scoped forwarding between the phone peer and the workstation peer.
4. Confirm the workstation routes replies through the WireGuard network.
5. Open the explorer URL from the phone.
6. Generate a phone SSH key on the phone and install only its public key on the
   workstation.
7. SSH or mosh into the workstation and attach the persistent `tmux` session.

## Helper Scripts

The helper scripts are safe to keep public because they require the caller to
provide concrete values at runtime:

```bash
ssh <HUB_SSH_TARGET> 'sudo bash -s' < scripts/wg_add_peer.sh -- <PEER_NAME> '<PHONE_WG_PUBLIC_KEY>' <PHONE_WG_IP>
ssh <HUB_SSH_TARGET> 'sudo bash -s' < scripts/wg_enable_forwarding.sh -- <PHONE_WG_IP> <MAC_WG_IP>
bash scripts/claude_mobile.sh
```

## Hardening

Once mobile access is working, bind `serve.py` only to localhost plus the
workstation's WireGuard address:

```bash
python3 serve.py --bind <MAC_WG_IP> --bind 127.0.0.1
```

With no `--bind`, `serve.py` keeps its existing all-interface behavior.

## What Must Stay Out Of Git

Do not commit:

- real hub endpoint or cloud host addresses
- real WireGuard public keys when they identify this deployment
- real internal WireGuard address assignments
- real SSH usernames or mobile host aliases
- phone provisioning screenshots
- any private key, token, password, or bearer credential
