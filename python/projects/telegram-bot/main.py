import telebot
import webbrowser

# Token для подсоединения к боту
bot = telebot.TeleBot('8834083876:AAHuL8dzablyeVmnK44QyEtrlcy22URqihg')


# По нажатию на кнопку старт выводится сообщение Привет!
# можно также и добавить другие команды ['start', 'start2']
@bot.message_handler(commands=['start'])
def main(message):
  bot.send_message(message.chat.id, 'Привет')

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

# Наша программа постоянно выполняется
bot.polling(none_stop = True)