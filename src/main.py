import threading
import asyncio

from shared.infra.sockets.server import Server

async def start_server(server:Server,con):
    await server.start(con)

def start_async_server(server:Server,con):
    asyncio.run(start_server(server=server,con=con))

if __name__ == "__main__":
    server = Server()

    while True:
        con, client = server.tcp.accept()
        print("Conectado por", client)
        threading.Thread(target=start_async_server, args=(server,con,)).start()
        print("Conectado com o client foi finalizada!", client)