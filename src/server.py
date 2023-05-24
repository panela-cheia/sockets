import socket

from config.app_url import HOST,PORT

class Server:
    def __init__(self) -> None:
        self.HOST = HOST
        self.PORT = PORT
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.orig = (self.HOST, self.PORT)
        self.tcp.bind(self.orig)
        self.tcp.listen(5)

    def send(self,message: str,socket: socket):
        EOF = 0x05
        socket.send(message.enconde())
        socket.send(bytearray([EOF]))