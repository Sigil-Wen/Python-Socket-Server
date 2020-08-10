import socket

HEADER = 64 #used for protocol, every first message to server is header length 64 and tells the byte of message, 
PORT = 5050
#SERVER = "192.168.0.15"
SERVER = socket.gethostbyname(socket.gethostname()) #gets ip address from desktop host name
ADDR = (SERVER, PORT)  #bind socket
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("bruh sound effect #3")
send("societ")

send(DISCONNECT_MESSAGE)