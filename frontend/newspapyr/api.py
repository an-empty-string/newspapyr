from requests import post
from newspapyr import app
from newspapyr.config import config

class ApiWrapper:
    def __init__(self, path="https://service1.newspapyr.co/"):
        self.path = path

    def __getattr__(self, x):
        return ApiWrapper(self.path + x + "/")

    def __call__(self, **kwargs):
        return post(self.path, data=kwargs, cert=(config["ssl"]["crt"], config["ssl"]["key"]), verify=config["ssl"]["ca"]).json()

@app.context_processor
def inject():
    return dict(api=ApiWrapper())
