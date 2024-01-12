import socket
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ipaddress = '192.168.1.2'

port = 6001

#screen_name = input("choose a screen name : ")

client.connect((ipaddress, port))
serverWelcome = client.recv(1024).decode()
print(f'server is saying{serverWelcome}')


def send_msg(client , text):


    client.send(text.encode())


def recive_msg(client , text):
    msg = client.recv(1024).decode()
    print(msg)


while True:
    text = input("-->")
    send_msg(client,text)
    if text.upper()=="QUIT":
        break
client.close()
sys.exit()

