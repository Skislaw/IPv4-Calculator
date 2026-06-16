import service

def run():
    print("Welcome to the service!")
    print("Type help for help")

    while True:
        user_choice = input(">")

        match user_choice:
            case "help":
                print("Commands:")
                print("help - Show this menu")
                print("divideBySubnets - Divide a network by number of subnets")
                print("divideByHosts  - Divide a network by number of hosts")
                print("exit - Exit the service")

            case "divideBySubnets":
                address = service.get_ip_address()
                mask = service.get_subnet_mask()
                network = service.create_network(address, mask)
                subnets = input("Number of subnets: ")
                try:
                    int(subnets)
                except ValueError:
                    print("Not an integer!")

                try:
                    subnet_list = (service.divide_network(network, int(subnets)))
                except ValueError:
                    print("Wrong number of subnets!")

                subnet_list = (service.divide_network(network, int(subnets)))
                i = 1
                for subnet in subnet_list:
                    print()
                    print(f"Subnet {i}:")
                    service.print_info(subnet)
                    i += 1

            case "divideByHosts":
                address = service.get_ip_address()
                mask = service.get_subnet_mask()
                network = service.create_network(address, mask)

                print("*Type q to stop assigning hosts numbers.")
                host_list = []

                n = 1
                while True:
                    value = input(f"Number of hosts in subnet {n}: ")

                    if value == "q":
                        break

                    try:
                        hosts = int(value)

                        if hosts < 1:
                            print("Wrong number of hosts!")
                            continue

                        host_list.append(hosts)
                    except ValueError:
                        print("Please enter a valid number of hosts or q")
                    n += 1

                if(host_list == []):
                    print("No hosts requirements provided!")
                    continue

                try:
                    result = service.vlsm(network, host_list)

                    i = 1
                    for hosts, subnet in result:
                        print()
                        print(f"{hosts} hosts -> subnet {i}:")
                        service.print_info(subnet)
                        i += 1

                except ValueError as e:
                    print("error")
                    
            case "showInfo":
                address = service.get_ip_address()
                mask = service.get_subnet_mask()
                network = service.create_network(address, mask)
                service.print_info(network)

            case "exit":
                print("Leaving service...")
                exit(0)

run()