from telebot import types

button = types.InlineKeyboardMarkup(row_width= 2)

en_ru = types.InlineKeyboardButton(text= "๐บ๐ธ/๐ท๐บ", callback_data= 'en__ru' )
ru_en = types.InlineKeyboardButton(text= "๐ท๐บ/๐บ๐ธ", callback_data= 'ru__en')
uz_ru = types.InlineKeyboardButton(text="๐บ๐ฟ/๐ท๐บ", callback_data= 'uz__ru')
ru_uz = types.InlineKeyboardButton(text="๐ท๐บ/๐บ๐ฟ", callback_data= 'ru__uz')


all_lang = types.InlineKeyboardButton(text = 'ะะฟัะตะดะตะปะธัั ัะทัะบ ๐', callback_data= 'determine_language')

button.add(en_ru,ru_en,uz_ru,ru_uz,)


