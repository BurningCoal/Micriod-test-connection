from netmiko import ConnectHandler
t=open("devicelist.txt","r")
g=t.readlines()
for z in range(0,len(g)-1):
    z=z.split(",")
    conn= {
    'device_type': 'cisco_ios',
    'host':   z[1],
    'username': z[2],
    'password': z[3],
    'port' : 22,         
    'secret': 'secret',
    }
    net_connect = ConnectHandler(**conn)
    output = net_connect.send_command('show cdp neighbors detail')
    print(output)
