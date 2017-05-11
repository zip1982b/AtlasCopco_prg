import asyncio
from assemblyMessage_v2 import message, assembly_header, MID

async def tcp_open_protocol_client(message, assembly_header, MID, loop):
    reader, writer = await asyncio.open_connection('192.168.8.1', 4545, loop=loop)  # необходимо добавить код в случае возникновения исключения
                                                                                    # необходимо добавить - IP передавать в качестве аргумента
    count = 0;
    print('Send: %r' % message(assembly_header(MID['Communication_start'])))
    writer.write(message(assembly_header(MID['Communication_start'])).encode())


    data = await reader.read(100)
    print('Received: %r' % data.decode())
    if data:
        msg = data.decode()
        PFname = msg[32:46]
        if msg[4:8] == MID['Communication_start_acknowledge']:
            print('PF name:', PFname, 'connected')
        elif msg[4:8] == MID['Command_error']:
            print('Command error, Client already connected or MID revision unsupported or more five connections')

    else:
        count += 1



    print('Close the socket')
    writer.close()

message = 'Hello World!'
loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_open_protocol_client(message, assembly_header, MID, loop))
loop.close()