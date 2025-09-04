import requests

api_url = "https://zelda.fanapis.com/api/characters?limit=100&page=5"

request = requests.get(api_url)

data = request.json()

nomes = [char['name'] for char in data['data']]

for nome in nomes:
  print(nome)

