from jsonsocket import Client, Server
import requests
import json

host = '127.0.0.1'
port = '8005'


# Client code:
client = Client()
respostaC = requests.get('https://www.metaweather.com/api/location/search/?query=london')
r = respostaC.json()
cidade = r[0]['woeid']
c = str(cidade)
consulta = requests.get('https://www.metaweather.com/api/location/'+c)
r = consulta.json()
client.connect(host, int(port)).send(r['consolidated_weather'])

response = client.recv()
print(response)
# response now is {'data': {'some_list': [123, 456]}}
client.close()
