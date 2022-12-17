'''
NIS Info Bot 

python-telegram-bot v13.15 is used
Developed by:
- Askhat Aubakirov, https://www.linkedin.com/in/askhattio/
- ... + more authors ...

Important links for the bot:
    code examples:
        https://github.com/python-telegram-bot/v13.x-wiki/wiki/Code-snippets#keyboard-menus
        https://github.com/askhat-aubakirov/conversation-handler-test-bot
        https://github.com/askhat-aubakirov/urban-dictionary-telegram-bot
    csv to gSheets in Python:
        https://medium.com/craftsmenltd/from-csv-to-google-sheet-using-python-ef097cb014f9
    info required:
        https://ptr.nis.edu.kz/o-shkole-2/pretendentam/

1) set up answers for buttons
    1.1) manually type the data from website 
    OR
    1.2) scrape the website every time
2) make it collect usernames and send them real-time to google sheets on my drive (askhat.aub.work@gmail.com)
    2.1) make a function to count DISTINCT usernames, anon them
    2.2) make a real-time dashboard of uses per day
3) buttons and info should be:
    first things first: Выберите язык
                        Казахский
                        Русский
    Затем:
        Прием документов
        Перечень документов
        Режим работы приемной комиссии
        Даты тестирования
        Перечень предметов
        Пробное тестирование
        Примеры тестов
        О гранте "Оркен"
        Правила тестирования
        Результаты теста ???
        Контакты и адрес
        О боте
        Задать вопрос
        Дополнительно: Интернат для СКО
        FAQ
4) Get TOKEN from Azat (contacts will be soon shared by D. Ualiev) 
'''

