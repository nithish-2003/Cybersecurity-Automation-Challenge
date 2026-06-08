import socket
target = input("Enter Target IP/Domain: ")
start_port = int(input("Enter Start Port: "))
end_port = int(input("Enter End Port: "))
# Common services
services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}
# Store open ports for saving later
results = []
print(f"\nScanning Target: {target}")
print("-" * 40)
for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        service = services.get(port, "Unknown Service")
        print(f"[+] Port {port} is OPEN ({service})")
        results.append(f"Port {port} OPEN ({service})")
        # Try banner grabbing
        try:
            banner = s.recv(1024).decode().strip()
            if banner:
                print(f"    Banner: {banner}")
                results.append(f"Banner: {banner}")
        except:
            pass
    s.close()
# Save results to a file
with open("scan_results.txt", "w") as file:
    file.write(f"Scan Results for {target}\n")
    file.write("-" * 40 + "\n")
    for item in results:
        file.write(item + "\n")
print("\nScan Completed.")
print("Results saved in scan_results.txt")
