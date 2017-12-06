import requests
import json

def geocode(address):
    parameters = {'address': address, 'sensor':'false'}
    base = 'http://maps.google.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters )
    resposta = response.json()
    print(resposta['results'][0]['geometry']['location'])

if __name__=='__main__':
    #Código somente será executado, se o programa estiver em execução como SCRIPT
    geocode('Av. Senador Salgado Filho, 1559, Natal, RN')
