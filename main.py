import socket
import sys
from assemblyMessage_v2 import message, assembly_header, MID



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.8.1'
port = 4545
try:
    s.connect((host, port))
    print("connected")
    s.send(message(assembly_header(MID['Communication_start'])).encode())

    data = s.recv(1000)
    dataASCII = data.decode("ascii")
    print('recivied:', dataASCII, len(data), 'bytes')

    s.close()

except ConnectionRefusedError:
    print("connection error")
    print("connection again ... ")
    try:
        s.connect((host, port))
    except ConnectionRefusedError:
        print("connection error 2")




print("end prg ...... ")



#sendData = b'002000010000000000000' #количество байт для передачи должно быть больше на 1
# Python скорее всего считает на 1 больше
# а может быть нужно добовлять Message end - nul,
# NUL необходимо добавлять к сообщению


