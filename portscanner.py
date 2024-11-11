import usocket as socket
import time
import network

# Initialize Wi-Fi Interface
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Wi-Fi credentials
ssid = 'POCO F6 Pro'
password = 'bananana'

# Check if already connected
if not wlan.isconnected():
    print('Connecting to Wi-Fi...')
    wlan.connect(ssid, password)

    # Wait for connection
    while not wlan.isconnected():
        time.sleep(1)

print('Connected to Wi-Fi')
print(wlan.ifconfig())  # Print the network information

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(5)
        s.connect((ip, port))
        return True
    except OSError as e:
        return False
    finally:
        s.close()

def port_scanner(ip, start_port, end_port):
    print("Scanning IP:", ip)
    for port in range(start_port, end_port + 1):
        if scan_port(ip, port):
            print("Port", port, "is open")
        else:
            print("Port", port, "is closed")

# Example usage
ip_to_scan = '192.168.70.187'  # Replace with the IP you want to scan
start_port = 1
end_port = 100  # Scanning 100 ports, adjust as needed

# Start port scanning
print("Running port scanning...")
port_scanner(ip_to_scan, start_port, end_port)
