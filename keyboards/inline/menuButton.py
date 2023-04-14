from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text="💌 Tabrik olish", callback_data="home")
button.add(btn1)

def generateImagesButtons(lst: list):
    btn_img = InlineKeyboardMarkup()
    for i in lst:
        btn = InlineKeyboardButton(text=i, callback_data=f"⭕{i}")
        btn_img.insert(btn)
    btn_img.add(InlineKeyboardButton(text="🔙Orqaga", callback_data='back'))
    return btn_img
