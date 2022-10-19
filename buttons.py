from telebot import types

button = types.InlineKeyboardMarkup(row_width= 2)

en_ru = types.InlineKeyboardButton(text= "🇺🇸/🇷🇺", callback_data= 'en__ru' )
ru_en = types.InlineKeyboardButton(text= "🇷🇺/🇺🇸", callback_data= 'ru__en')
uz_ru = types.InlineKeyboardButton(text="🇺🇿/🇷🇺", callback_data= 'uz__ru')
ru_uz = types.InlineKeyboardButton(text="🇷🇺/🇺🇿", callback_data= 'ru__uz')


all_lang = types.InlineKeyboardButton(text = 'Определить язык 🌐', callback_data= 'determine_language')

button.add(en_ru,ru_en,uz_ru,ru_uz,)


