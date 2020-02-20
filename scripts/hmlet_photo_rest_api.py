import requests
import json
import os

ENDPOINT = "http://127.0.0.1:8000/api/photo/"
image_path = os.path.join(os.getcwd(),"300.png")


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