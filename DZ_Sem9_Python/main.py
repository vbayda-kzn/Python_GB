# Напишите бота, удаляющего из текста все слова, содержащие "абв". (текст вводит пользователь)
# Название бота - Learn_Python_Bot,    адрес бота - @vb_python_bot.

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


bot = Bot(token='***')
updater = Updater(token='***')
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет, чувак!')
    context.bot.send_message(update.effective_chat.id, 'Напиши мне что-нибудь, а я попытаюсь удалить слова, содержащие строку "абв"')
    
def find_and_cut(update, context):
    
    phrase = update.message.text.split()
    if phrase[0][0] == "/":
        context.bot.send_message(update.effective_chat.id, 'Приятель, я таких команд не знаю.')
    else:
        context.bot.send_message(update.effective_chat.id, 'Ок. Ща, пять сек!')
        for word in phrase:
            if "абв" in word.lower():
                phrase.remove(word)
        context.bot.send_message(update.effective_chat.id, " ".join(phrase))


start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, find_and_cut)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()
