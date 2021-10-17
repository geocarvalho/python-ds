import requests

payload = {"genome": "hg38", "track": "ncbiRefSeq", "maxItemsOutput": 5}
api_url = "https://api.genome.ucsc.edu/getData/track"
r = requests.get(api_url, params=payload)
print(r.url)