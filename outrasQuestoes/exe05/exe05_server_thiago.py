from jsonsocket import Client, Server
import requests
host = 'localhost'
port = '8003'


# Server code:
server = Server(host, int(port))
server.accept()
data = server.recv()
print(data)
# data now is: {'some_list': [123, 456]}
server.send({'Data': data}).close()
