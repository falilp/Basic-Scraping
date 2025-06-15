import requests

print('version request: ' + requests.__version__)

#url https://sunrise-sunset.org/api

latitud = -4
longitud = 4.2222
fecha = '2025-06-09' # AAAA-MM-DD

response = requests.get(f'https://api.sunrise-sunset.org/json?lat={latitud}&lng={longitud}&date={fecha}')

print("Cual ha sido el resultado: " + response.json()['status'])
print("A que hora salio el sol? " + response.json()['results']['sunrise'])