import requests
import json
from constant import Constants, TestData

class UserApi:
    def __init__(self):
        self.headers = Constants.header
    def post(self, path, data):
        response = requests.post(url=path, headers=self.headers, data=json.dumps(data))
        return response
    def get(self, path, auth=None):
        if auth is None:
            response = requests.get(url=path, headers=self.headers)
        else:
            headers = {"accept": "application/json", "Content-Type": "application/json", "Authorization": auth}
            response = requests.get(url=path, headers=headers)
        return response
    def delete(self, path, auth=None):
        response = requests.delete(url=path, headers={"Authorization": auth})
    def patch(self, path, data, auth=None):
        response = requests.patch(url=path, headers={"Authorization": auth}, data=json.dumps(data))
        return response