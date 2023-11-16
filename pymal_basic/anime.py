import requests

class Anime:
    def __init__(self, client_id):
        self.token = client_id
        self.headers = {'X-MAL-CLIENT-ID': f'{self.token}'}
        
    def SearchAnime(self, search: str, limit: int = 4):
        url = 'https://api.myanimelist.net/v2/anime'
        params = {'q': f'{search}', 'limit': f'{limit}'}
        response = requests.get(url, params=params, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return f'Error: {response.status_code}, {response.text}'
        
    def GetAnime(self, result):
        data_json = result
        
        data_anime = []
        for entry in data_json.get('data', []):
            node = entry.get('node', {})
            title = node.get('title', '')
            anime_id = node.get('id', '')
            
            data_anime.append({'title': title, 'id': anime_id})
        
        return data_anime