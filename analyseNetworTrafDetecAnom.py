from scapy.all import sniff, IP
import time

# variables for tracking packets and time

packet_count = 0
start_time = time.time()

# define a packet processing function
def packet_handler(pkt):
    global packet_count

    if IP in pkt:
        packet_count += 1

# sniff network traffic for a specified time (say, 30 seconds)

sniff (filter='ip', prn=packet_handler, timeout=30)

# calculate packets per second

end_time = time.time - start_time
time_elapsed = end_time - start_time
packets_per_second = packet_count / time_elapsed

# Set a threshold for anomally detection 

threshold = 60 

# analyse and detect anomalies
if packets_per_second > threshold:
    print(f"Anomaly detected! Packets per second: {packets_per_second}")
else:
    print(f"No anomalies detected. Packets per second: {packets_per_second}")
