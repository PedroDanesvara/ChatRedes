from socket import *

servidor = "127.0.0.1"
porta = 43210

while True:
    obj_socket = socket(AF_INET, SOCK_STREAM)
    obj_socket.connect((servidor, porta))
    msg = bytes(input("Sua mensagem: ") + "3", 'utf-8')
    obj_socket.send(msg)
obj_socket.close()