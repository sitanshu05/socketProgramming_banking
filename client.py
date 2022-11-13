import socket
port = 8041

s = socket.socket()

s.connect(('127.0.0.1',port))

cmd = input()
s.send(cmd.encode())
print(s.recv(1024).decode())

s.close()