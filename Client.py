import socket
serverName = 'localhost'   
serverPort = 1200 

socketi = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socketi.connect((serverName,serverPort))
