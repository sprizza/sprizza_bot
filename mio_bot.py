#!usr/bin/python
# -*- coding: utf-8 -*-

#ciao ciao

import json
import webbrowser
import requests
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import time
import datetime
import string
import random
url = "https://api.telegram.org/bot444957336:AAFnuueZrO_xiTBQ02-zNgSqI7ylSVkR65Q/"
TOKEN = '444957336:AAFnuueZrO_xiTBQ02-zNgSqI7ylSVkR65Q'
bot = telepot.Bot(TOKEN)


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        name = msg["from"]["first_name"]
        txt = msg['text']
        bot.sendMessage(chat_id, 'ciao %s, non sono capace a fare tanto ancora!' % name)
        #bot.answerCallbackQuery(query_id, 'Pure a te %s' % txt)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='PASSWORD TOSTA', callback_data='password tosta'),
         InlineKeyboardButton(text='NIENTE', callback_data='niente')],
        [InlineKeyboardButton(text='NIENTE', callback_data='niente'),
         InlineKeyboardButton(text='NIENTE', callback_data='niente')],
        [InlineKeyboardButton(text='NIENTE', callback_data='niente'),
         InlineKeyboardButton(text='NIENTE', callback_data='niente')],
        [InlineKeyboardButton(text='NIENTE', callback_data='niente'),
         InlineKeyboardButton(text='NIENTE', callback_data='niente')],
        [InlineKeyboardButton(text='NIENTE', callback_data='niente'),
         InlineKeyboardButton(text='NIENTE', callback_data='niente')],
    ])
    bot.sendMessage(chat_id, 'Usa i tasti sotto %s se vuoi' % name, reply_markup=keyboard)


def on_callback_query(msg):
    query_id, chat_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, chat_id, query_data)
    if query_data == 'password tosta':
        characters = string.ascii_letters + string.punctuation + string.digits
        password = ""
        password_length = random.randint(26, 40)
        for x in range(password_length):
            char = random.choice(characters)
            password = password + char
        bot.sendMessage(chat_id, password)
        bot.answerCallbackQuery(query_id, password)
    

MessageLoop(bot, {'chat': on_chat_message, 'callback_query': on_callback_query}).run_as_thread()


while True:
    time.sleep(10)

