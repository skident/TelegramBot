import requests
import datetime
from time import sleep
from FuckingGreatAdvisor import FuckingGreatAdvice
from EnglishWords import WordList

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


def main():
    token = '{}'
    greet_bot = BotHandler(token)

    greetings = ('hello', 'hi', 'greetings', 'sup')
    get_advice = ('/advice', '/advice@skidentbot')
    get_eng_word = ('/word', '/word@skidentbot')

    now = datetime.datetime.now()


    new_offset = None
    today = now.day
    hour = now.hour


    fucking_advicer = FuckingGreatAdvice()
    word_list = WordList()


    while True:
        try:
            greet_bot.get_updates(new_offset)

            last_update = greet_bot.get_last_update()
            # print (last_update)

            print ("Last update:", last_update['message'])

            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            last_chat_id = last_update['message']['chat']['id']
            # last_chat_name = last_update['message']['chat']['first_name']

            print('chat text:', last_chat_text)

            if last_chat_text.lower() in get_advice:
                advice_text = fucking_advicer.get_advise()
                greet_bot.send_message(last_chat_id, advice_text)

            elif last_chat_text.lower() in get_eng_word:
                word = word_list.get_random()
                greet_bot.send_message(last_chat_id, word)

            new_offset = last_update_id + 1

        except:
            print ("exception caught")
            sleep(1)


if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        exit()