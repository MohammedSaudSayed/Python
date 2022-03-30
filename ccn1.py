import socket
s=socket.socket()
print('Socket Created')
s.bind(('localhost',9999))
s.listen(3)#This makes it TCP
print('Waiting for connections....')
while True:
 c, addr = s.accept()
 name = c.recv(1024).decode()
 print('Connected with Client',addr,name)
 c.send(bytes('Welcome to CPM','utf-8'))
 c.close()

c=socket.socket() 
c.connect(('localhost',9999))
name=input("Enter your name: ") 
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())