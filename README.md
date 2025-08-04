# REDOS
# Simple TCP Flood Script

This is a Python-based TCP flood tool designed to send multiple TCP packets to a target IP and port concurrently using threading. It attempts to check if the target is online before starting the attack and visually displays status messages using colored terminal output.

---

## Features

- Checks if the target IP is online by pinging it before starting.
- Creates 100 threads to continuously send TCP packets to the target.
- Uses socket programming to connect and send basic HTTP GET requests.
- Colored console output for status updates using `colorama`.
- Gracefully handles `KeyboardInterrupt` to stop the script.

---

## Requirements

- Python 3.x
- `colorama` module (for colored terminal output)

You can install `colorama` via pip:

```bash
pip install colorama

Usage

    Run the script:

python tcp_flood.py

    When prompted, enter the target IP address.

    Enter an open port number on the target.

    The script will check if the target is online.

    If the target is up, it will start 100 threads to send TCP packets continuously.

    To stop the script, press Ctrl+C.

Disclaimer

This script is intended for educational and testing purposes only. Do NOT use it to attack any network or system without explicit permission from the owner. Unauthorized use may be illegal and unethical.
How It Works

    The script pings the target IP to verify it's reachable.

    If online, it launches multiple threads.

    Each thread repeatedly opens a TCP connection to the target and sends a simple HTTP GET request.

    The script prints success or failure messages for each packet sent.

Example Output

Enter Target IP: 192.168.1.10

Enter open port: 80

[+] Target is up

[*] Starting flood thread...

[+] Packet sent!

[-] Failed to send packet
