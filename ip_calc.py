# Main Program for user data gathering, retrieves input from the user.
class OutofBoundsValueError(Exception):
    pass


class Data_Collector:
    def calculate_broadcast_address(self, ip_octets, cidr):
        ip_int = (ip_octets[0] << 24) | (ip_octets[1] << 16) | (ip_octets[2] << 8) | ip_octets[3]
        mask = (0xFFFFFFFF << (32 - cidr)) & 0xFFFFFFFF
        broadcast_int = ip_int | (~mask & 0xFFFFFFFF)
        return [(broadcast_int >> 24) & 0xFF, (broadcast_int >> 16) & 0xFF, (broadcast_int >> 8) & 0xFF, broadcast_int & 0xFF]

    def user_input(self):

        host_ip = input("\nPlease enter a valid ip address: ")

        host_ip_octet_1 = int(host_ip.split(".")[0])
        if host_ip_octet_1 < 0 or host_ip_octet_1 > 255:
            raise OutofBoundsValueError("Error: Please enter an integer value between 0 and 255")

        host_ip_octet_2 = int(host_ip.split(".")[1])
        if host_ip_octet_2 < 0 or host_ip_octet_2 > 255:
            raise OutofBoundsValueError("Error: Please enter an integer value between 0 and 255")

        host_ip_octet_3 = int(host_ip.split(".")[2])
        if host_ip_octet_3 < 0 or host_ip_octet_3 > 255:
            raise OutofBoundsValueError("Error: Please enter an integer value between 0 and 255")

        host_ip_octet_4 = int(host_ip.split(".")[3])
        if host_ip_octet_4 < 0 or host_ip_octet_4 > 255:
            raise OutofBoundsValueError("Error: Please enter an integer value between 0 and 255")

        cidr = int(input("Please choose your CIDR: "))
        if cidr < 1 or cidr > 32:
            raise OutofBoundsValueError("Error: Please enter an integer value between 0 - 31.")

        host_ip = [host_ip_octet_1, host_ip_octet_2, host_ip_octet_3, host_ip_octet_4, cidr]

        return host_ip

    def cidr_to_netmask(self, cidr=24):

        try:

            netmask = (0xFFFFFFFFF << (32 - cidr)) & 0xFFFFFFFFF
            # Extract each octet
            octet_1 = (netmask >> 24) & 0xFF
            octet_2 = (netmask >> 16) & 0xFF
            octet_3 = (netmask >> 8) & 0xFF
            octet_4 = netmask & 0xFF

            return [octet_1, octet_2, octet_3, octet_4]

        except OutofBoundsValueError as e:
            print(f"Error: {e}")
            return None

    # Determine IP class based on CIDR notation
    def netmask_to_class(self, cidr):

        try:
            if 1 <= cidr <= 8:
                return "A"
            elif 9 <= cidr <= 16:
                return "B"
            elif 17 <= cidr <= 24:
                return "C"
            elif 25 <= cidr <= 31:
                return "D/E"
        except OutofBoundsValueError as e:
            print(f"Error: {e}")
            return None

    def netmask_to_netid(self):
        try:
            ip_data = self.ip_data
            cidr = ip_data[4]
            ip_int = (ip_data[0] << 24) | (ip_data[1] << 16) | (ip_data[2] << 8) | ip_data[3]
            mask = (0xFFFFFFFF << (32 - cidr)) & 0xFFFFFFFF
            netid_int = ip_int & mask
            return [(netid_int >> 24) & 0xFF, (netid_int >> 16) & 0xFF, (netid_int >> 8) & 0xFF, netid_int & 0xFF]
        except OutofBoundsValueError as e:
            print(f"Error: {e}")
            return None

    def network_address_no_bitwise(self, ip_octets, mask_octets):
        net = []
        for ip, mask in zip(ip_octets, mask_octets):
            if mask == 255:
                net.append(ip)
            elif mask == 0:
                net.append(0)
            else:
                block = 256 - mask
                net.append(ip - (ip % block))
        return net

    def display_results(self):
        try:
            # Passes user input to the display function
            ip_data = self.user_input()
            self.ip_data = ip_data
            cidr_value = ip_data[4]

            # Passes CIDR and Class to the display function
            sbnmsk = self.cidr_to_netmask(cidr_value)
            net_class = self.netmask_to_class(cidr_value)

            net_id = self.netmask_to_netid()
            broadcast = self.calculate_broadcast_address(ip_data[:4], cidr_value)

            # Convert to string for comparison
            ip_str = f"{ip_data[0]}.{ip_data[1]}.{ip_data[2]}.{ip_data[3]}"
            netid_str = f"{net_id[0]}.{net_id[1]}.{net_id[2]}.{net_id[3]}"
            broadcast_str = f"{broadcast[0]}.{broadcast[1]}.{broadcast[2]}.{broadcast[3]}"

            # Calculate first and last usable addresses
            netid_int = (net_id[0] << 24) | (net_id[1] << 16) | (net_id[2] << 8) | net_id[3]
            broadcast_int = (broadcast[0] << 24) | (broadcast[1] << 16) | (broadcast[2] << 8) | broadcast[3]

            if cidr_value < 31:
                first_usable_int = netid_int + 1
                last_usable_int = broadcast_int - 1
                first_usable = [
                    (first_usable_int >> 24) & 0xFF,
                    (first_usable_int >> 16) & 0xFF,
                    (first_usable_int >> 8) & 0xFF,
                    first_usable_int & 0xFF,
                ]
                last_usable = [
                    (last_usable_int >> 24) & 0xFF,
                    (last_usable_int >> 16) & 0xFF,
                    (last_usable_int >> 8) & 0xFF,
                    last_usable_int & 0xFF,
                ]
            else:
                # /31 and /32 have special cases
                first_usable = last_usable = None

            print(f"\nIP Address: {ip_str}")
            print(f"CIDR: /{cidr_value}")
            print(f"Subnet Mask: {sbnmsk[0]}.{sbnmsk[1]}.{sbnmsk[2]}.{sbnmsk[3]}")
            print(f"Class: {net_class}")
            print(f"Network Address: {netid_str}")
            print(f"Broadcast Address: {broadcast_str}")

            if ip_str == netid_str:
                print("Note: The entered IP is the network address (network ID) of this subnet.")

            if first_usable and last_usable:
                print(f"First usable address: {first_usable[0]}.{first_usable[1]}.{first_usable[2]}.{first_usable[3]}")
                print(f"Last usable address: {last_usable[0]}.{last_usable[1]}.{last_usable[2]}.{last_usable[3]}")
            else:
                print("No usable host addresses in this subnet (point-to-point or single host network).")

        except OutofBoundsValueError as e:
            print(f"Error: {e}")
        except ValueError:
            print("Error: Please enter valid IP address and CIDR values.")


if __name__ == "__main__":
    data = Data_Collector()
    data.display_results()
