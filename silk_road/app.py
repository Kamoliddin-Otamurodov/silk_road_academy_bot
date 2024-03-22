from dotenv import load_dotenv
import os
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler , MessageHandler , Filters
import handlers
from flask import Flask , request
import requests


load_dotenv()
TOKEN = os.environ.get('TOKEN')
URL = os.environ.get('URL')

bot = Bot(TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)
app = Flask(__name__)


@app.route('/silkroad', methods=['GET', 'POST'])
def random_dog():
    if request.method == 'GET':
        return '<h1>Silk road is working...!</h1>'

    if request.method == 'POST':
        body = request.get_json()
        
        updater = Update.de_json(body, bot)

        dispatcher.add_handler(handler=CommandHandler("start", handlers.start))
        dispatcher.add_handler(handler=CommandHandler("users", handlers.users))
        dispatcher.add_handler(handler=MessageHandler(Filters.contact, handlers.handle_contact))
        dispatcher.add_handler(handler=MessageHandler(Filters.text("Kurslar"), handlers.course))
        dispatcher.add_handler(handler=MessageHandler(Filters.text("⬅️ Qaytish"), handlers.start))
        dispatcher.add_handler(handler=MessageHandler(Filters.text("🇬🇧 English"), handlers.english))
        dispatcher.add_handler(handler=MessageHandler(Filters.text("🇯🇵 Yapon tili"), handlers.japanese))
        dispatcher.add_handler(handler=MessageHandler(Filters.text("🇰🇷 Koreys tili"), handlers.korean))
        dispatcher.add_handler(handler=MessageHandler(Filters.text("⬅️Qaytish"), handlers.course))
        dispatcher.add_handler(handler=MessageHandler(Filters.text("🇬🇧 Kurs haqida"), handlers.english_info))
        dispatcher.add_handler(handler=MessageHandler(Filters.text("🇬🇧 Kursga yoziltirish"), handlers.get_contact))
        dispatcher.add_handler(handler=MessageHandler(Filters.text("🇯🇵 Kurs haqida"), handlers.japanese_info))
        dispatcher.add_handler(handler=MessageHandler(Filters.text("🇯🇵 Kursga yoziltirish"), handlers.get_contact))
        dispatcher.add_handler(handler=MessageHandler(Filters.text("🇰🇷 Kurs haqida"), handlers.korean_info))
        dispatcher.add_handler(handler=MessageHandler(Filters.text("🇰🇷 Kursga yoziltirish"), handlers.get_contact))
        dispatcher.add_handler(handler=MessageHandler(Filters.text("♻️Tozalash"), handlers.clear_users))

        updater.start_polling()
        updater.idle()

        return {'message': 'ok'}


if __name__ == '__main__':
    app.run(debug=True)