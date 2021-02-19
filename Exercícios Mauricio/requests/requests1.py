import requests

r = requests.get('https://github.com/timeline.json', stream=True)

print(r.headers)
