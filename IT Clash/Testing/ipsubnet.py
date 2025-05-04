import ipaddress

def calculate_subnet(ip_address, subnet_mask):
    """
    Calculates subnet information from an IP address and subnet mask.

    Args:
        ip_address (str): The IP address.
        subnet_mask (str): The subnet mask.

    Returns:
        dict: A dictionary containing subnet information.
    """
    try:
        network = ipaddress.ip_network(f"{ip_address}/{subnet_mask}", strict=False)
        return {
            "network_address": str(network.network_address),
            "netmask": str(network.netmask),
            "broadcast_address": str(network.broadcast_address),
            "host_addresses": [str(host) for host in network.hosts()],
            "number_of_hosts": network.num_addresses - 2 if network.prefixlen < 31 else network.num_addresses,
        }
    except ValueError as e:
        return {"error": str(e)}

if __name__ == "__main__":
    ip_address = input("Enter IP address: ")
    subnet_mask = input("Enter subnet mask (e.g., 24 or 255.255.255.0): ")

    subnet_info = calculate_subnet(ip_address, subnet_mask)

    if "error" in subnet_info:
        print(f"Error: {subnet_info['error']}")
    else:
        print("\nSubnet Information:")
        for key, value in subnet_info.items():
            print(f"{key}: {value}")