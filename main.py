import socket
import sys
from assemblyMessage_v2 import message, assembly_header, MID


def work_PF4000():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.8.1'
    port = 4545
    s.connect((host, port))
    print("connected on TCP")
    s.send(message(assembly_header(MID['Communication_start'])).encode())

    data = s.recv(1000)
    dataASCII = data.decode("ascii")
    print('recivied:', dataASCII, len(data), 'bytes')
    print("close socket - disconected ...")
    s.close()



def connecting_again():
    try:
        work_PF4000()
    except Exception as ex:
        template = "An exeption of type {0} occured. Arguments: \n{1!r}"
        mes = template.format(type(ex).__name__, ex.args)
        print(mes)



count = 3
while count > 0:
    connecting_again()
    count = count - 1


print("end prg ...... ")
