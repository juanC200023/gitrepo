#!/usr/bin/env python3

import scapy.all as scapy


def process_dns_packet(packet):
    if packet.haslayer(scapy.DNSQR):
        print(packet.show())


def main():
    interface = "ens33"
    print(f"\n[+] Interceptando paquetes de la maquina victima:\n")
    scapy.sniff(iface=interface, filter="udp and port 53", prn=process_dns_packet, store=0)

if __name__ == '__main__':
    main()
