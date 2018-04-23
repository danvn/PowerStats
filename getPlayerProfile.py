import http.client
import json
import requests

url = 'https://api.sportradar.us//nba/trial/v4/en/players/0afbe608-940a-4d5d-a1f7-468718c67d91/profile.json?api_key=ujyv72ke4uas2mdvwq6h7tjp'
response = requests.get(url)
data = json.loads(response.content.decode('utf-8'))

with open('LeBronJamesProfile.json', 'w') as f:
    json.dump(data, f)
