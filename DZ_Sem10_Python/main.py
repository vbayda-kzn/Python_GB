# ДЗ: Добавить счет, сколько раз выиграл бот и пользователь.
#     Необходимо добавить команду, при вызове которой, бот говорит, кто сколько раз выиграл(выводит счет).

#     /score - команда вывода информации кто сколько раз побеждал.

from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from scripts import check
from random import choice as ch
import datetime


bot = Bot(token='###')
updater = Updater(token='###')
dispatcher = updater.dispatcher

data = {6: 4, 7: 4, 8: 4, 9: 4, 10: 4, 'Валет': 4, 'Дама': 4, 'Король': 4,
        'Туз': 4}

count_points_user = []
count_points_bot = 0

WINNER = None # 0 - ничья, 1 - выиграл пользователь, -1 - выиграл бот

BOT = 1
USER = 2

def save_result(win):
    with open("score.txt", 'a', encoding='utf-8') as file:
        file.write(f'{win + 1} {datetime.datetime.now()} \n')

def winner_count(update, context):
    print ("Привет, я в модуле winner_count!")
    count_win_bot= 0
    count_nich = 0
    count_win_plr = 0
    with open("score.txt", 'r', encoding='utf-8') as file:
        log_list = file.read().splitlines()
        print(log_list)
        for item in log_list:
            if item[0] == "0": count_win_bot += 1
            elif item[0] == "1": count_nich += 1
            else: count_win_plr += 1
    context.bot.send_message(update.effective_chat.id, f"Бот выиграл {count_win_bot} раз(а)\n" 
                                                       f"{update.effective_user.first_name} выиграл {count_win_plr} раз(а)\n"
                                                       f"В ничью сыграли {count_nich} раз(а)\n")

def winner_check(user, bots):
    global WINNER
    if (sum(user) > 21 and bots < 22) or (sum(user) < bots and bots <= 21):
        WINNER = -1
    elif (bots > 21 and sum(user) < 22) or (sum(user) > bots and sum(user) <= 21 and bots <= 21 and bots > 14):
        print("bots = ", bots, "player = ", sum(user))
        WINNER = 1
    elif sum(user) > 21 and bots > 21:
        WINNER = 0

def start(update, context):
    global count_points_user, count_points_bot, WINNER

    count_points_user.clear()
    count_points_bot = 0
    WINNER = None

    for i in range(2):
        data_object = ch(list(data.keys()))
        while data[data_object] == 0:
            data_object = ch(list(data.keys()))
        data[data_object] -= 1
        points = check(data_object)
        count_points_user.append(points)

    for i in range(2):
        data_object = ch(list(data.keys()))
        print(data_object)
        while data[data_object] == 0:
            data_object = ch(list(data.keys()))
        data[data_object] -= 1
        points = check(data_object)
        count_points_bot += points

    if sum(count_points_user) > 21 and count_points_bot < 22:
        context.bot.send_message(update.effective_chat.id, "Перебор, выиграл бот")
    elif count_points_bot > 21 and sum(count_points_user) < 22:
        context.bot.send_message(update.effective_chat.id, "Перебор, выиграл ты")
    elif sum(count_points_user) > 21 and count_points_bot > 21:
        context.bot.send_message(update.effective_chat.id, "Перебор, вы лузеры")
    else:
        a = '\n'.join([str(i) for i in count_points_user])
        context.bot.send_message(update.effective_chat.id, f"{a}\nСумма: {sum(count_points_user)}")

def yet(update, context):
    global count_points_user
    if sum(count_points_user) < 21:
        data_object = ch(list(data.keys()))
        while data[data_object] == 0:
            data_object = ch(list(data.keys()))
        data[data_object] -= 1
        points = check(data_object)
        count_points_user.append(points)
        a = '\n'.join([str(i) for i in count_points_user])
        winner_check(count_points_user, count_points_bot)
        context.bot.send_message(update.effective_chat.id, f"{a}\nСумма: {sum(count_points_user)}")
        if sum(count_points_user) > 21:
            context.bot.send_message(update.effective_chat.id, f"{update.effective_user.first_name}, у тебя перебор, ты проиграл.")
            save_result(WINNER)
            context.bot.send_message(update.effective_chat.id, f"Игра окончена, чтобы начать заново напишите /start")
    else:
        context.bot.send_message(update.effective_chat.id, "Ты не можешь взять больше!")

def stop(update, context):
    if WINNER == None:
        global count_points_bot
        context.bot.send_message(update.effective_chat.id, 'Вы закончили набор, теперь набирает бот')
        while (count_points_bot > 15 and ch([True, False]) and count_points_bot < 20) or count_points_bot <= 14:
            data_object = ch(list(data.keys()))
            while data[data_object] == 0:
                data_object = ch(list(data.keys()))
            data[data_object] -= 1
            points = check(data_object)
            count_points_bot += points
        winner_check(count_points_user, count_points_bot)
        context.bot.send_message(update.effective_chat.id, f'Кол-во очков у бота: {count_points_bot}\n'
                                                           f'Кол-во очков у {update.effective_user.first_name}: {sum(count_points_user)}')
        if WINNER == -1:
            context.bot.send_message(update.effective_chat.id, f"{update.effective_user.first_name}, "
                                                               f"увы, выиграл бот")
            save_result(WINNER)
            context.bot.send_message(update.effective_chat.id, f"Игра окончена, чтобы начать заново напишите /start")
        elif WINNER == 1:
            context.bot.send_message(update.effective_chat.id, f"{update.effective_user.first_name}, ты выиграл")
            save_result(WINNER)
            context.bot.send_message(update.effective_chat.id, f"Игра окончена, чтобы начать заново напишите /start")
        elif WINNER == 0:
            context.bot.send_message(update.effective_chat.id, f"{update.effective_user.first_name} вы с ботом лузеры")
            save_result(WINNER)
            context.bot.send_message(update.effective_chat.id, f"Игра окончена, чтобы начать заново напишите /start")
    else:
        if WINNER == -1:
            context.bot.send_message(update.effective_chat.id, f"{update.effective_user.first_name}, "
                                                               f"увы, выиграл бот")
            save_result(WINNER)
            context.bot.send_message(update.effective_chat.id, f"Игра окончена, чтобы начать заново напишите /start")
        elif WINNER == 1:
            context.bot.send_message(update.effective_chat.id, f"{update.effective_user.first_name}, ты выиграл")
            save_result(WINNER)
            context.bot.send_message(update.effective_chat.id, f"Игра окончена, чтобы начать заново напишите /start")
        elif WINNER == 0:
            context.bot.send_message(update.effective_chat.id, f"{update.effective_user.first_name} вы с ботом лузеры")
            save_result(WINNER)
            context.bot.send_message(update.effective_chat.id, f"Игра окончена, чтобы начать заново напишите /start")

start_handler = CommandHandler('start', start)
still_handler = CommandHandler('yet', yet)
stop_handler = CommandHandler('stop', stop)
total_score_handler = CommandHandler('score', winner_count)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(still_handler)
dispatcher.add_handler(stop_handler)
dispatcher.add_handler(total_score_handler)

updater.start_polling()
updater.idle()  # ctrl + c