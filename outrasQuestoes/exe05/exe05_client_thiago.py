from jsonsocket import Client, Server
import requests
import json

host = '127.0.0.1'
port = '8003'


# Client code:
client = Client()
resposta = requests.get('https://swapi.co/api/films/1/')
r = resposta.json()
client.connect(host, int(port)).send(r['title'])
response = client.recv()
print(response)
# response now is {'data': {'some_list': [123, 456]}}
client.close()
