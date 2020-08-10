import socket
import threading #allows us to seperate clients

HEADER = 64 #used for protocol, every first message to server is header length 64 and tells the byte of message, 
PORT = 5050
#SERVER = "192.168.0.15"
SERVER = socket.gethostbyname(socket.gethostname()) #gets ip address from desktop host name
ADDR = (SERVER, PORT)  #bind socket
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket, first param is family of socket (over internet), type of addresses
server.bind(ADDR) 

def handle_client(conn, addr): #handles individual connections
    print(f"[NEW CONNECTION] {addr} connected.") #prints ip of who connected
    connected = True 
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #blocking line, recieves bytes from socket, converts from bytes into string using utf-8
        if msg_length: 
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
    conn.close()

def start(): #handles new connections to server
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        #blocking line of code
        conn, addr = server.accept() #conn is socket object, addr is ip address 
        #waits on new connections
        thread = threading.Thread(target=handle_client, args=(conn, addr)) #adds new thread
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}") #prints number of active connections with threads

print("[STARTING] server is starting...")
start()