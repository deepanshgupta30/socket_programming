import socket
#importing socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#what is my receiver address
recv_addr=('127.0.0.1',9999)
#now i want a msg
user_data=input('enter your message:-')
#converting data into ascii code
newdata=user_data.encode('ascii')
#now you can send data
s.sendto(newdata, recv_addr)
#        data,receiver's address
print('your msg has been sent..')
