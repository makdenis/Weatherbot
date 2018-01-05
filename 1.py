import requests
import datetime
from telegram.ext import Updater
import logging
import re

import datetime
import random
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

updater = Updater(token='452156710:AAGKA4Oyi-O1QUknFpVanjMUubS5LfClao0')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(bot, update):
    response1 = requests.get(
        'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/294021?apikey=AGTPiYmUHl8Pe1FycGCHkmuDiMkuJlcV&metric=true').json()
    # response = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22moscow%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys').json()
    # response = requests.get('https://api.darksky.net/forecast/94f3ca138b7325aa81c79772b8f1d1de/55.71176759,37.78098164?exclude=currently&units=si').json()
    # print(response1)
    i = 0
    all = ''
    while (i < 10):
        #     print(response["hourly"]['data'][i]["temperature"])
        #     print(datetime.datetime.fromtimestamp(int(response["hourly"]['data'][i]["time"])).strftime('%Y-%m-%d %H:%M:%S'))
        all = all + '\n' + str((response1[i]['DateTime'])[11:13]) + ' ' + str(response1[i]['IconPhrase']) + ' ' + str(
            response1[i]['Temperature']['Value'])
        i = i + 1
    bot.send_message(chat_id=update.message.chat_id, text=all)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)





