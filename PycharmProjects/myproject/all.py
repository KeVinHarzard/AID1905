import socket

HOST =''
PORT =8000

reply = 'Yes'

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))

s.listen(3)

conn,addr = s.accept()

request = conn.recv(1024)

print('request is:',request)
print('connected by:',conn)

conn.send(reply.encode())

conn.close()
