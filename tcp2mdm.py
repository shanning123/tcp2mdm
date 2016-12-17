#!/usr/bin/env python

"this is a module to transfer message between tcp socket and modem port"

import threading, serial, socket


BOUND_RATE = 19600


def tcp_thread():
    print 'tcp_thread started'

    HOST=''
    PORT=4754
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    while 1:
        conn, addr = s.accept()
        print 'Connected by', addr
        while 1:
            data = conn.recv(1024)
            print 'received data'

    print 'tcp_thread exit'

def mdm_thread():
    print 'mdm_thread started'

    print 'mdm_thread exit'

if __name__=='__main__':
    print 'tcp2mdm module enter'

    t = threading.Thread(target=tcp_thread)
    t.start()
    t = threading.Thread(target=mdm_thread)
    t.start()

    print 'tcp2mdm module exit'




