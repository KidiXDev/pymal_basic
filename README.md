# pymal_basic
Python Basic API wrapper for [MyAnimeList](https://myanimelist.net/)
> **WORK ON PROGRESS**

## Installation
```shell
pip install pymal_basics
```

## Usage
Basic Usage:
```python
from pymal_basic import Anime

obj = Anime('YOUR CLIENT ID')

ress = obj.SearchAnime('naruto', 4)
final_ress = obj.GetAnime(ress)

# You can process more data by processing the results
for anime in final_ress:
    print(f"Title: {anime['title']}, ID: {anime['id']}")
```