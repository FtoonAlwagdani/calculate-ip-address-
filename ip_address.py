

import math
# ============== Function Defintions =========================
def swap(number):
    return str(255-number)
def validateIP(ip):

    # take the user input and split it to 4 octets in put them in an array named 'octets'    ['192,'168','1','1']
    octets = ip.split('.')

    # this is a boolean variable to indicate if the user input ip was correctly formated
    ipFormatted = True

    # first condition to make sure we have 4 octetes
    if len(octets) == 4:
    
        # ths loop is to validate that every octet is within the range 0-255
        for octet in octets:

            octetDigit  = int(octet)   

            if  octetDigit <0 or octetDigit >255:                                                                             
                ipFormatted = False
                break


    else:
        ipFormatted = False

    return ipFormatted
def getNetworkId(ip, mask):
    
    ipOctets = ip.split('.')
    maskOctets = mask.split('.')
    networkId=[]
    for i in range(0,4): # i: 0,1,2,3
        networkId.append(str(int(ipOctets[i]) & int(maskOctets[i]))) #   str(192)  
    
    return '.'.join(networkId)
def getCIDR(mask):
    maskOctets = mask.split('.')
    maskcombined = ''
    for octet in maskOctets:
        if(octet != '0'):
            maskcombined += bin(int(octet))[2:]
    return len(maskcombined.replace('0', ''))
def getMaximumNumberOfHosts(mask): 
    return  int(math.pow(2,32 - getCIDR(mask))- 2) 
def getTheFirstHostAddress(net_id):  
    firstHostAddress = net_id.split('.')
    firstHostAddress[3] = str(int(firstHostAddress[3]) + 1)
    return '.'.join(firstHostAddress)
def getTheBroadcastAddress(net_id, mask): 
    maskOctets = mask.split('.')
    wildCard = []

    for octet in maskOctets:
        wildCard.append(swap(int(octet)))

    netOctets = net_id.split('.')
    broadcast = []

    for i in range(0,4):    
        broadcast.append(str(int(netOctets[i]) | int(wildCard[i])))

    return '.'.join(broadcast)
def getTheLastHostAddress(net_id, mask): 
    lastHostAddress = getTheBroadcastAddress(net_id, mask).split('.')
    lastHostAddress[3] = str(int(lastHostAddress[3]) - 1)
    return '.'.join(lastHostAddress)
def printResults(ip, mask, net_id, max, first, broadcast, last):
    print('\n\n\n @ Subnetting (' + ip + ') with ' + mask + ' :')
    print("\n\t- The network ID: " + net_id + ' /' + str(getCIDR(mask))) 
    print("\n\t- The maximum number of hosts is: " + str(max))
    print("\n\t- The first host is: " + first)
    print("\n\t- The last host is: " + last)
    print("\n\t- The broadcast address is: " + broadcast)
    print("------------------------------")
def bitnumber (n):
    
    n=int(n)
    x=2
    for i in range(1,32):
        if n>x:
            x=2**i
        else:
            break 
    return i,x
def printresult2 (host ,net, cidr ,ip,  ips ):
    hostNum=str(host[1])
    networkNum=int(net[1])
    print("\n\t- Ip host's + bradcast + network = " + hostNum)
    print("\n\t- Networks  = " + str(networkNum))
    print("\n\t- Ip for all networks = " + ip + "/" + str(32 - (host[0]+ net[0])) )
    print( '    Network ID   |    First host   |    Last host   |    broadcast ' )
    for i in  range(len(ips)):
        ipaddress= ips[i] 
        print( str(i+1)  + " - " \
            + ipaddress+ "   |   "\
            + getTheFirstHostAddress(ipaddress)+ "   |   "\
            + getlasHostAddress(ipaddress , host ) + "   |   "\
            + getBroadcast(ipaddress, host))
def getlasHostAddress(ip , host):  
    lastHost = getBroadcast(ip , host ).split('.')
    lastHost[3] = str(int(lastHost[3]) - 1)
    return '.'.join(lastHost)
def getBroadcast(ip , host):
    netip=ip.split('.') 
    netip[3]=str (int(netip[3]) + int(host[1]-1))   # 0+ (64-1) . ( 192 +(64-1))
    return '.'.join(netip)
def networks (ip , host , net):
    network=int(net[1])-1
    netip=ip.split('.') 
    nextip =[ip]
    for i in range (network):  # 1
        octit3=int(netip[3]) + int(host[1])   # 0+64 .... 256
        octit2=0
        octit1=0
        octit0=0
        if octit3 >255:
            octit3=0
            octit2=int(netip[2]) + int(host[1])
            netip[3]=str(octit3)
            netip[2]=str(octit2)
            nextip.append('.'.join(netip))

            if octit2 >255:

                octit2=0
                octit3=0
                octit1=int(netip[1]) + int(host[1])
                netip[3]=str(octit3)
                netip[2]=str(octit2)
                netip[1]=str(octit1)
                nextip.append('.'.join(netip)) 

                if octit1 >255:

                    octit1=0
                    octit2=0
                    octit3=0 
                    octit0=int(netip[0]) + int(host[1])
                    netip[3]=str(octit3)
                    netip[2]=str(octit2)
                    netip[1]=str(octit1)
                    netip[0]=str(octit0)
                    nextip.append('.'.join(netip)) 
                    
        elif octit3 < 255:
            netip[3]=str(octit3)
            nextip.append('.'.join(netip))
        else :
            print("You have not enough IP address for your networks !!")
                        
    return nextip



#==============    Main Function     ========================

print("\n\t ATTENTION: To Skip The Operation Type \'n\'")
print('First Operation: calculate First And Last Hosts , Broadcast And Network ID')
print(''.center(10,'-'))
ip = input('Enter IP: ')                                       
ipValid = validateIP(ip) # boolean variable to state whether ip is valid 
if ipValid:  #i=0
    mask= input('Enter the sbunet mask: ') # get subnet mask from user
    networkId = getNetworkId(ip, mask) # get network id                                                                       
    maximumHosts= getMaximumNumberOfHosts(mask) # get maximum number of host
    firstHost = getTheFirstHostAddress(networkId) # get the first host in the network
    broadcast = getTheBroadcastAddress(networkId, mask) # get the broadcast address 
    lastHost = getTheLastHostAddress(networkId, mask) # get the last host in the network
    printResults(ip, mask, networkId, maximumHosts, firstHost, broadcast, lastHost) # print the results

elif ip.lower() == 'n':
    print('\nSecond Operation: Divide IP to many networks\n') 
    print(''.center(10,'-'))
    ip = input('Enter IP: ')
    ipValid = validateIP(ip)

    if ipValid:  
      mask= input('Enter the sbunet mask: ')
      host= input('How many host ? ') 
      net= input('How many network ? ') 
     
      numhost= bitnumber(int(host)+2) #broadcast + network  numhost[0]= number bit ,  numhost[1]= number of host
      numbnet= bitnumber(int(net))    #numhost[0]= number bit ,  numhost[1]= number of network
      cidr = getCIDR(mask)
      networksip = networks(ip, numhost , numbnet)
      printresult2(numhost,numbnet,cidr ,ip , networksip  )

    elif ip == 'n':
          print("You skiped all operations \U0001F642")

else:
    print('Sorry! I cant continue because you are stupid. why stupid? because you cant type a valid ip') # print error message to the user



