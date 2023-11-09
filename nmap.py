import socket
from time import sleep

def open_ports(ip):

    try:
        ip = socket.gethostbyname(ip)
        for port in range(1,25):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            x = sock.connect_ex((ip, port))
            if x == 0:
                print(f"[+] Port Open: {port}")
            else:
                print(f"[-] Port Closed: {port}")
                sock.close()
    except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    ip = input("Enter IP Address to scan: ")
    open_ports(ip)
