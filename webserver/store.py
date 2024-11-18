import requests

def get_categories():
    r=requests.get('https://dragonball-api.com/api/characters')
    print(r.status_code)
    data = r.json()
    characters = data.get('items', [])  
    for character in characters: 
        name = character.get('name', 'N/A') 
        ki = character.get('ki', 'N/A')
        race = character.get('race', 'N/A')
        print(f"{name} - {ki} - {race}")