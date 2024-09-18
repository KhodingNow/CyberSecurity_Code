import subprocess

def discover_active_hosts(network_prefix, start_range,end_range):
    active_hosts =[]

    for host in range(start_range, end_range + 1):
        ip_address = f'{network_prefix}.{host}'
        response = subprocess.run(['ping', '-c','1', ip_address], stdout=subprocess.DEVNULL)

        if response.returncode == 0:
            active_hosts.append(ip_address)

    return active_hosts
if __name__=='__main__':
    network_prefix = '192.168.1' # Change this to your network prefix
    start_range = 1
    end_range =255

    active_hosts =discover_active_hosts(network_prefix, start_range, end_range)

    if active_hosts:
        print("Active hosts:")
        for host in active_hosts:
            print(host)
    else:
        print('No active hosts found.')