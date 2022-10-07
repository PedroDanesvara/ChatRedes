from socket import *
import threading

clts = []

servidor = "127.0.0.1"
porta = 43210

def main():
    obj_socket = socket(AF_INET, SOCK_STREAM)
    try:
        obj_socket.bind((servidor, porta))
        obj_socket.listen()
        print("Aguardando cliente...")
    except:
        return print('Deu ruim 2')
    while True:
        con, cliente = obj_socket.accept()
        print("Conectado com: ", cliente)
        clts.append(con)
        thread = threading.Thread(target = tratMsg, args = [con])
        thread.start()

def rmvClts(con):
    clts.remove(con)

def tratMsg(con):
    while True:
        try:
            msg = con.recv(1024)
            mandClts(msg, con)
        except:
            rmvClts(con)
            break

def mandClts(msg_recebida, con):
    for cltsItm in clts:
        if cltsItm != con:
            try:
                cltsItm.send(msg_recebida)
            except:
                rmvClts(cltsItm)

main()


