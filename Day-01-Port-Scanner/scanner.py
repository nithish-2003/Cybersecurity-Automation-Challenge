import socket

target = input("Enter Target IP/Domain: ")
start_port = int(input("Enter Start Port: "))
end_port = int(input("Enter End Port: "))

print(f"\nScanning Target: {target}")
print("-" * 40)

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[+] Port {port} is OPEN")

    s.close()

print("\nScan Completed.")
