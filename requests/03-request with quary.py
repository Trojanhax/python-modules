import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.url)
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(r.text)