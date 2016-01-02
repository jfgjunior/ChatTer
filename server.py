import socket
import sys
from thread import start_new_thread
class Server(object):
    def __init__(self):
        self.lista = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', 5000))
        self.sock.listen(10)

    def Start(self):
        while True:
            conn, addr = self.sock.accept()
            server.lista.append(conn)
            start_new_thread(self.Run, (conn,))
        self.sock.close()


    def Online(self, args):
        sock = args[0]
        sock.send('Online users:\n')
        for name in self.lista:
            sock.send('    - '+name[1])

    def Run(self, conn):
        commands = {'/online' : self.Online,} #Add new commands
        name = conn.recv(1024) #Receive client name
        self.lista[-1] = (conn, name) #Save socket and client name
        self.lista[-1][0].setblocking(False)
        #Show for all clients who entered
        for i in self.lista:
            mensagem = name + ' entered'
            i[0].send(mensagem)
        #chat
        up = True
        while up:
            for i in self.lista:
                try:
                    msg = i[0].recv(1024)
                except Exception:
                    continue

                if msg[0] == '/':
                    try:
                        commands[msg]([i[0]])
                    except Exception:
                        pass
                elif msg == 'exit':
                    index = self.lista.index(i)
                    up = False
                    break
                else:
                    for j in self.lista:
                        if msg:
                            j[0].send(i[1] + ' said:\n' + msg + '\n')
        self.lista[index][0].shutdown(True)
        self.lista.pop(index)

server = Server()
server.Start()
