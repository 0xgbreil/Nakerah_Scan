import socket
import logo
import sys
import scan_animator

# List of common ports to scan if only IP is provided
common_ports = [
    80, 443, 22, 21, 25, 53, 110, 135, 139, 143, 445, 3306, 3389
]

def print_usage():
    """
    Display usage instructions for the script.
    """
    print("""
\033[1;36mUsage:\033[0m
\033[1;33m    python3 nakerah_scan.py <IP> <start_port> <end_port>\033[0m   ===>> Scan a range of ports
\033[1;33m    python3 nakerah_scan.py <IP> <port>\033[0m                  ===>> Scan a single port
\033[1;33m    python3 nakerah_scan.py <IP> <port1> <port2> ...\033[0m      ===>>  Scan multiple specific ports
\033[1;33m    python3 nakerah_scan.py<IP> \033[0m                        ===>> Scan common ports
\033[1;33m    python3 nakerah_scan.py <port>\033[0m                      ===>> Show usage if port only
""")

def get_service_info(port):
    """
    Get the service name running on the open port.
    """
    try:
        return socket.getservbyport(port)
    except OSError:
        return "Unknown"

def scan_ports(ip, ports_to_scan):
    """
    Scan specified ports on the given IP address or domain.
    """
    open_ports = []

    # Try resolving the domain to IP
    try:
        ip = socket.gethostbyname(ip)
        print("")
        print("")
        print("")
        print("======================")
        print(f"\033[1;34mResolved {ip}...\033[0m")
    except socket.gaierror:
        print(f"\033[1;31mError: Unable to resolve domain {ip}\033[0m")
        sys.exit(1)
    except KeyboardInterrupt:
        pass
    print("")
    print("=========================")
    print("")
    # text anmation 
    target = sys.argv[1]
    text = f"\033[1;34mstart scanning on \033[1;31m{target}\033[0m\033[0m"
    scan_animator.animated_print(text)
    print("\n")

    try:
        for port in ports_to_scan:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Keep timeout 1 second
            try:
                sock.connect((ip, port))
                service = get_service_info(port)
                open_ports.append(port)
                print(f"\033[1;32mPort {port}: [OPEN] Service: {service}\033[0m")
            except (socket.timeout, ConnectionRefusedError):
                # Handle closed or filtered ports
                print(f"\033[1;31mPort {port}: [CLOSED or FILTERED]\033[0m")
            finally:
                sock.close()

    except KeyboardInterrupt:
        print("\n\033[1;31mScan interrupted by user.\033[0m")
        sys.exit(0)  # Exit the script gracefully
       # After the scanning loop, display the summary of open ports
    if open_ports:
        print("\n\033[1;37m----------------------------------------\033[0m")
        print("\033[1;32mOpen Ports Summary:\033[0m")
        print("")
        for open_port in open_ports:
            print(f"\033[1;32mPort {open_port}: [OPEN]\033[0m")
        print("\033[1;37m----------------------------------------\033[0m")
    else:
        print("\n\033[1;31mNo open ports found.\033[0m")

# Display the banner using the logo module
logo.banner()

# Example usage
if len(sys.argv) == 2:
    if sys.argv[1].isdigit():
        print_usage()  # Show usage if a port number is passed instead of an IP
    else:
        scan_ports(sys.argv[1], common_ports)  # Scan common ports
elif len(sys.argv) == 3:
    scan_ports(sys.argv[1], [int(sys.argv[2])])  # Scan a single port
elif len(sys.argv) == 4:
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    
    if start_port > end_port:
        # If start port is greater than end port, scan both ports
        print(f"\033[1;33mScanning ports {start_port} and {end_port} only.\033[0m")
        scan_ports(sys.argv[1], [start_port, end_port])
    else:
        # Scan the range of ports from start to end
        scan_ports(sys.argv[1], range(start_port, end_port + 1))
elif len(sys.argv) > 4:
    # Scan multiple specific ports
    ports = [int(port) for port in sys.argv[2:]]
    scan_ports(sys.argv[1], ports)
else:
    print_usage()

