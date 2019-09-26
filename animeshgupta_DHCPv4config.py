#Animesh Gupta
#The purpose of this script is to login into each router and set "ip address dhcp" so that routers get IPv4 address
#!/usr/bin/env python


import threading
from netmiko import ConnectHandler
    
def Router_2(b):
    
    ios_r1={
    'device_type':'cisco_ios',
    'username':'lab',
    'password':'lab123',
    'ip':b,
    }
    
    net_connect = ConnectHandler(**ios_r1)
    configuration_set = ['interface fastEthernet 0/0','ip address dhcp']
    output = net_connect.send_config_set(configuration_set)
    #print (output)

def Router_3(c):
    
    ios_r1={
    'device_type':'cisco_ios',
    'username':'lab',
    'password':'lab123',
    'ip':c,
    }
    
    net_connect = ConnectHandler(**ios_r1)
    configuration_set = ['interface fastEthernet 0/0','ip address dhcp']
    output = net_connect.send_config_set(configuration_set)
    print (output)


def Router_4(d):
    
    ios_r1={
    'device_type':'cisco_ios',
    'username':'lab',
    'password':'lab123',
    'ip':d,
    }
    
    net_connect = ConnectHandler(**ios_r1)
    configuration_set = ['interface fastEthernet 0/0','ip address dhcp']
    output = net_connect.send_config_set(configuration_set)
    print (output)
    
if __name__ == "__main__":
    
    #a="198.51.100.10"
    b="198.51.100.20"
    c="198.51.100.30"
    d="198.51.100.40"
    #creating threads
    #t1 = threading.Thread(target=R1, args=(a,))
    t5 = threading.Thread(target = Router_2, args=(b,))
    t6 = threading.Thread(target = Router_3, args=(c,))
    t4 = threading.Thread(target=Router_4, args=(d,))
    #t1.start()
    t5.start()
    t6.start()
    t4.start()
    #t1.join()
    t5.join()
    t6.join()
    t4.join()
    #t2.stop()
    #t3.stop() 
