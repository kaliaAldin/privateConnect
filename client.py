import socket
import sys



ipaddress = socket.gethostname()

port = 6001



class Client:
    def __init__(self, ipaddress , port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ipaddress = ipaddress
        self.port = port
        self.client.connect((self.ipaddress, self.port))
    def send_msg(self, text):
        self.client.send(text.encode())

    def recive(self):
        msg = self.client.recv(1024)
        return msg.decode()
    def close_connection(self):
        self.client.close()



def main():
    client = Client(ipaddress,port)
    welcomemsg = client.recive()
    print(f'server is saying{welcomemsg}')
    alias = input('Alias: ')
    client.send_msg(alias)
    while True:
        text = input('--->')
        client.send_msg(text)
        if text.upper()== 'QUIT':
            break
    client.close_connection()
    sys.exit()


if __name__ == "__main__":
    main()



