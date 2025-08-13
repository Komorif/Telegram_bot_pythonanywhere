from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Клавиатура номер 1 (выбором языка)
mainMenu_en_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="English 🇺🇸", callback_data="lang_en"),
            InlineKeyboardButton(text="Russian 🇷🇺", callback_data="lang_rus")
        ]
    ]
)


# Клавиатура номер 1.2 (выбором языка)
mainMenu_en_rus_two = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="English 🇺🇸", callback_data="lang_en_two")
        ],
        [
            InlineKeyboardButton(text="Russian 🇷🇺", callback_data="lang_rus_two")
        ]
    ]
)