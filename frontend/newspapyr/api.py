from requests import post
from newspapyr.config import config

class ApiWrapper:
    def __init__(self, path="/"):
        self.path = path

    def __getitem__(self, x):
        return ApiWrapper(self.path + x + "/")

    def __call__(self, **kwargs):
        return post(self.path, data=kwargs, cert=(config["ssl"]["crt"], config["ssl"]["key"])).json()
