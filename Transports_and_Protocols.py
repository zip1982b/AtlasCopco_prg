import asyncio
from assemblyMessages import Message, assemblyHeader, MID

class ClientOpenProtocol(asyncio.Protocol):
    def __init__(self, message, loop):
        #self.message = message
        self.loop = loop

    def connection_made(self, transport):
        print("TCP connect")
        transport.write(self.message)
        print('Data sent: {!r}'.format(self.message))

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()


loop = asyncio.get_event_loop()
message = Message(assemblyHeader(MID['Communication_start']))
coro = loop.create_connection(lambda: ClientOpenProtocol(message, loop),
                              '192.168.8.1', 4545)
loop.run_until_complete(coro)
loop.run_forever()
loop.close()



