from socket import *

servidor = "127.0.0.1"
porta = 43210

while True:
    obj_socket = socket(AF_INET, SOCK_STREAM)
    obj_socket.connect((servidor, porta))
    msg = bytes(input("Sua mensagem: ") + "1", 'utf-8')
    obj_socket.send(msg)
    resposta = str(obj_socket.recv(1024))
    print(f"Cliente {str(resposta)[-3:-2]}: ", str(resposta)[4:-3])
obj_socket.close()