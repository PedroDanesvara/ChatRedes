from concurrent.futures import thread
from socket import *
from threading import Thread

servidor = "127.0.0.1"
porta = 43210

def main():
    obj_socket = socket(AF_INET, SOCK_STREAM)
    try:
        obj_socket.connect((servidor, porta))
    except :
        return print('Deu ruim')
    thread1 = Thread(target = recvMsg, args = [obj_socket])
    thread2 = Thread(target = sndMsg, args = [obj_socket])
    thread1.start()
    thread2.start()

def recvMsg(con):
        while True:
            try:
                msg = con.recv(1024).decode('utf-8')
                print(f'{msg}\n')
            except:
                con.close()
                break

def sndMsg(con):
        while True:
            try:
                msg = input('Digite:   ')
                con.send(f'{msg}'.encode('utf-8'))
            except:
                return

main()

