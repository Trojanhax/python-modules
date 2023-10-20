import requests

http_proxy = "http://154.58.202.47:1337"
proxies = {
    "http": http_proxy,
}

r = requests.get('https://httpbin.org/get', proxies=proxies)
print(r.text)
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
