from http.client import RemoteDisconnected
import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

list_of_clients = []
nicknames = []

print("Server has started...")


def clientthread(conn, nickname):
    conn.send("Welcome to this chatroom!".encode('utf-8'))
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                if message == "exit":
                    remove(conn)
                    remove_nickname(nickname)
                else:
                    print(message)
                    broadcast(message, conn)
            else:
                remove(conn)
                remove_nickname(nickname)
        except:
            continue


def broadcast(msg, conn):
    for client in list_of_clients:
        if client != conn:
            try:
                client.send(msg.encode('utf-8'))
            except:
                remove(client)


def remove(conn):
    if conn in list_of_clients:
        list_of_clients.remove(conn)


def remove_nickname(nick):
    if nick in nicknames:
        nicknames.remove(nick)
    leavemsg = "{} left.".format(nick)
    print(leavemsg)
    broadcast(leavemsg)


while True:
    conn, addr = server.accept()
    conn.send("nickname".encode("utf-8"))
    nickname = conn.recv(2048).decode("utf-8")
    list_of_clients.append(conn)
    nicknames.append(nickname)
    msg = "{} joined.".format(nickname)
    print(addr[0] + " connected")
    print(msg)
    broadcast(msg, conn)
    new_thread = Thread(target=clientthread, args=(conn, nickname))
    new_thread.start()
