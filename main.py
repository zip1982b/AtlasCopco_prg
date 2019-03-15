import socket
import sys
from assemblyMessage_v2 import message, assembly_header, MID
import parse

host = '192.168.8.1'
port = 4545

def mysend(arg_s, arg_msg, arg_MSGLEN):
    totalsent = 0
    print("send MSGLEN:")
    print(arg_MSGLEN)
    while totalsent < arg_MSGLEN:
        print(arg_msg[totalsent: ])
        sent = arg_s.send(arg_msg[totalsent: ])
        if sent == 0:
            raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent


def myreceive(arg_s, arg_MSGLEN):
    chunks = []
    bytes_recd = 0
    print("recv MSGLEN:")
    print(arg_MSGLEN)
    while bytes_recd < arg_MSGLEN:
        chunk = arg_s.recv(min(arg_MSGLEN - bytes_recd, 2048))
        if chunk == b'':
            raise RuntimeError("socket connection broken")
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)
    return b''.join(chunks)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port)) #connect TCP
except Exception as ex:
    template = "An exeption of type {0} occured. Arguments: \n{1!r}"
    mes = template.format(type(ex).__name__, ex.args)
    print(mes)


mysend(s, message(assembly_header(MID['Communication_start'])).encode(), len(message(assembly_header(MID['Communication_start']))))
# здесь необходимо поставить таймер на возврат ответа
recv_data = myreceive(s, 57)
answer = recv_data.decode()

print(recv_data.decode())

prnt_head = "header:|{0}|received".format(parse.get_header(answer))
print(prnt_head)

prnt_length = "length:|{0}|received".format(parse.get_length(answer))
print(prnt_length)

prnt_mid = "mid:|{0}|received".format(parse.get_mid(answer))
print(prnt_mid)

prnt_rev = "revision:|{0}|received".format(parse.get_revision(answer))
print(prnt_rev)

prnt_no_ack_f = "no ack flag:|{0}|received".format(parse.get_no_ack_flag(answer))
print(prnt_no_ack_f)

prnt_s_id = "station ID:|{0}|received".format(parse.get_station_id(answer))
print(prnt_s_id)

prnt_sp_id = "spindle ID:|{0}|received".format(parse.get_spindle_id(answer))
print(prnt_sp_id)

prnt_spare = "spare:|{0}|received".format(parse.get_spare(answer))
print(prnt_spare)



if(parse.get_mid(answer) == MID['Communication_start_acknowledge']):
    print('connected on Open Protocol')
if(parse.get_mid(answer) == MID['Command_error']):
    print(parse.get_err_code(answer))














print("close socket - disconected ...")
s.close()


"""
def connecting_again():
    try:
        work_PF4000()
    except Exception as ex:
        template = "An exeption of type {0} occured. Arguments: \n{1!r}"
        mes = template.format(type(ex).__name__, ex.args)
        print(mes)

"""


print("end prg ...... ")
