import requests


# url of the api
url = 'http://127.0.0.1:5000/api/stats/'

# id of the url
url_id = 'mOLv'

url = url + url_id

# request to the api
r = requests.get(url)

# gets the response in a json format
print(r.json())


