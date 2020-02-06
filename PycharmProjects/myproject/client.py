import socket

HOST = '172.17.0.9'
PORT =8000

request = 'canyou hear me?'

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

s.sendall(request.encode())

reply = s.recv(1024).decode()

print('reply is:',reply)

s.close()