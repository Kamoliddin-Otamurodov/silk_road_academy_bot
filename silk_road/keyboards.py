from telegram import KeyboardButton, ReplyKeyboardMarkup , InlineKeyboardMarkup , InlineKeyboardButton


WELCOME_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kurslar"),
        ]
    ]
    ,
    resize_keyboard=True,
)


COURSE_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇬🇧 English"),
            KeyboardButton(text="🇯🇵 Yapon tili"),
            KeyboardButton(text="🇰🇷 Koreys tili"),
        ],
        [
            KeyboardButton(text="⬅️ Qaytish"),
        ]
    ]
    ,
    resize_keyboard=True,
)

KOREAN_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇰🇷 Kurs haqida"),
            KeyboardButton(text="🇰🇷 Kursga yoziltirish"),
        ],
        [
            KeyboardButton(text="⬅️Qaytish"),
        ]
    ]
    ,
    resize_keyboard=True,
)

JAPANESE_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇯🇵 Kurs haqida"),
            KeyboardButton(text="🇯🇵 Kursga yoziltirish"),
        ],
        [
            KeyboardButton(text="⬅️Qaytish"),
        ]
    ]
    ,
    resize_keyboard=True,
)

ENGLISH_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇬🇧 Kurs haqida"),
            KeyboardButton(text="🇬🇧 Kursga yoziltirish"),
        ],
        [
            KeyboardButton(text="⬅️Qaytish"),
        ]
    ]
    ,
    resize_keyboard=True,
)

CLEAR_USERS_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="♻️Tozalash"),
        ],
        [
            KeyboardButton(text="⬅️ Qaytish"),
        ]
    ]
    ,
    resize_keyboard=True,
)
