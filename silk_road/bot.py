from dotenv import load_dotenv
import os

from telegram.ext import (
    Updater, 
    Dispatcher,
    CommandHandler,
    MessageHandler,
    Filters,
)

from .handlers import start  ,users, clear_users , get_contact  , handle_contact,  course , english , japanese , korean , english_info , english_write , japanase_write , japanese_info , korean_write , korean_info

# getting the token from .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")


updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

def register_handlers():
    dispatcher.add_handler(handler=CommandHandler("start", start))
    dispatcher.add_handler(handler=CommandHandler("users", users))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.contact, callback=handle_contact))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("Kurslar"), callback=course))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("⬅️ Qaytish"), callback=start))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("🇬🇧 English"), callback=english))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("🇯🇵 Yapon tili"), callback=japanese))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("🇰🇷 Koreys tili"), callback=korean))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("⬅️Qaytish"), callback=course))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("🇬🇧 Kurs haqida"), callback=english_info))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("🇬🇧 Kursga yoziltirish"), callback=get_contact))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("🇯🇵 Kurs haqida"), callback=japanese_info))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("🇯🇵 Kursga yoziltirish"), callback=get_contact))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("🇰🇷 Kurs haqida"), callback=korean_info))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("🇰🇷 Kursga yoziltirish"), callback=get_contact))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("♻️Tozalash"), callback=clear_users))

    updater.start_polling()
    updater.idle()