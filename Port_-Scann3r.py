import socket
import threading
import time
import sys

# ───────────── Get Target ─────────────
while True:
    target = input("\nEnter Target IP or Domain: ")

    try:
        target_ip = socket.gethostbyname(target)
        print(f"✔ Target OK → {target_ip}")
        break

    except socket.gaierror:
        print("✘ Invalid domain! Try again...\n")

# ───────────── Animation ─────────────
banner = "\nStarting Port Scan..."
for char in banner:
    print(char, end="", flush=True)
    time.sleep(0.04)

print("\n" + "-"*50)

# ───────────── Port Scan Function ─────────────
def scan(port):
    s = socket.socket()
    s.settimeout(0.5)
    try:
        if s.connect_ex((target_ip, port)) == 0:
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "Unknown"

            print(f"[OPEN] Port {port:<4} | Service: {service}")
    finally:
        s.close()

# ───────────── Create Threads + Handle Ctrl+C ─────────────
try:
    for port in range(1, 1025):
        t = threading.Thread(target=scan, args=(port,))
        t.start()
        time.sleep(0.01)  # تخفيف السرعة قليلاً حتى يكون الكونسول منظم

except KeyboardInterrupt:
    print("\n\n⛔ Scan interrupted by user (Ctrl+C)!")
    print("Exiting cleanly...\n")
    sys.exit()
