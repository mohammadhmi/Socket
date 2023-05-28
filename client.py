import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('localhost', 12021))

message = input("Enter any message for server: ")
while message.strip() != '!quit':
    
    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()
    print("Received response:", response)

    message = input("Enter any message for server: ")

client_socket.close()
