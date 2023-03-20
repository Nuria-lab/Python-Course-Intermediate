#making a browser

## networked programs: resources on the network using python
##sockets in python
##tcp protocol: transport control protocol

##starting with the communciation betwwn two computers (client and server)
#creates a conexion bw the two parts, to talk, and to listen
#in computing networking, an internet socket or network socket, is an 
#endpoint of a bidirectional iter.process communication flow
#across an internet protocol.based computer network, such as internet
#a socket call, si that call to a server // a port is an software communication endpoint
#common ports: telnet23 - login, ssh 22 - secure login , http 80, https 443 - secure, smtp 25 - mail, imap 143 220 993 - mail retrieval, pop 109 110 - mail retrieval, dns 53 - domain name, ftp 21 - file transfer



#now application protocols
#http is the hypertext transfer protocol, the dominant app layer protocol on the internet.
#a protocl is a set of rules we all agree to use to predict behaviour-, choosing sides of the connection
#http is a protocol to get data from a server: client: GET request, server: returns html document
#the standars of the internet protocols are developed by IETF: internet engineering tasks force. 
#standars: GET http://www.whatever.com/index.htm HTTP/1.0

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

#cmd= 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()  #not working at all
#cmd= 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()   #not working well
cmd = 'GET /romeo.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode('utf-8') #working

mysock.send(cmd)


while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode('utf-8'))

mysock.close()


# another 