import pandas as pd
import re
from telegram import (
    Update,
    ReplyKeyboardRemove,
    Update,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    CallbackContext,
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

users_names = []
timestamps = []
print(users_names)

updater = Updater("5354566347:AAFl3UEnNV8ZIKnMZa2WnF6TFtxxqLOgCe4")
dispatcher = updater.dispatcher

STATE0, STATE1, STATE2 = range(3)

ru_custom_keyboard = [
        ["Прием документов"],
        ["Перечень необходимых документов"],
        ["Режим работы Приемной Комиссии"],
        ["Даты тестирования"],
        ["Перечень предметов в тестировании"],
        ["Пробное тестирование"],
        ["Примеры тестов"],
        ["О гранте \"Оркен\""],
        ["Правила тестирования"],
        ["Результаты теста"],
        ["Контакты и адрес"],
        ["О боте"],
        ["Задать вопрос"],
        ["Дополнительно: Интернат для СКО"],
        ["Часто задаваемые вопросы"],
        ["Выход"],
]
print(len(ru_custom_keyboard))
ru_custom_keyboard = ReplyKeyboardMarkup(ru_custom_keyboard)

kz_custom_keyboard = [
        ["kzopt1"],
        ["kzopt2"],
        ["kzopt3"]
]

kz_custom_keyboard = ReplyKeyboardMarkup(kz_custom_keyboard)


def start(update: Update, context: CallbackContext):
    #saving name of the user to csv file for analytics 
    users_names.append(update._effective_user.full_name)
    
    custom_keyboard = [['Казахский'], ['Русский']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True)
    message = update.message.reply_text(f"Здравствуйте, {update.effective_user.first_name}. \nВыберите язык", reply_markup=reply_markup)
    
    timestamps.append(message.date)
    
    df = pd.DataFrame({"user_name": users_names, "timestamp": timestamps})
    df.to_csv('report1.csv', index = False, encoding='utf-8')
    print(df)

    return STATE0

def lang(update: Update, context: CallbackContext):
    print(update.message.text.lower())
    if update.message.text.lower() in ["Казахский".lower()]:
        update.message.reply_text("Вы выбрали казахский")

        #reply_markup = ReplyKeyboardMarkup(kz_custom_keyboard, one_time_keyboard=True)
        update.message.reply_text("choose option", reply_markup=kz_custom_keyboard)
        
        return STATE1
    
    elif update.message.text.lower() in ["Русский".lower()]:
        update.message.reply_text("Привет! Вы выбрали русский язык. \nЯ информационный бот НИШ ХБН г. Петропавловска и я здесь, чтобы ответить на Ваши вопросы! Выберите интересующую Вас тему в меню! \nЕсли Вы хотите вернуться в начало, отправьте /start")
        update.message.reply_text("Выберите интересующую Вас категорию:", reply_markup=ru_custom_keyboard)
        return STATE2
    
    else:
        update.message.reply_text("error occured")
        return ConversationHandler.END

def ru_get_info(update: Update, context: CallbackContext):
    
    if update.message.text.lower() in ["Прием документов".lower()]:
        update.message.reply_text("Документы принимаются туда-то и тогда-то", reply_markup=ru_custom_keyboard)
        return STATE2
    elif update.message.text.lower() in ["Перечень необходимых документов".lower()]:
        update.message.reply_text("Документы нужны всякие", reply_markup=ru_custom_keyboard)
        return STATE2
    elif update.message.text.lower() in ["Режим работы Приемной Комиссии".lower()]:
        update.message.reply_text("Приемная комиссия работает до 10 января с 9.00 утра до 18.00 вечера с перерывом на обед с 12.00 до 13.00", reply_markup=ru_custom_keyboard)
        return STATE2
    elif update.message.text.lower() in ["Даты тестирования".lower()]:
        update.message.reply_text("Тестирование будет проходить 2-3 марта, в два дня.", reply_markup=ru_custom_keyboard)
        return STATE2
    elif update.message.text.lower() in ["Перечень предметов в тестировании".lower()]:
        update.message.reply_text("В первый день: 1, 2, 3 \nВо второй день: 1, 2, 3", reply_markup=ru_custom_keyboard)
        return STATE2
    elif update.message.text.lower() in ["Пробное тестирование".lower()]:
        update.message.reply_text("Пробные тестирования запланированы на следующие даты:\n24 декабря\nЦена: 12 000 тг", reply_markup=ru_custom_keyboard)
        return STATE2
    elif update.message.text.lower() in ["Примеры тестов".lower()]:
        update.message.reply_text("Примеры тестов: блаблабла", reply_markup=ru_custom_keyboard)
        return STATE2
    elif update.message.text.lower() in ["О гранте \"Оркен\"".lower()]:
        update.message.reply_text("\"Оркен\" - это грант, который...", reply_markup=ru_custom_keyboard)
        return STATE2
    elif update.message.text.lower() in ["Правила тестирования".lower()]:
        update.message.reply_text("NO CHEATING", reply_markup=ru_custom_keyboard)
        return STATE2
    elif update.message.text.lower() in ["Результаты теста".lower()]:
        update.message.reply_text("С результатами теста можно ознакомиться по ссылке: ", reply_markup=ru_custom_keyboard)
        return STATE2
    elif update.message.text.lower() in ["Контакты и адрес".lower()]:
        update.message.reply_text("Адрес: г. Петропавловск, ул. Ибраева, 22А\nТелефон приемной комиссии: 4920", reply_markup=ru_custom_keyboard)
        return STATE2
    elif update.message.text.lower() in ["О боте".lower()]:
        update.message.reply_text("Бот был разработан для использования НИШ ХБН г. Петропавловска.\nРазработчики:\nАсхат Аубакиров, aubakirov_a@ptr.nis.edu.kz,\nhttps://www.linkedin.com/in/askhattio/\n", reply_markup=ru_custom_keyboard)
        return STATE2
    elif update.message.text.lower() in ["Задать вопрос".lower()]:
        update.message.reply_text("Если у Вас остались вопросы, напишите письмо на почту aubakirov_a@ptr.nis.edu.kz", reply_markup=ru_custom_keyboard)
        return STATE2
    elif update.message.text.lower() in ["Дополнительно: Интернат для СКО".lower()]:
        update.message.reply_text("Интернат предоставляется претендентам из СКО", reply_markup=ru_custom_keyboard)
        return STATE2
    elif update.message.text.lower() in ["Часто задаваемые вопросы".lower()]:
        update.message.reply_text("1) вопрос один?\nответ один\n\n2) вопрос два?\nответ два", reply_markup=ru_custom_keyboard)
        return STATE2

    elif update.message.text.lower() in ["Выход".lower()]:
        update.message.reply_text("Завершаем работу с ботом.\nЧтобы начать работу заново, отправьте /start", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END


def kz_get_info(update: Update, context: CallbackContext):
    
    if update.message.text.lower() in ["kzopt1"]:
        update.message.reply_text("nice test kz")

    return STATE1

def cancel(update: Update, context: CallbackContext):
    update.message.reply_text(f"It was a good test. Bye then!", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


choice_regex = re.compile(r"^(Казахский|Русский)$", re.IGNORECASE)
kz_choice1_regex = re.compile(r"^(kzopt1|kzopt2|kzopt3)$", re.IGNORECASE)

#add some options
ru_choice1_regex = re.compile(r"^(Прием документов|Перечень необходимых документов|Режим работы Приемной Комиссии|Даты тестирования|Перечень предметов в тестировании|Пробное тестирование|Примеры тестов|О гранте \"Оркен\"|Правила тестирования|Результаты теста|Контакты и адрес|О боте|Задать вопрос|Дополнительно: Интернат для СКО|Часто задаваемые вопросы|Выход)$", re.IGNORECASE)

handler = ConversationHandler(
    entry_points= [CommandHandler("start", start)],
    states= {
        STATE0: [MessageHandler(Filters.regex(choice_regex), lang)],
        STATE1: [MessageHandler(Filters.regex(kz_choice1_regex), kz_get_info)],
        STATE2: [MessageHandler(Filters.regex(ru_choice1_regex), ru_get_info)]
    },
    fallbacks= [CommandHandler("cancel", cancel)],
)

dispatcher.add_handler(handler)

updater.start_polling()
updater.idle()

