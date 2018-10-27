
from libs import usuario, dados, game, historia
import telebot


bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start', 'help'])
def start(m):
    cid = m.chat.id
    m_text = "Hola, esto es una prueba"
    bot.send_message(cid, m_text)

    