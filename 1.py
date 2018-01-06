from telegram.ext import Updater
import logging
import random
import requests
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

updater = Updater(token='452156710:AAGKA4Oyi-O1QUknFpVanjMUubS5LfClao0')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Тест на пидора. Используй синтаксис /test name")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
a = ['пидор', 'не пидор']


def say(bot, update, args):
    response1 = requests.get('http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/294021?apikey=AGTPiYmUHl8Pe1FycGCHkmuDiMkuJlcV&metric=true').json()

    response3 = requests.get('https://api.darksky.net/forecast/94f3ca138b7325aa81c79772b8f1d1de/55.71176759,37.78098164?exclude=currently&units=si').json()

    i = 0
    all = ''
    while (i < 9):

        all = all + '\n' + str((response1[i]['DateTime'])[11:13]) + '  ' + str(response1[i]['IconPhrase']) + ' ' + str(
            response1[i]['Temperature']['Value'])+'   '+str(response3["hourly"]['data'][i]['temperature'])+' '+str(response3["hourly"]['data'][i]['icon'])
        i = i + 1
    bot.send_message(chat_id=update.message.chat_id, text=all)


say_handler = CommandHandler('test', say, pass_args=True)
dispatcher.add_handler(say_handler)


def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)


caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)
updater.start_polling()
