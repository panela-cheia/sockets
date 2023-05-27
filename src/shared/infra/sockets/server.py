import socket
import json

from config.app_url import HOST,PORT
from base.base import Bootstrap

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
        socket.send(message.encode())
        socket.send(bytearray([EOF]))

    def read(self,socket: socket )-> str:
        message = ""
        EOF = 0x05
        while True:
            msg = socket.recv(4096)
            if not msg: break
            if msg[len(msg) - 1] == EOF:
                message += str(msg[: len(msg) - 1].decode())
                break
            else:
                message+=str(msg.decode())
        return message
    
    async def start(self,con):
        bootstrap = Bootstrap()

        while True:
            message = self.read(con)
            if not message: break

            message = await bootstrap.run(message=message)

            self.send(socket=con,message=json.dumps(message))