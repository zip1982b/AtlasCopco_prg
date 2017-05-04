import asyncio
from assemblyMessages import Message, assemblyHeader, MID



async def tcp_OpenProtocolClient(Message, assemblyHeader, MID, loop):
    reader, writer = await asyncio.open_connection('192.168.8.1', 4545,
                                                        loop=loop)


    message = Message(assemblyHeader(MID['Communication_start']))



    print('Send: %r' % message.decode())
    writer.write(message)

    data = await reader.read(1000)
    print('Received: %r' % data.decode())


    PFname = data[32:46]
    if data[4:8] == MID['Communication_start_acknowledge']:
        print('PF name:', PFname, 'connected')
    elif data[4:8] == MID['Command_error']:
        print('Command error, Client already connected or MID revision unsupported or more five connections')

    print('Close the socket')
    writer.close()

message = 'Hello World!'
loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_OpenProtocolClient(Message, assemblyHeader, MID, loop))
loop.close()