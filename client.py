# -*- coding: utf-8 -*-
import socket
from thread import start_new_thread

class Client(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('', 5000))
        self.sock.send(raw_input('Name: '))
        self.sock.setblocking(True)
        start_new_thread(self.Send, (self.sock,))

    def Send(self, sock):
        while True:
            msg = raw_input()
            if msg != '':
                sock.send(msg)
            if msg == 'exit':
                break
        sock.shutdown(True)
        print '[+] Exiting...'

    def Start(self):
        while True:
            msg = self.sock.recv(1024)
            if not msg:
                break
            print msg
        print '[+] Exit'

client = Client()
client.Start()
