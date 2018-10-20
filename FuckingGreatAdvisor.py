import requests

class FuckingGreatAdvice:
    def __init__(self):
        self.api_url = "http://fucking-great-advice.ru/api/random"

    def get_advise(self):
        resp = requests.get(self.api_url)
        result_json = resp.json()
        # print("[resonse for get updates]: ", result_json)
        return result_json['text']
