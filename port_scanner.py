from tqdm import tqdm
import socket
import argparse
from colorama import init, Fore, Style
from pyfiglet import Figlet


# Descripcion
description = f""" Ejemplos de uso:
            [+] Escaneo a los 51 puertos más usados:
                -t 127.0.0.1 -f
            [+] Especificar los puertos separados por (,) [80,8080]:
                -t 127.0.0.1 -p 21,23,443
            [+] Escanea un rango de puertos [default 1-65536]:
                -t 127.0.0.1 -ip 70 -ep 100
            [+] Escanea puertos por defecto [default 1-65536]:
                -t 127.0.0.1 """


parser = argparse.ArgumentParser(description='Escanner de puertos',
                                 epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-t", "--target", help="target", required=True)
parser.add_argument("-f", "--fast", help="Escanea los 51 puertos más usados.",
                    action="store_true", default=False)
parser.add_argument(
    "-p", "--ports", help="Especificar los puertos separados por (,) [80,8080].")
parser.add_argument("-ip", "--initial_port",
                    help="Especificar puerto de inicio, default [1].", default=1)
parser.add_argument("-ep", "--end_port",
                    help="Especificar puerto final, default [65536].", default=65536)
params = parser.parse_args()


openPorts = []
puertos_mas_usados = [
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


def show_open_ports():
    print("\n")
    for port in openPorts:
        print(f'\t{Fore.GREEN}http://{params.target}:{port}\t-->\tPuerto: {Fore.RED}{Style.BRIGHT}{port}{Style.RESET_ALL} {Fore.GREEN}abierto')


def scannerMostImportantsPorts():
    try:
        print(
            f'\t\nEscanendo IP: {Fore.MAGENTA}{Style.BRIGHT}{params.target}{Fore.RESET}{Style.RESET_ALL} con los puertos:\n {puertos_mas_usados}\n')

        for port in tqdm(puertos_mas_usados):
            # crendo el objeto socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # estableciendo el timeout
            s.settimeout(2)
            # comprobar conexion
            if s.connect_ex((params.target, port)) == 0:
                openPorts.append(port)
            # cerramos el socket
            s.close()
    except Exception as err:
        print(
            f"\t{Fore.RED}{Style.BRIGHT}[!]-Error {err=}\n\t[!]-{type(err)=}{Fore.RESET}{Style.RESET_ALL}")


def scanner():
    try:
        print(
            f'\t\nEscanendo IP: {Fore.MAGENTA}{Style.BRIGHT}{params.target}{Fore.RESET}{Style.RESET_ALL} del puerto {params.initial_port} al {params.end_port}\n')

        for port in tqdm(range(int(params.initial_port), int(params.end_port))):
            # crendo el objeto socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # estableciendo el timeout
            s.settimeout(2)
            # comprobar conexion
            if s.connect_ex((params.target, port)) == 0:
                openPorts.append(port)
            # cerramos el socket
            s.close()
    except Exception as err:
        print(
            f"\t{Fore.RED}{Style.BRIGHT}[!]-Error {err=}\n\t[!]-{type(err)=}{Fore.RESET}{Style.RESET_ALL}")


def selected_ports():
    try:
        print(
            f'\t\nEscanendo IP: {Fore.MAGENTA}{Style.BRIGHT}{params.target}{Fore.RESET}{Style.RESET_ALL} con los puertos {params.ports}\n')
        ports = params.ports.split(',')

        for port in tqdm(ports):
            # crendo el objeto socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # estableciendo el timeout
            s.settimeout(2)
            # comprobar conexion
            if s.connect_ex((params.target, int(port))) == 0:
                openPorts.append(port)
            # cerramos el socket
            s.close()
    except Exception as err:
        print(
            f"\t{Fore.RED}{Style.BRIGHT}[!]-Error {err=}\n\t[!]-{type(err)=}{Fore.RESET}{Style.RESET_ALL}")


def main():
    # colorama init
    init()

    # banner
    f = Figlet(font='slant')
    print(f.renderText('n1c3Scanner'))

    # name
    name = 'by_n1c3bug'
    print(f'{Fore.RED}{Style.BRIGHT}\n {name:_^40}\n\t{Fore.RESET}{Style.RESET_ALL}')

    # choose function
    if params.fast:
        scannerMostImportantsPorts()
    elif params.ports:
        selected_ports()
    else:
        scanner()
    # show open  ports
    show_open_ports()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(
            f'{Fore.RED}{Style.BRIGHT}[!]{Fore.RESET}{Style.RESET_ALL} {Fore.MAGENTA}{Style.BRIGHT}Saliendo...{Fore.RESET}{Style.RESET_ALL}')
        exit()
