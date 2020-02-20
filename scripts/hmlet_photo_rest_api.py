import requests
import json
import os

ENDPOINT = "http://127.0.0.1:8000/api/photo/"
AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + 'refresh'
image_path = os.path.join(os.getcwd(),"300.png")


login_data = {
    'username': 'archit',
    'password': '!23456789'
}

r = requests.post(AUTH_ENDPOINT, data=login_data)
token = r.json()#['token']
print(token)

'''
refresh_header = {
    'content-type': 'application/json'
}
refresh_payload = {
    'token': token
}
ref_token = requests.post(REFRESH_ENDPOINT, data=refresh_payload, headers=refresh_header)
resp = ref_token.json()
print(resp)
'''
post_data = json.dumps({"content": "test"})
post_headers = {
    'content-type': 'application/json',
    'Authorization': 'JWT ' + token
}
post = requests.post(ENDPOINT, data=post_data, headers=post_headers) #will fail
print(post.text)

'''
r = requests.get(ENDPOINT)
print(r.status_code) #should be okay

r2=requests.get(ENDPOINT+ str(10))
print(r2.text)

post_data = json.dumps({"content": "test"})
post_headers = {
    'content-type': 'application/json'
}
post = requests.post(ENDPOINT, data=post_data, headers=post_headers) #will fail
print(post.text)
'''

'''
def do_img(method = 'get', data={}, is_json=True, img_path=None):

    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
    if img_path is not None:
        with open(image_path, 'rb') as image:
            file_data = {
                'image': image
            }
            r = requests.request(method, ENDPOINT, data=data, files=file_data, headers=headers)
    else:
        r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r


#do_img(method="post", data={'user': 1, 'content': ''}, is_json=False, img_path=image_path)
do_img(method="put", data={'id':10,'user': 1, 'content': ''}, is_json=False, img_path=image_path)
'''
'''
def do(method = 'get', data={}, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r


#get
do(data={'id': 3})
#post
do(method='post', data={"content": "test content", "user": 1})
#put/patch
do(method='put', data={'id': 6, "content": "test content", "user": 1})
#delete
do(method='delete', data={'id': 3})
#do(data={'id': 300000})
'''