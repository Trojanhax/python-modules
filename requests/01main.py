import requests

r = requests.get('https://github.com/')
print(r.text)
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(r.text)

