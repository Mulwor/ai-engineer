import telebot
import sqlite3
from config import TOKEN
from property import *

bot = telebot.TeleBot(TOKEN)
name = 'None'

@bot.message_handler(commands=['start'])
def start(message):
  # 1. Создания файла где будет хранится полностью вся база данных
  connection = sqlite3.connect('example.sql')
  # 2. C помощью данного метода сможем выполнять различные комманды
  cursor = connection.cursor()
  # 3. Создаем таблицу если его еще не существует с 3 полями:
  # id int auto_increment key - это айди
  # name, varchar(50) - это имя не больше 50 символов
  # pass varchar(50)) - пароль не больше 50 символов
  cursor.execute("CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name, varchar(50), pass varchar(50))")
  # 4. Создание самое таблицы и подключения к базе данных
  connection.commit()
  # Закрываем соединения и курсор с базой данных 
  cursor.close()
  connection.close()

  bot.send_message(
    message.chat.id, 
    "Hi please write your name for registration"
  )
  bot.register_next_step_handler(message, user_name)

def user_name(message):
  # Позволяет удалить различные пробелы до и после текста
  name = message.text.strip()
  bot.send_message(message.chat.id, "Write password")
  bot.register_next_step_handler(message, user_name)

def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)
    # bot.register_next_step_handler(message, user_pass)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n'
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)

bot.polling(none_stop=True)