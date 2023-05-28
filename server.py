import socket

def reverse_string(string):
    reverse = string[::-1]
    if reverse[-1].isupper():
      reverse = reverse[0].upper() + reverse[1:-1] + reverse[-1].lower()
    return reverse

def uppercase_string(string):
    return string.upper()
    

def lowercase_string(string):
    return string.lower()

def capitalize_string(string):
    return string.capitalize()

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode()
        print("Received message:", message)
        option = input("Enter an option (1:Reverse , 2:Uppercase , 3:Lowercase , 4:Capitalize): ")
        if option == "1":
            response = reverse_string(message)
        elif option == "2":
            response = uppercase_string(message)
        elif option == "3":
            response = lowercase_string(message)
        elif option == "4":
            response = capitalize_string(message)
        else:
            response = "Invalid option"
        client_socket.send(response.encode())
    client_socket.close()

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('localhost', 12021))
server_socket.listen(5)


while True:
    client_socket, address = server_socket.accept()
    print("Accepted connection from", address[0], "on port", address[1])
    handle_client(client_socket)
    