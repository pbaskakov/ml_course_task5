import requests


data = open('text.txt').read().strip('\n')
r = requests.post('http://127.0.0.1:8000/', data=data)
print(r.text)
