# server logic

import socket #for socket

HOST = "127.0.0.1"  # loopback address to the same mache
PORT = 65431 # port to listen (running the process) (non privilegeed ports are >1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s:
    s.bind((HOST, PORT))  # binds the host machine to the port
    s.listen()  #listening for the client machine
    conn, addr = s.accept() #connection id
    with conn:
        print("Connected by: ",addr)
        while True:
            data = conn.recv(1024)
            if data=="bye":  #if there are no data being recieved
                print("The person you were talking to left")
                break
            print(data)
            message=input("message: ")
            if(message=="bye"):
                print("Over and Out")
                break
            conn.sendall(message.encode())
        conn.close()
    s.close()
