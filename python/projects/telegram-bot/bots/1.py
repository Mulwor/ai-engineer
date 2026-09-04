import telebot
from telebot import types
from config import TOKEN
import webbrowser

bot = telebot.TeleBot(TOKEN)

# По нажатию на кнопку старт выводится сообщение Привет!
# можно также и добавить другие команды ['start', 'start2']
@bot.message_handler(commands=['start'])
def main(message):
  markup = types.ReplyKeyboardMarkup() 
  btn1 = types.KeyboardButton('Перейти на сайт')
  btn2 = types.KeyboardButton('Удалить')
  btn3 = types.KeyboardButton('Изменить текст')
  markup.row(btn1)
  markup.row(btn2, btn3)

  # Отправляем фото по нажатию на кнопку старт
  file = open('./assets/photo.webp', 'rb')
  bot.send_photo(message.chat.id, file, reply_markup=markup)

  # Отправляем аудио/видео по нажатию на кнопку стар
  # file = open('./audio.mp3', 'rb')
  # file = open('./video.mp4', 'rb')
  # bot.send_photo(message.chat.id, file, reply_markup=markup)

  bot.send_message(message, 'Какое красивое фото!', reply_markup=markup)
  bot.register_next_step_handler(message, on_click)

def on_click(message):
  if message.text == "Перейти на сайт":
    bot.send_message(message.chat.id, "Website is open")
  elif message.text == "Удалить фото":

@bot.message_handler(commands=['side', 'website'])
def site(message):
  webbrowser.open('https://itproger.com')

@bot.message_handler(commands=['formatText'])
def main(message):
  bot.send_message(
    message.chat.id, 
    # Можно форматировать текст
    '<b>Help</b> <em><u>information</em></u>', parse_mode='html'
  )

@bot.message_handler(commands=['showName'])
def main(message):
  bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}  {message.from_user.last_name}" )

# Обрабатываем любой текст который поступает от пользователя
@bot.message_handler()
def info(message):
  if message.text.lower() == 'привет':
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}  {message.from_user.last_name}" )
  elif message.text.lower() == 'id':
    # Ответ на пред.сообщение
    bot.reply_to(message, f'ID: {message.from_user.id} ')

# Когда пользователь отправляет файл нам в бот, мы можем взаимодействовать
# с этим файлом
@bot.message_handler(content_types=['photo']) 
def get_photo(message):
  # Создание кнопки
  markup = types.InlineKeyboardMarkup() 
  btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://www.tryexponent.com/blog/ai-engineer-interview-questions')
  btn2 = types.InlineKeyboardButton('Удалить', callback_data='delete')
  btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')

  # Стилизация кнопок
  markup.row(btn1)
  markup.row(btn2, btn3)

  bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
  chatId = callback.message.chat.id,
  messageId = callback.message.message_id

  if callback.data == 'delete':
    bot.delete_message(chatId, messageId - 1)
  elif callback.data == 'edit':
    bot.edit_message_text('Edit text', chatId, messageId)

# Наша программа постоянно выполняется
bot.polling(none_stop = True)