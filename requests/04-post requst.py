import requests


# r = requests.get('https://api.github.com/events', auth=('user', 'pass'))
r = requests.post('https://httpbin.org/post', data={'key': 'value'})


print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.content)
w=r.encoding = 'ISO-8859-1'
print(w)
print(r.json())
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(r.text)