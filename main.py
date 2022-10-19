# Code by myth-dev or h4ckerworld 
#! /usr/bin/python3


from deep_translator import GoogleTranslator
from telebot import *

from buttons import *

TOKEN = '# add your token'

bot = telebot.TeleBot(TOKEN)

ENGLISH = 'en'
RUSSIAN = 'ru'
UZBEK  = 'uz'
UKRAINIAN = 'uk'
FRENCH = 'fr'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Выберите язык которое хотите переводить.', reply_markup = button)

# 
    
@bot.callback_query_handler(func = lambda call: True)

def translator(call):
    if call.data == 'en__ru':
        bot.send_message(call.message.chat.id, 'Send the text that you want to translate!')
        @bot.message_handler()
        def translate_en_ru(message):
            bot.reply_to(message, GoogleTranslator(source=ENGLISH, target=RUSSIAN).translate(message.text))

    elif call.data == 'ru__en':
        bot.send_message(call.message.chat.id, 'Отправьте текст которое хотите переводит!')
        @bot.message_handler()
        def translate_ru_en(message):
            bot.reply_to(message, GoogleTranslator(source=RUSSIAN, target=ENGLISH).translate(message.text))

    elif call.data == 'uz__ru':
        bot.send_message(call.message.chat.id, "Tarjima qilmoqchi bo'lgan matnni yuboring!")
        @bot.message_handler()
        def translate_uz_ru(message):
            bot.reply_to(message, GoogleTranslator(source=UZBEK, target=RUSSIAN).translate(message.text))     

    elif call.data == 'ru__uz':
        bot.send_message(call.message.chat.id, "Отправьте текст которое хотите переводит!")
        @bot.message_handler()
        def translate_ru_uz(message):
            bot.reply_to(message, GoogleTranslator(source=RUSSIAN, target=UZBEK).translate(message.text))            
              
bot.infinity_polling()
