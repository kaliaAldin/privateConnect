import socket
import sys
import customtkinter
import tkinter

from client import Client

ipaddress = socket.gethostname()

port = 6001

customtkinter.set_appearance_mode("system")

app = customtkinter.CTk()
app.geometry("600x500")
app.title("CTk example")
client = Client(ipaddress, port)


def start_msging():
    received_msg.grid(row=1)

    msgEntry.grid(row=2)

    sendButton.grid(row=3, pady=10)


def send_alias():
    msg = aliasEntry.get()
    client.send_msg(msg)
    alias.grid_forget()
    serverMsg.grid_forget()
    aliasEntry.grid_forget()
    ButtonElias.grid_forget()
    start_msging()


def send_msg():
    msg = msgEntry.get()
    client.send_msg(msg)
    msgEntry.select_clear()


def server_msg():
    return client.recive()


def quiting():
    client.send_msg('quit')
    sys.exit()


# component for  sharing a new screen name
# Label to receive first server msg
serverMsg = customtkinter.CTkLabel(app , text=server_msg())
serverMsg.grid(row=0 ,padx=2 )
# label to  for screen name
alias = customtkinter.CTkLabel(app, text="Screen Name:", anchor="w")
alias.grid(row=5, column=0, padx=0, pady=5, sticky="w")
# Entry for screen name
aliasEntry = customtkinter.CTkEntry(app)
aliasEntry.grid(row=5, column=1, padx=0)
# Button to submit screen name
ButtonElias = customtkinter.CTkButton(app, text="Submit", command=send_alias)
ButtonElias.grid(row=5, column=2, padx=5)

# component for the received msg
received_msg = customtkinter.CTkLabel(app, bg_color="white", text="Place Holder")
# component for sending msg
msgEntry = customtkinter.CTkEntry(app)
sendButton = customtkinter.CTkButton(app, text="send", command=send_msg)

# quiting component

quitButton = customtkinter.CTkButton(app, text="Quit",fg_color="red", command=quiting)
quitButton.grid(row=0, column=2)

app.mainloop()
