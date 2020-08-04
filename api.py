import requests

url = "https://instagram-facebook-media-downloader.p.rapidapi.com/api"

querystring = {"igurl":"https%3A%2F%2Fwww.instagram.com%2Fp%2FBvJyyOhoYvJ"}

headers = {
    'x-rapidapi-host': "instagram-facebook-media-downloader.p.rapidapi.com",
    'x-rapidapi-key': "ce8ea61463mshba51cb620b94a68p161c06jsnc8d90c1f2bb2"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)