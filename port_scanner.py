import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from colorama import Fore, Style
from pyfiglet import Figlet


# Descripción
description = """Ejemplos de uso:
    [+] Escaneo a los 51 puertos más usados:
        python port_scanner.py -t 127.0.0.1 -f
    [+] Escanea los puertos separados por (,) [80,8080]:
        python port_scanner.py -t 127.0.0.1 -p 21,23,443
    [+] Escanea un rango de puertos:
        python port_scanner.py -t 127.0.0.1 -ip 70 -ep 100
    [+] Escanea todos los puertos [default 1-65536]:
        python port_scanner.py -t 127.0.0.1"""

# Inicialización de argumentos de línea de comandos
parser = argparse.ArgumentParser(description='Escáner de puertos',
                                 epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-t", "--target", help="IP objetivo", required=True)
parser.add_argument("-f", "--fast", help="Escanea los 51 puertos más usados.",
                    action="store_true", default=False)
parser.add_argument("-p", "--ports", help="Especificar los puertos separados por (,) [80,8080].")
parser.add_argument("-ip", "--initial_port",
                    help="Especificar puerto inicial, por defecto [1].", default=1)
parser.add_argument("-ep", "--end_port",
                    help="Especificar puerto final, por defecto [65536].", default=65536)
params = parser.parse_args()


open_ports = []
common_ports = [
    80,     # HTTP
    443,    # HTTPS
    22,     # SSH
    21,     # FTP
    25,     # SMTP
    110,    # POP3
    143,    # IMAP
    53,     # DNS
    3306,   # MySQL
    3389,   # RDP
    8080,   # HTTP alternativo
    23,     # Telnet
    587,    # SMTP alternativo
    995,    # POP3 SSL/TLS
    993,    # IMAP SSL/TLS
    1723,   # PPTP
    1194,   # OpenVPN
    111,    # RPCbind
    123,    # NTP
    137,    # NetBIOS
    138,    # NetBIOS
    139,    # NetBIOS
    161,    # SNMP
    162,    # SNMP trap
    389,    # LDAP
    445,    # SMB
    512,    # Rexec
    513,    # Rlogin
    514,    # Syslog
    1433,   # MS SQL Server
    1521,   # Oracle database
    3307,   # MySQL alternativo
    5432,   # PostgreSQL
    5900,   # VNC
    6000,   # X11
    8000,   # HTTP alternativo
    8888,   # HTTP alternativo
    1812,   # RADIUS
    1813,   # RADIUS
    2049,   # NFS
    27017,  # MongoDB
    33060,  # MySQL alternativo
    33848,  # Oracle database
    47808,  # BACnet
    49152,  # UPnP
    49153,  # Windows Remote Management (WinRM)
    50000,  # SAP
    54321,  # BACnet
    55000,  # VNC alternativo
    55001,  # VNC alternativo
    55002,  # VNC alternativo
]
def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((params.target, port))
    sock.close()
    return port if result == 0 else None


def show_open_ports(open_ports):
    if open_ports:
        print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Puertos abiertos:{Style.RESET_ALL}")
        for port in open_ports:
            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Puerto {Fore.RED}{port}{Style.RESET_ALL} abierto")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.RED}No se encontraron puertos abiertos.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")


def main():
    ip_address = params.target
    initial_port = int(params.initial_port)
    end_port = int(params.end_port)
    ports_to_scan = []

    if params.fast:
        ports_to_scan = common_ports
    elif params.ports:
        ports_to_scan = list(map(int, params.ports.split(",")))
    else:
        ports_to_scan = list(range(initial_port, end_port + 1))

    print(f"{Fore.CYAN}\nEscaneando puertos en la dirección IP: {ip_address}{Style.RESET_ALL}\n")

    with ThreadPoolExecutor() as executor:
        results = list(tqdm(executor.map(scan_port, ports_to_scan), total=len(ports_to_scan), ncols=80))

    open_ports = [port for port in results if port is not None]
    show_open_ports(open_ports)


if __name__ == '__main__':
    try:
        f = Figlet(font='slant')
        print(f.renderText('n1c3Scanner'))
        print(f'{Fore.RED}{"_"*25}by_n1c3bug{"_"*25}{Style.RESET_ALL}')
        main()
    except KeyboardInterrupt:
        print(f"{Fore.RED}[!] Saliendo...{Style.RESET_ALL}" )
        exit()
