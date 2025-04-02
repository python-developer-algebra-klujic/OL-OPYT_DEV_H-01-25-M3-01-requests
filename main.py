import json
import requests


URL = 'https://jsonplaceholder.typicode.com/users'

try:
    response = requests.get(URL)
    if response.status_code == 200:
        users = json.loads(response.text)
        # users je lista
        # users[5] je rjecnik u listi users na indeksu 5
        # users[5]['name'] je vrijednost pod kljucem 'name' u rjecniku users[5]
        print(users[5]['name'])
    else:
        print(response.status_code)
except Exception as ex:
    print(f'Dogodila se greska {ex}')
