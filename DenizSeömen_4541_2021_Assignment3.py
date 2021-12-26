from netmiko import ConnectHandler
t=open("devicelist.txt","r")
g=t.readlines()
g=g[2]
for z in range(0,3):
    z=g.split(",")
    z[4]=str(z[4])
    print(z[4])
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
