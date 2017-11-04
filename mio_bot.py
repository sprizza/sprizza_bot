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
         InlineKeyboardButton(text='?', callback_data='?')],
        [InlineKeyboardButton(text='APRO PAGINA MUSICA YUTUBE', callback_data='apro pagina musica yutube'),
         InlineKeyboardButton(text='NIENTE', callback_data='niente')],
        [InlineKeyboardButton(text='!', callback_data='!'),
         InlineKeyboardButton(text='!', callback_data='!')],
        [InlineKeyboardButton(text='!', callback_data='!'),
         InlineKeyboardButton(text='!', callback_data='!')],
        [InlineKeyboardButton(text='!', callback_data='!'),
         InlineKeyboardButton(text='!', callback_data='!')],
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
    elif query_data == '?':
        info = 'son bravooo'
        bot.sendMessage(chat_id, info)
        bot.answerCallbackQuery(query_id, 'Ciao')
    elif query_data == 'apro pagina musica yutube':
        webbrowser.open('https://www.youtube.com/results?search_query=musica')
    elif query_data == 'niente':
        a = 'booo....'
        bot.sendMessage(chat_id, a)
        bot.answerCallbackQuery(query_id, 'Chissà')

MessageLoop(bot, {'chat': on_chat_message, 'callback_query': on_callback_query}).run_as_thread()


while True:
    time.sleep(10)

