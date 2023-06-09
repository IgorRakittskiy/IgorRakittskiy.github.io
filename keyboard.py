from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

web_app = WebAppInfo(url="https://igorrakittskiy.github.io/")

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Site", web_app=web_app)]
    ],
    resize_keyboard=True
)

cb = CallbackData('btn', 'action')
key = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton('Pay', callback_data='btn:buy')]]
)