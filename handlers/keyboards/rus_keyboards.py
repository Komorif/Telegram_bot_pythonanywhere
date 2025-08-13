from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Клавиатура номер 1 (Russian_main_menu)
rus_mainMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Наши игры 🎮", callback_data="rus_in_our_games"),
            InlineKeyboardButton(text="Социалки 🌍", callback_data="rus_in_social_network")
        ],
        [
            InlineKeyboardButton(text="Профиль 🧒", callback_data="rus_in_Profile"),
            InlineKeyboardButton(text="FAQ❓", callback_data="rus_in_FAQ")
        ],
        [
            InlineKeyboardButton(text="Отзывы ✏", callback_data="rus_in_reviews"),
            InlineKeyboardButton(text="Поддержка 💰", callback_data="rus_in_donation")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="rus_back_mainMenu")
        ]
    ]
)

# Клавиатура номер 2 (Наши игры)
rus_in_our_games = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="IOS 🍏", callback_data="rus_in_ios"),
            InlineKeyboardButton(text="ANDROID 🤖", callback_data="rus_in_android")
        ],
        [
            InlineKeyboardButton(text="PC 🖥️", callback_data="rus_in_pc"),
            InlineKeyboardButton(text="WEB GAMES 🎮", callback_data="rus_in_web_games")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="rus_back_games")
        ]
    ]
)

# Клавиатура номер 3 (ios)
rus_in_ios = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="rus_back_ios")
        ]
    ]
)

# Клавиатура номер 4 (android)
rus_in_android = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="GOOGLE PLAY 👾", callback_data="rus_in_google_play"),
            InlineKeyboardButton(text="Cars 🚗", callback_data="rus_in_cars_two")
        ],
        [
            InlineKeyboardButton(text="Mosaic 🧠", callback_data="rus_in_mosaic")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="rus_back_android")
        ]
    ]
)

# Клавиатура номер 5 (pc)
rus_in_pc = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="МОД БЛ 🧚‍♂️", callback_data="rus_in_mod_bl"),
            InlineKeyboardButton(text="Калькулятор C#", callback_data="rus_in_pc_calculator")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="rus_back_pc")
        ]
    ]
)

# Клавиатура номер 6 (web_games)
rus_in_web_games = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="ПК 🖥️", callback_data="rus_in_pc_web_games"),
            InlineKeyboardButton(text="ТЕЛЕФОН 📱", callback_data="rus_in_phone_web_games")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="rus_back_in_web_games")
        ]
    ]
)

# Клавиатура номер 7 (pc_web_games)
rus_in_pc_web_games = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="rus_back_in_pc_web_games")
        ]
    ]
)

# Клавиатура номер 8 (phone_web_games)
rus_in_phone_web_games = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="rus_back_in_phone_web_games")
        ]
    ]
)

# Клавиатура номер 9 (google_play)
rus_in_google_play = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Back", callback_data="rus_back_in_google_play")
        ]
    ]
)

# Клавиатура номер 10 (социальные сети)
rus_in_social_network = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="YOUTUBE 1 📺", url="https://www.youtube.com/channel/UC9EJAIYe4sL0iGB_huHTqHw"),
            InlineKeyboardButton(text="YOUTUBE 2 📺", url="https://www.youtube.com/channel/UCb2GlPOgqB_VpWTvQM_dzKg")
        ],
        [
            InlineKeyboardButton(text="TWITCH 🔴", url="https://www.twitch.tv/komorifn"),
            InlineKeyboardButton(text="DISCORD 🗣️", url="https://discord.gg/2pbCpNcDZm")
        ],
        [
            InlineKeyboardButton(text="GITHUB 💣", url="https://github.com/Komorif"),
            InlineKeyboardButton(text="VK ✔️", url="https://vk.com/komorilfg")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="rus_back_social")
        ]
    ]
)

# Клавиатура номер 11 (FAQ)
rus_in_FAQ = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="rus_back_faq")
        ]
    ]
)

# Клавиатура номер 12 (Профиль)
rus_in_Profile = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="rus_back_prof")
        ]
    ]
)

# Клавиатура номер 13 (Пожертвования)
rus_in_donation = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Пожертвование 💰", url="https://www.donationalerts.com/r/fetchy74")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="rus_back_donat")
        ]
    ]
)

# Клавиатура номер 14 (Отзывы)
rus_in_reviews = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="rus_back_in_reviews")
        ]
    ]
)

# PC — Мод БЛ
rus_in_mod_bl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Скачать мод для игры БЛ 🧚‍♂️", url="https://disk.yandex.ru/d/XmU8R4pGdsiuIA")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="rus_back_mod")
        ]
    ]
)

# PC — Калькулятор
rus_in_pc_calculator = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Скачать", url="https://disk.yandex.ru/d/rDZ7E98l2uj8YA")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="rus_back_in_pc_calculator")
        ]
    ]
)

# Android — Машины
rus_in_cars_two = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Скачать", url="https://disk.yandex.ru/d/rDZ7E98l2uj8YA")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="rus_back_in_cars_two")
        ]
    ]
)

# Android — Мозаика
rus_in_mosaic = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Скачать", url="https://disk.yandex.ru/d/G2b7dN2O8vFd7g")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="rus_back_in_mosaic")
        ]
    ]
)