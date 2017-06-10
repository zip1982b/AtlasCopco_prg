import asyncio
import sys
from assemblyMessage_v2 import message, assembly_header, MID

async def tcp_open_protocol_client(assembly_header, MID, loop):
    try:
        reader, writer = await asyncio.open_connection('192.168.8.1', 4545, loop=loop)  # необходимо добавить код в случае возникновения исключения

    except(Exception):
        print('exeption')
        print(sys.exc_info()[1])
    else:
        count = 0;

        print('Send: %r' % message(assembly_header(MID['Communication_start'])))
        writer.write(message(assembly_header(MID['Communication_start'])).encode())
        data = await reader.read(1000)
        print('Received: %r' % data.decode())
        if data:
            msg = data.decode()
            PFname = msg[32:46]
            if msg[4:8] == MID['Communication_start_acknowledge']:
                print('PF name:', PFname, 'connected')
                writer.write(message(assembly_header(MID['VIN_subscribe'])).encode())
                print('Send: %r' % message(assembly_header(MID['VIN_subscribe'])))
                data = await reader.read(1000)
                print('Received: %r' % data.decode())
                if data:
                    msg = data.decode()
                    if msg[4:8] == MID['Command_accepted']:
                        while True:
                            data = await reader.read(1000)
                            if data:
                                print('Received: %r' % data.decode())
                                msg = data.decode()
                                if msg[4:8] == MID['VIN']:
                                    writer.write(message(assembly_header(MID['VIN_acknowledge'])).encode())
                                    print('Send: %r' % message(assembly_header(MID['VIN_acknowledge'])))



            elif msg[4:8] == MID['Command_error']:
                print('Command error, Client already connected or MID revision unsupported or more five connections')

        else:
            count += 1

        print('Close the socket')
        writer.close()
        # необходимо добавить - IP передавать в качестве аргумента
    print("continue........")



loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_open_protocol_client(assembly_header, MID, loop))   # возможно в будущем run_forever()
loop.close()