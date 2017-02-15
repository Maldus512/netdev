#!/usr/bin/env python
from socket import *
import thread
from select import select
from device.unix import *
 
BUFF = 1024
HOST = '0.0.0.0'# must be input parameter @TODO
PORT = 9999 # must be input parameter @TODO

 
def handler(clientsock,addr):
    dev = Device()
    while 1:
        read, write, err = select([clientsock], [], [])
        if not read:
            continue
        data = read[0].recv(BUFF)
        data = data.strip('\n')
        dev.send(data) 
        print 'data:' + repr(data)
        if not data:
            break
        read[0].send(b"echo:" + data)

    dev.close()
    clientsock.close()
 
if __name__=='__main__':
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)
    while 1:
        print 'waiting for connection...'
        clientsock, addr = serversock.accept()
        print '...connected from:', addr
        thread.start_new_thread(handler, (clientsock, addr))
