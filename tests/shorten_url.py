import requests

# url of the api
url = 'http://127.0.0.1:5000/api/shorten'

# insert your url in the 'url' value
payload = {
    'url': 'https://www.youtube.com/'
}

# request to the api
r = requests.post(url, data=payload)

# response will be formatted in json 
print(r.json())
