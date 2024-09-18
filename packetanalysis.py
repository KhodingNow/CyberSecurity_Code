from scapy.all import sniff,IP 

def packet_handler(packet):
    if IP in packet:
        ip_packet=packet[IP]
        print(f"Source IP: {ip_packet.src}, Destination IP: {ip_packet.dst}")

sniff(iface='eth0', filter='ip', prn=packet_handler,count=10)
