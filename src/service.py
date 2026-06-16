import ipaddress

import math


def  get_ip_address():
    while True:
        user_ip = input("IP address: ")

        try:
            return ipaddress.IPv4Address(user_ip)
        except ValueError:
            print("Wrong IP address!")

def get_subnet_mask():
    while True:
        user_mask = input("Subnet mask: ")

        try:
            ipaddress.IPv4Network(f"0.0.0.0/{user_mask}")

            return user_mask
        except ValueError:
            print("Wrong subnet mask!")

def create_network(ip_address, subnet_mask):
    network = ipaddress.IPv4Network((ip_address, subnet_mask), strict=False)
    return network



def print_info(network):
    print (f"Network address: {network}")
    print(f"Default gateway: {network.network_address + 1}")
    print(f"Broadcast address: {network.broadcast_address}")
    print(f"Number of useful hosts: {network.num_addresses - 3} ")
    print(f"First useful host: {network.network_address + 2}")
    print(f"Last useful host: {network.broadcast_address - 1}")

def divide_network(network, subnets):
    network = ipaddress.IPv4Network(network)
    if subnets < 1:
        raise ValueError("Number of subnets must be greater than 0!")

    if subnets & (subnets - 1) != 0:
        raise ValueError("Number of subnets must be power of 2!")

    prefix_diff = int(math.log2(subnets))
    max_diff = network.max_prefixlen - network.prefixlen

    if prefix_diff > max_diff:
        raise ValueError("Cannot create such number of subnets!")

    subnet_list = list(network.subnets(prefixlen_diff=prefix_diff))
    return subnet_list

def get_prefix(hosts):
    host_bits = math.ceil(math.log2(hosts + 2))
    return 32 - host_bits

def vlsm(network, hosts_list):
    network = ipaddress.IPv4Network(network)

    hosts_list = sorted(hosts_list, reverse=True)

    current_ip = network.network_address
    result = []

    for hosts in hosts_list:
        prefix = get_prefix(hosts)

        subnet = ipaddress.IPv4Network((current_ip, prefix), strict=False)

        if not subnet.subnet_of(network):
            raise ValueError("Not enough addresses for VLSM!")

        result.append((hosts, subnet)) #this is one obj, that's why it's in ()

        current_ip = subnet.broadcast_address + 1

    return result


