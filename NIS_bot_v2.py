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
    info required:
        https://ptr.nis.edu.kz/o-shkole-2/pretendentam/
1) set up answers for buttons
    1.1) manually type the data from website 
    OR
    1.2) scrape the website every time
2) buttons and info should be:
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
        О гранте "Өркен"
        Правила тестирования
        Результаты теста ???
        Контакты и адрес
        О боте
        Задать вопрос
        Дополнительно: Интернат для СКО
        FAQ
4) Get TOKEN from Azat (contacts will be soon shared by D. Ualiev) 
'''

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
  ["О гранте \"Өркен\""],
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

kz_custom_keyboard = [["kzopt1"], ["kzopt2"], ["kzopt3"]]

kz_custom_keyboard = ReplyKeyboardMarkup(kz_custom_keyboard)


def start(update: Update, context: CallbackContext):

  custom_keyboard = [['Казахский'], ['Русский']]
  reply_markup = ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True)
  message = update.message.reply_text(
    f"Здравствуйте, {update.effective_user.first_name}. \nВыберите язык",
    reply_markup=reply_markup)

  return STATE0


def lang(update: Update, context: CallbackContext):
  print(update.message.text.lower())
  if update.message.text.lower() in ["Казахский".lower()]:
    update.message.reply_text("Вы выбрали казахский")

    #reply_markup = ReplyKeyboardMarkup(kz_custom_keyboard, one_time_keyboard=True)
    update.message.reply_text("choose option", reply_markup=kz_custom_keyboard)

    return STATE1

  elif update.message.text.lower() in ["Русский".lower()]:
    update.message.reply_text(
      "Привет! Вы выбрали русский язык. \nЯ информационный бот НИШ ХБН г. Петропавловска и я здесь, чтобы ответить на Ваши вопросы! Выберите интересующую Вас тему в меню! \nЕсли Вы хотите вернуться в начало, отправьте /start"
    )
    update.message.reply_text(
      "Автономная организация образования «Назарбаев Интеллектуальные школы» с целью формирования ученического контингента на 2023-2024 учебный год объявляет сроки проведения конкурсного отбора претендентов для присуждения образовательного гранта Первого Президента Республики Казахстан – Елбасы «Өркен» на обучение в 7 классах Назарбаев Интеллектуальных школ.\n\nВся необходимая информация опубликована по ссылке: https://ptr.nis.edu.kz/o-shkole-2/pretendentam/#1640167513886-a1cf7f5b-4a20. \n\nВажная информация: в следующем году школьная форма выдаваться не будет, а питание будет обеспечиваться одноразовое (только обед)")
    update.message.reply_text("Выберите интересующую Вас категорию:",
                              reply_markup=ru_custom_keyboard)
    return STATE2

  else:
    update.message.reply_text("error occured")
    return ConversationHandler.END


def ru_get_info(update: Update, context: CallbackContext):

  if update.message.text.lower() in ["Прием документов".lower()]:
    update.message.reply_text(
      "Прием документов с 1 декабря 2022 года по 10 января 2023 года",
      reply_markup=ru_custom_keyboard)
    return STATE2
  elif update.message.text.lower() in [
      "Перечень необходимых документов".lower()
  ]:
    update.message.reply_text(
      "Для участия в конкурсном отборе при поступлении в Интеллектуальную школу, претендентом предоставляются в приемную комиссию следующие документы:",
      reply_markup=ru_custom_keyboard)
    update.message.reply_text(
      "1) заявление на участие в конкурсе (заполняется в приемной комиссии);\n\n2) заполненная анкета (форма анкеты скачивается при бронировании места и времени, заполнятся заранее и предоставляется вместе с другими документами, заполняется в приемной комиссии);\n\n3) копии свидетельства о рождении претендента, ИИН претендента, удостоверения личности претендента (в случае наличия), копия удостоверения личности законного представителя с указанием ИИН;\n\n4) копия табеля успеваемости и поведения претендента за предыдущий год обучения, предшествующий классу обучения в Интеллектуальной школе, за первое полугодие, в случае если претендент не закончил текущий учебный год и продолжает обучение. Требуемые документы должны быть заверены подписью руководителя и скреплены печатью соответствующей организации образования (примечание: в случае сдачи документов до окончания первого полугодия 6 класса сдается табель за 5 класс, после окончания первого полугодия 6 класса сдается табель за первое полугодие 6 класса).\n\n5) цифровая фотография претендента размером 3х4 см. в виде графического файла не более 1 МБ (мегабайт) или выполнить фотосъемку претендента в приемной комиссии при подаче документов.\nФотография выполняется строго в анфас на светлом фоне, с нейтральным выражением лица и закрытым ртом, в которой лицо занимает около 75% общей площади фотографии. Не допускается использование изображений, изготовленных методом компьютерного сканирования, моделирования или ксерокопирования. При фотографировании не допускаются головные уборы и очки. Глаза открыты, четко видны и не закрыты волосами. Размер фотографии должен быть не менее 450х600 пикселей с разрешением не ниже 600 пикселей/дюйм (dpi).\n\nВсе указанные документы подшиваются в пластиковую папку с прозрачной лицевой стороной на 10 файлов."
    )
    return STATE2
  elif update.message.text.lower() in ["Режим работы Приемной Комиссии".lower()]:
    update.message.reply_text(
      "График работы приемной комиссии:\n\nПонедельник — пятница с 9.00 до 18.00 часов \nВ субботу с 9.00 до 13.00 часов \nОбеденный перерыв с 12.00-13.00 часов\nПраздничные дни: 16, 31 декабря 2022 года. 1, 2, 7 января 2023 года.\nВыходной день: 17 декабря 2022 года.",
      reply_markup=ru_custom_keyboard)
    return STATE2
  elif update.message.text.lower() in ["Даты тестирования".lower()]:
    update.message.reply_text(
      "Комплексные тестирования проводятся 2-3 марта 2023 года.",
      reply_markup=ru_custom_keyboard)
    return STATE2
  elif update.message.text.lower() in ["Перечень предметов в тестировании".lower()]:
    update.message.reply_text(
      "Предметы для сдачи 2 марта: \nМатематика, Количественные характеристики, Естествознание\nПродолжительность теста 120 минут\n\nПредметы для сдачи 3 марта:\nКазахский язык, Русский язык, Английский язык\nПродолжительность теста 120 минут",
      reply_markup=ru_custom_keyboard)
    return STATE2
  elif update.message.text.lower() in ["Пробное тестирование".lower()]:
    update.message.reply_text(
      "Пробные тестирования запланированы на следующие даты:\n\n24 декабря\nРегистрация на 24 декабря открыта в период 14-21.12.2022\n\n14 января\nРегистрация открыта в период 28.12.2022-11.01.2023\n\n28 января\nРегистрация открыта в период 18-25.01.2023\n\n11 февраля\nРегистрация открыта в период 01-08.02.2023 \n\nСтоимость: 12 000 тг\nБронирование по ссылке: https://trialtest.nis.edu.kz/",
      reply_markup=ru_custom_keyboard)
    return STATE2
  elif update.message.text.lower() in ["Примеры тестов".lower()]:
    update.message.reply_text("Примеры тестов:\nНа русском: https://www.nis.edu.kz/ru/applicants/konkurs-tasks/?id=7323\nНа казахском: https://www.nis.edu.kz/kz/applicants/konkurs-tasks/?id=7324",
                              reply_markup=ru_custom_keyboard)
    return STATE2
  elif update.message.text.lower() in ["О гранте \"Өркен\"".lower()]:
    update.message.reply_text("Информация о гранте в скором времени будет опубликована по ссылке: https://www.nis.edu.kz/ru/applicants/student/", reply_markup=ru_custom_keyboard)
    return STATE2
  elif update.message.text.lower() in ["Правила тестирования".lower()]:
    update.message.reply_text("Тестирование проводится в 2 дня, 2 и 3 марта 2023 года.\nБланки ответов заполняются ручкой с черной пастой (негелевая паста). При себе претенденту необходимо иметь пропуск, который предоставляется после принятия приемной комиссией документов.", reply_markup=ru_custom_keyboard)
    return STATE2
  elif update.message.text.lower() in ["Результаты теста".lower()]:
    update.message.reply_text(
      "С результатами конкурсного отбора можно ознакомиться по ссылке: https://www.nis.edu.kz/ru/applicants/konkurs-results/",
      reply_markup=ru_custom_keyboard)
    return STATE2
  elif update.message.text.lower() in ["Контакты и адрес".lower()]:
    update.message.reply_text(
      "Адрес: г. Петропавловск, ул. Ибраева, 22А\nТелефон: +7(7152) 55-97-22",
      reply_markup=ru_custom_keyboard)
    return STATE2
  elif update.message.text.lower() in ["О боте".lower()]:
    update.message.reply_text(
      "Бот был разработан для использования НИШ ХБН г. Петропавловска.\nРазработчики:\nАсхат Аубакиров, aubakirov_a@ptr.nis.edu.kz,\nhttps://www.linkedin.com/in/askhattio/\n",
      reply_markup=ru_custom_keyboard)
    return STATE2
  elif update.message.text.lower() in ["Задать вопрос".lower()]:
    update.message.reply_text(
      "Если у Вас остались вопросы, звоните по номеру +7(7152) 55-97-22, или напишите письмо на почту aubakirov_a@ptr.nis.edu.kz",
      reply_markup=ru_custom_keyboard)
    return STATE2
  elif update.message.text.lower() in [
      "Дополнительно: Интернат для СКО".lower()
  ]:
    update.message.reply_text("Интернат предоставляется претендентам из СКО",
                              reply_markup=ru_custom_keyboard)
    return STATE2
  elif update.message.text.lower() in ["Часто задаваемые вопросы".lower()]:
    update.message.reply_text(
      "1) В каких случаях мне может быть отказано в приеме документов?\nОснованием для отказа в приеме документов может являться:\n- подача заявления об участии в конкурсном отборе позже установленных сроков;\n- предоставление неполного перечня документов.\n\n2) Можно ли передать документы через другого человека?\n-Документы, предоставленные в приемную комиссию третьим лицом без доверенности, не принимаются. Если у человека есть доверенность с правом подписи, то документы принимаются.",
      reply_markup=ru_custom_keyboard)
    return STATE2

  elif update.message.text.lower() in ["Выход".lower()]:
    update.message.reply_text(
      "Завершаем работу с ботом.\nЧтобы начать работу заново, отправьте /start",
      reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def kz_get_info(update: Update, context: CallbackContext):

  if update.message.text.lower() in ["kzopt1"]:
    update.message.reply_text("nice test kz")

  return STATE1


def cancel(update: Update, context: CallbackContext):
  update.message.reply_text(f"It was a good test. Bye then!",
                            reply_markup=ReplyKeyboardRemove())
  return ConversationHandler.END


choice_regex = re.compile(r"^(Казахский|Русский)$", re.IGNORECASE)
kz_choice1_regex = re.compile(r"^(kzopt1|kzopt2|kzopt3)$", re.IGNORECASE)

#add some options
ru_choice1_regex = re.compile(
  r"^(Прием документов|Перечень необходимых документов|Режим работы Приемной Комиссии|Даты тестирования|Перечень предметов в тестировании|Пробное тестирование|Примеры тестов|О гранте \"Өркен\"|Правила тестирования|Результаты теста|Контакты и адрес|О боте|Задать вопрос|Дополнительно: Интернат для СКО|Часто задаваемые вопросы|Выход)$",
  re.IGNORECASE)

handler = ConversationHandler(
  entry_points=[CommandHandler("start", start)],
  states={
    STATE0: [MessageHandler(Filters.regex(choice_regex), lang)],
    STATE1: [MessageHandler(Filters.regex(kz_choice1_regex), kz_get_info)],
    STATE2: [MessageHandler(Filters.regex(ru_choice1_regex), ru_get_info)]
  },
  fallbacks=[CommandHandler("cancel", cancel)],
)

dispatcher.add_handler(handler)

updater.start_polling()
updater.idle()
