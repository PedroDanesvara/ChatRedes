from socket import *

servidor = "127.0.0.1"
porta = 43210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor, porta))
obj_socket.listen(5)
print("Aguardando cliente...")

while True:
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print(f"Cliente {str(msg_recebida[-2:-1])}: ", str(msg_recebida)[2:-2])
        msg_enviada = bytes(msg_recebida, 'utf-8')
        con.send(msg_enviada)
        break
    con.close()
