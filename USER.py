import  socket
import  sys
import  customtkinter
import  tkinter


from client import  Client
ipaddress = socket.gethostname()

port = 6001

customtkinter.set_appearance_mode("system")

app = customtkinter.CTk()
app.geometry("600x500")
app.title("CTk example")
client = Client(ipaddress,port)

def send_alias():
   msg= aliasEntry.get()
   client.send_msg(msg)

def server_msg():
    return  client.recive()


servermsg = customtkinter.CTkLabel(app, width=100 , height=50 ,text=server_msg())
servermsg.grid(row=0)

alias = customtkinter.CTkLabel(app, width=100 , height=50 ,text="Screen Name:" )
alias.grid(row = 1 , column=0, padx=0)

aliasEntry = customtkinter.CTkEntry(app , height=25 )
aliasEntry.grid(row = 1, column=1, padx=0)

ButtonElias = customtkinter.CTkButton(app, text="Submit", command=send_alias , height= 25)
ButtonElias.grid(row=1 , column=2 , padx=10)





app.mainloop()

