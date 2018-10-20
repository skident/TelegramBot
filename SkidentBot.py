import requests
import datetime
from time import sleep

# url = "https://api.telegram.org/bot728208585:AAGL1Bx8UX_8s1_II8cF9DUlVT30r_X2WQI/"

class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
        print( self.api_url )

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        # print("[resonse for get updates]: ", result_json)
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        result_len = len(get_result)
        if result_len > 0:
            last_update = get_result[-1]
        else:
            last_update = '' #'"#get_result[len(get_result)]

        return last_update

class FuckingGreatAdvice:
    def __init__(self):
        self.api_url = "http://fucking-great-advice.ru/api/random"

    def get_advise(self):
        resp = requests.get(self.api_url)
        result_json = resp.json()
        # print("[resonse for get updates]: ", result_json)
        return result_json['text']


token = '728208585:AAGL1Bx8UX_8s1_II8cF9DUlVT30r_X2WQI'
greet_bot = BotHandler(token)
greetings = ('hello', 'hi', 'greetings', 'sup')
get_advice = ('/advice', '/advice@skidentbot')
now = datetime.datetime.now()


def main():
    new_offset = None
    today = now.day
    hour = now.hour

    fucking_advicer = FuckingGreatAdvice()


    while True:
        try:
            greet_bot.get_updates(new_offset)

            last_update = greet_bot.get_last_update()
            # print (last_update)

            print ("Last update:", last_update['message'])

            # if 'text' not in last_update['message']:
            #     print ("text not found")
            #     continue

            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            last_chat_id = last_update['message']['chat']['id']
            # last_chat_name = last_update['message']['chat']['first_name']

            print('chat text:', last_chat_text)

            if last_chat_text.lower() in get_advice:
                advice_text = fucking_advicer.get_advise()
                greet_bot.send_message(last_chat_id, advice_text)

            # print (advice_text)

            # if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            #     greet_bot.send_message(last_chat_id, 'Good Morning  {}'.format(last_chat_name))
            #     # today += 1
            #
            # elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            #     greet_bot.send_message(last_chat_id, 'Good Afternoon {}'.format(last_chat_name))
            #     # today += 1
            #
            # elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            #     greet_bot.send_message(last_chat_id, 'Good Evening  {}'.format(last_chat_name))
            #     # today += 1
            #
            # else:
            #     greet_bot.send_message(last_chat_id, 'Unknown command {}'.format(last_chat_name))
            #     # today += 1

            new_offset = last_update_id + 1
        except:
            sleep(1)
        #     new_offset = 0
            # print ("continue")
            # continue

if __name__ == '__main__':
    try:
        main()
        # fucking_advicer = FuckingGreatAdvice()
        # advice_text = fucking_advicer.get_advise()
        # print (advice_text)

    except KeyboardInterrupt:
        exit()