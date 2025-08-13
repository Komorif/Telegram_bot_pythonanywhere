from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# English
# Клавиатура номер 1 (English_main_menu)
en_mainMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Our games 🎮", callback_data="en_in_our_games"),
            InlineKeyboardButton(text="Social Media 🌍", callback_data="en_in_social_network")
        ],
        [
            InlineKeyboardButton(text="Profile 🧒", callback_data="en_in_Profile"),
            InlineKeyboardButton(text="FAQ❓", callback_data="en_in_FAQ")
        ],
        [
            InlineKeyboardButton(text="Reviews ✏", callback_data="en_in_reviews"),
            InlineKeyboardButton(text="Support 💰", callback_data="en_in_donation")
        ],
        [
            InlineKeyboardButton(text="Back", callback_data="en_back_mainMenu")
        ]
    ]
)


# Клавиатура номер 2 (Наши игры)
en_in_our_games = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="IOS 🍏", callback_data="en_in_ios"),
            InlineKeyboardButton(text="ANDROID 🤖", callback_data="en_in_android")
        ],
        [
            InlineKeyboardButton(text="PC 🖥️", callback_data="en_in_pc"),
            InlineKeyboardButton(text="WEB GAMES 🎮", callback_data="en_in_web_games")
        ],
        [
            InlineKeyboardButton(text="Back", callback_data="en_back_games")
        ]
    ]
)


# Клавиатура номер 3 (IOS)
en_in_ios = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Back", callback_data="en_back_ios")
        ]
    ]
)


# Клавиатура номер 4 (Android)
en_in_android = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="GOOGLE PLAY 👾", callback_data="en_in_google_play"),
            InlineKeyboardButton(text="Cars 🚗", callback_data="en_in_cars_two")
        ],
        [
            InlineKeyboardButton(text="Mosaic 🧠", callback_data="en_in_mosaic")
        ],
        [
            InlineKeyboardButton(text="Back", callback_data="en_back_android")
        ]
    ]
)

# Клавиатура номер 5 (PC)
en_in_pc = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="ES MOD 🧚‍♂️", callback_data="en_in_mod_bl"),
            InlineKeyboardButton(text="Calculator C#", callback_data="en_in_pc_calculator")
        ],
        [
            InlineKeyboardButton(text="Back", callback_data="en_back_pc")
        ]
    ]
)

# Клавиатура номер 6 (Web Games)
en_in_web_games = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="PC 🖥️", callback_data="en_in_pc_web_games"),
            InlineKeyboardButton(text="PHONE 📱", callback_data="en_in_phone_web_games")
        ],
        [
            InlineKeyboardButton(text="Back", callback_data="en_back_in_web_games")
        ]
    ]
)


# Клавиатура номер 7 (PC Web Games)
en_in_pc_web_games = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Back", callback_data="en_back_in_pc_web_games")
        ]
    ]
)

# Клавиатура номер 8 (Phone Web Games)
en_in_phone_web_games = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Back", callback_data="en_back_in_phone_web_games")
        ]
    ]
)

# Клавиатура номер 9 (Google Play)
en_in_google_play = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Back", callback_data="en_back_in_google_play")
        ]
    ]
)

# Клавиатура номер 10 (Социальные сети)
en_in_social_network = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="YOUTUBE 1 📺", url="https://www.youtube.com/channel/UC9EJAIYe4sL0iGB_huHTqHw", callback_data="en_in_youtube_one"),
            InlineKeyboardButton(text="YOUTUBE 2 📺", url="https://www.youtube.com/channel/UCb2GlPOgqB_VpWTvQM_dzKg", callback_data="en_in_youtube_two")
        ],
        [
            InlineKeyboardButton(text="TWITCH 🔴", url="https://www.twitch.tv/komorifn", callback_data="en_in_twitch"),
            InlineKeyboardButton(text="DISCORD 🗣️", url="https://discord.gg/2pbCpNcDZm", callback_data="en_in_discord")
        ],
        [
            InlineKeyboardButton(text="GITHUB 💣", url="https://github.com/Komorif", callback_data="en_in_github"),
            InlineKeyboardButton(text="VK ✔️", url="https://vk.com/komorilfg", callback_data="en_in_vk")
        ],
        [
            InlineKeyboardButton(text="Back", callback_data="en_back_social")
        ]
    ]
)


# Клавиатура номер 11 (FAQ)
en_in_FAQ = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Back", callback_data="en_back_faq")
        ]
    ]
)

# Клавиатура номер 12 (Профиль)
en_in_Profile = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Back", callback_data="en_back_prof")
        ]
    ]
)

# Клавиатура номер 13 (Пожертвования)
en_in_donation = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Donation 💰", url="https://www.donationalerts.com/r/fetchy74")
        ],
        [
            InlineKeyboardButton(text="Back", callback_data="en_back_donat")
        ]
    ]
)

# Клавиатура номер 14 (Отзывы)
en_in_reviews = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Back", callback_data="en_back_in_reviews")
        ]
    ]
)



# PC
# Клавиатура номер 1.1 (Мод БЛ)
en_in_mod_bl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Download mod for the game ES 🧚‍♂️", url="https://disk.yandex.ru/d/XmU8R4pGdsiuIA")
        ],
        [
            InlineKeyboardButton(text="Back", callback_data="en_back_mod")
        ]
    ]
)

# Клавиатура 1.2 (Карточка Калькулятор)
en_in_pc_calculator = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Download", url="https://disk.yandex.ru/d/rDZ7E98l2uj8YA")
        ],
        [
            InlineKeyboardButton(text="Back", callback_data="en_back_in_pc_calculator")
        ]
    ]
)

# Android
# Клавиатура номер 1.1 (Машины)
en_in_cars_two = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Download", url="https://disk.yandex.ru/d/rDZ7E98l2uj8YA")
        ],
        [
            InlineKeyboardButton(text="Back", callback_data="en_back_in_cars_two")
        ]
    ]
)

# Клавиатура номер 1.2 (Мозаика)
en_in_mosaic = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Download", url="https://disk.yandex.ru/d/G2b7dN2O8vFd7g")
        ],
        [
            InlineKeyboardButton(text="Back", callback_data="en_back_in_mosaic")
        ]
    ]
)