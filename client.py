import socket
from threading import Thread
from tkinter import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = "127.0.0.1"
port = 8000
client.connect((ip_address, port))
print("Connected with Server", ip_address+':'+str(port))


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.withdraw()
        self.login = Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=300)
        self.pls = Label(self.login, text="Login to Continue",
                         justify=CENTER, font=("Verdana"))
        self.pls.place(relheight=0.15, relx=0.2, rely=0.07)
        self.label_name = Label(self.login, text="Name", font=("Verdana"))
        self.label_name.place(relheight=0.2, relx=0.1, rely=0.2)
        self.entry_name = Entry(self.login, text="", font=("Verdana"))
        self.entry_name.place(
            relwidth=0.4, relheight=0.12, relx=0.35, rely=0.2)
        self.entry_name.focus()
        self.go = Button(self.login, text="Continue", font=(
            "Verdana"), command=lambda: self.go_ahead(self.entry_name.get()))
        self.go.place(relx=0.2, rely=0.5)
        self.window.mainloop()

    def go_ahead(self, name):
        self.login.destroy()
        self.name = name
        rcp = Thread(target=self.receive)
        rcp.start()

    def receive(self):
        while True:
            try:
                message = client.recv(2048).decode("utf-8")
                if message == "nickname":
                    client.send(self.name.encode("utf-8"))
                else:
                    pass
            except:
                print("An error occured.")
                client.close()
                break


g = GUI()


# ======================== CLI ==============================

# nick = input("Enter nickname: ")

# def recieve():
#     while True:
#         try:
#             msg = client.recv(2048).decode("utf-8")
#             if msg == 'nickname':
#                 client.send(nick.encode('utf-8'))
#             else:
#                 print(msg)
#         except:
#             print("Sorry! An error occured.")
#             client.close()
#             break


# def write():
#     while True:
#         msgtxt = input("")
#         if msgtxt == ":q":
#             client.send("exit".encode("utf-8"))
#             quit()
#         else:
#             msg = '{}:{}'.format(nick, msgtxt)
#             client.send(msg.encode('utf-8'))


# recieve_thread = Thread(target=recieve)
# recieve_thread.start()

# write_thread = Thread(target=write)
# write_thread.start()
