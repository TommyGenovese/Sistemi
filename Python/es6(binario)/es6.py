import ipaddress

network = ipaddress.ip_network("192.168.1.0/24")
hosts = list(network.hosts())

subnets = {"start_address": str(list(subnet.hosts())[0]),"end_address": str(list(subnet.hosts())[-1])}

print(subnets)

hosts = list(network.hosts())
subnets = [{"start_address": str(subnet[0]), "end_address": str(subnet[-1])}

for subnet in (hosts[:len(hosts)//2], hosts[len(hosts)//2:])]
print(subnets)







    
