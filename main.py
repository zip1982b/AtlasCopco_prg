"""import socket
import sys
from assemblyMessages import Message, assemblyHeader, MID

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.39.23.82'
port = 4545
s.connect((host, port))

#Request message Communication Start
sendData = Message(assemblyHeader(MID['Communication_start']))
#print(sendData)
#print(len(sendData))
s.send(sendData)

#Request reply message
data = s.recv(1000)
answer = data.decode("utf-8")# type string
#print ('recivied:', answer, len(data), ':bytes')
PFname = answer[32:46]
if data[4:8]==MID['Communication_start_acknowledge']:
        print('PF name:',PFname, 'connected' )
elif data[4:8]==MID['Command_error']:
        print('Command error, Client already connected or MID revision unsupported or more five connections')

z=input()

#Request message Communication Stop
sendData = Message(assemblyHeader(MID['Communication_stop']))
#print(sendData)
#print(len(sendData))
s.send(sendData)

#Request reply message
data = s.recv(1000)
answer = data.decode("utf-8") # type string
#print ('recivied:', answer, len(data), ':bytes')
if data[4:8]==MID['Command_accepted']:
        print('PF name:',PFname, 'disconnected' )

s.close() # закрываем сокет
"""
import asyncio
from assemblyMessages import Message, assemblyHeader, MID

class ClientOpenProtocol(asyncio.Protocol):
    def __init__(self, message, loop):
        self.message = message
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



