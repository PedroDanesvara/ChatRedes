from socket import *

servidor = "127.0.0.1"
porta = 43210

while True:
    obj_socket = socket(AF_INET, SOCK_STREAM)
    obj_socket.connect((servidor, porta))
    msg = bytes(input("Sua mensagem: "), 'utf-8')
    obj_socket.send(msg, 1)
    resposta = obj_socket.recv(1024)
    print("Client: ", str(resposta)[2:-1])
obj_socket.close()
