import scapy.all as scapy

def dns_packet_handler(packet):
    if packet.haslayer(scapy.DNSRR):
        dns_layer=packet[scapy.DNSRR]
        dns_query = dns_layer.qname.decode('utf-8')
        dns_response = dns_layer.rdata.decode('utf-8')

        print(f'DBS Query: {dns_query} --> DNS Response: {dns_response}')

def sniff_dns_traffic(interface):
    scapy.sniff(iface=interface, filter='port 53',prn=dns_packet_handler)

if __name__=='__main__':
    network_interface ='eth0' # Change to your network interface
    print(f'Sniffing DNS traffic on {network_interface}...\n')
    