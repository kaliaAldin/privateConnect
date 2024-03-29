import socket
import threading
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ipaddress = socket.gethostname()

port = 6001
server.bind((ipaddress, port))
server.listen(6)
users_dict = {}
print("server is listening")

connected = True


# client , address = server.accept()
#def handle_users(conn, address):



def recive_msg(conn, address):
    while True:
        msg = conn.recv(1024).decode()
        print(f'{users_dict[conn]}: {str(msg)}')
        if msg.upper() == "QUIT":
            print(f'{users_dict[conn]} disconnected')
            break
    conn.close()



#def send_msg(conn, msg):
    #while True:
        #conn.send(msg.encode())


while connected:
    try:
        conn, address = server.accept()
        conn.send("connection succeful provide a screen name : ".encode())

        alias = conn.recv(1024).decode()
        users_dict[conn] = alias
        print(f"{alias} connected to the server ")
        print(users_dict.values())
        #msg = input('send--->')
        #firstThread = threading.Thread(target=send_msg, args=(conn, msg))
        #firstThread.start()
        secondThread = threading.Thread(target=recive_msg , args=(conn,address))
        secondThread.start()
        secondThread.join()
    except KeyboardInterrupt:
        connected= False

        server.close()
        print('server disconnected')
        sys.exit()

