import requests, time

# request_get = requests.get('http://requestbin.fullcontact.com/1i3k7bp1', data={"ts": time.time()})
# print(request_get.status_code)
# print(request_get.content)

request_post = requests.post('http://requestbin.fullcontact.com/1i3k7bp1', data={"ts": time.time()})
print(request_post.status_code)
print(request_post.content)
