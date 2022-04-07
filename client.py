import socket
from threading import Thread

nick = input("Enter nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = "127.0.0.1"
port = 8000
client.connect((ip_address, port))

commands = [":q"]


print("Connected with Server", ip_address+':'+str(port))


def recieve():
    while True:
        try:
            msg = client.recv(2048).decode("utf-8")
            if msg == 'nickname':
                client.send(nick.encode('utf-8'))
            else:
                print(msg)
        except:
            print("Sorry! An error occured.")
            client.close()
            break


def write():
    while True:
        msgtxt = input("")
        if msgtxt == ":q":
            client.send("exit".encode("utf-8"))
            quit()
        else:
            msg = '{}:{}'.format(nick, msgtxt)
            client.send(msg.encode('utf-8'))


recieve_thread = Thread(target=recieve)
recieve_thread.start()

write_thread = Thread(target=write)
write_thread.start()
