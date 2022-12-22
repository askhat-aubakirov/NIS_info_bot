'''
NIS Info Bot 
python-telegram-bot v13.15 is used
Developed by:
- Askhat Aubakirov, https://www.linkedin.com/in/askhattio/
- Azat Kabiden
Important links for the bot:
    code examples:
        https://github.com/python-telegram-bot/v13.x-wiki/wiki/Code-snippets#keyboard-menus
        https://github.com/askhat-aubakirov/conversation-handler-test-bot
        https://github.com/askhat-aubakirov/urban-dictionary-telegram-bot
    info required:
        https://ptr.nis.edu.kz/o-shkole-2/pretendentam/
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

#my test bot (cactus_bot, teacup bot) token
#updater = Updater("5354566347:AAFl3UEnNV8ZIKnMZa2WnF6TFtxxqLOgCe4")

#NISinfo_bot TOKEN by Azat
updater = Updater("5066784590:AAF-QzNoj2TQxE7EuXWQL6TfI12y1OXqogo")
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
  ["/start"], ["/cancel"]
]
ru_custom_keyboard = ReplyKeyboardMarkup(ru_custom_keyboard)

kz_custom_keyboard = [
  ["Құжаттарды қабылдау"],
  ["Қажетті құжаттар тізімі"],
  ["Қабылдау комиссиясының жұмыс уақыты"],
  ["Тестілеу күндері"],
  ["Тестілеудегі пәндер тізімі"],
  ["Байқау тестілеуі"],
  ["Тест мысалдары"],
  ["\"Өркен\" гранты туралы"],
  ["Тестілеу ережелері"],
  ["Тест нәтижелері"],
  ["Байланыстар мен мекенжай"],
  ["Бот туралы"],
  ["Сұрақ қою"],
  ["Қосымша: Солтүстік Қазақстан облысына арналған интернат"],
  ["Жиі қойылатын сұрақтар"],
  ["Шығу"],
  ["/start"], ["/cancel"]
]

kz_custom_keyboard = ReplyKeyboardMarkup(kz_custom_keyboard)

print("program started")


def start(update: Update, context: CallbackContext):

  custom_keyboard = [['Қазақ тілі'], ['Русский'],
                     ["Басынан бастау/Начать заново"], ["/start"], ["/cancel"]]
  reply_markup = ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True)
  message = update.message.reply_text(
    f"Здравствуйте, {update.effective_user.first_name}. \nТілді таңдаңыз || Выберите язык",
    reply_markup=reply_markup)

  return STATE0


def lang(update: Update, context: CallbackContext):
  if update.message.text.lower() in ["Қазақ тілі".lower()]:
    update.message.reply_text(
      "Сәлеметсіз бе! Сіз қазақ тілін таңдадыңыз. \nМен Петропавлдағы НЗМ ХББ ақпараттық ботымын және сіздердің сұрақтарыңызға жауап беруге келдім! Мәзірден сізді қызықтыратын тақырыпты таңдаңыз! \nЕгер басына оралғыңыз келсе, /start жіберіңіз"
    )
    update.message.reply_text(
      "«Назарбаев Зияткерлік мектептері» дербес білім беру ұйымы 2023-2024 оқу жылында Назарбаев Зияткерлік мектептерінің 7-сыныптарында білім алу үшін үміткерлерге Қазақстан Республикасы Тұңғыш Президенті – Елбасының «Өркен» білім беру грантын тағайындауға конкурс жариялайды. \n\nБарлық қажетті ақпарат мына сілтемеде жарияланған: https://ptr.nis.edu.kz/o-shkole-2/pretendentam/#1640167513886-a1cf7f5b-4a20. \n\nМаңызды ақпарат: келесі жылы мектеп формасы берілмейді, тамақ күніне бір рет беріледі (тек түскі ас)»"
    )
    update.message.reply_text("Сізді қызықтыратын санатты таңдаңыз:",
                              reply_markup=kz_custom_keyboard)

    return STATE1

  elif update.message.text.lower() in ["Русский".lower()]:
    update.message.reply_text(
      "Привет! Вы выбрали русский язык. \nЯ информационный бот НИШ ХБН г. Петропавловска и я здесь, чтобы ответить на Ваши вопросы! Выберите интересующую Вас тему в меню! \nЕсли Вы хотите вернуться в начало, отправьте /start"
    )
    update.message.reply_text(
      "Автономная организация образования «Назарбаев Интеллектуальные школы» с целью формирования ученического контингента на 2023-2024 учебный год объявляет сроки проведения конкурсного отбора претендентов для присуждения образовательного гранта Первого Президента Республики Казахстан – Елбасы «Өркен» на обучение в 7 классах Назарбаев Интеллектуальных школ.\n\nВся необходимая информация опубликована по ссылке: https://ptr.nis.edu.kz/o-shkole-2/pretendentam/#1640167513886-a1cf7f5b-4a20. \n\nВажная информация: в следующем году школьная форма выдаваться не будет, а питание будет обеспечиваться одноразовое (только обед)"
    )
    update.message.reply_text("Выберите интересующую Вас категорию:",
                              reply_markup=ru_custom_keyboard)
    return STATE2
  elif update.message.text.lower() in ["Басынан бастау/Начать заново".lower()]:
    update.message.reply_text(
      "/start командасын пайдаланыңыз\nИспользуйте команду /start")
    return ConversationHandler.END
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
  elif update.message.text.lower() in [
      "Режим работы Приемной Комиссии".lower()
  ]:
    update.message.reply_text(
      "График работы приемной комиссии:\n\nПонедельник — пятница с 9.00 до 18.00 часов \nВ субботу с 9.00 до 13.00 часов \nОбеденный перерыв с 12.00-13.00 часов\nПраздничные дни: 16, 31 декабря 2022 года. 1, 2, 7 января 2023 года.\nВыходной день: 17 декабря 2022 года.",
      reply_markup=ru_custom_keyboard)
    return STATE2
  elif update.message.text.lower() in ["Даты тестирования".lower()]:
    update.message.reply_text(
      "Комплексные тестирования проводятся 2-3 марта 2023 года.",
      reply_markup=ru_custom_keyboard)
    return STATE2
  elif update.message.text.lower() in [
      "Перечень предметов в тестировании".lower()
  ]:
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
    update.message.reply_text(
      "Примеры тестов:\nНа русском: https://www.nis.edu.kz/ru/applicants/konkurs-tasks/?id=7323\nНа казахском: https://www.nis.edu.kz/kz/applicants/konkurs-tasks/?id=7324",
      reply_markup=ru_custom_keyboard)
    return STATE2
  elif update.message.text.lower() in ["О гранте \"Өркен\"".lower()]:
    update.message.reply_text(
      "Информация о гранте в скором времени будет опубликована по ссылке: https://www.nis.edu.kz/ru/applicants/student/",
      reply_markup=ru_custom_keyboard)
    return STATE2
  elif update.message.text.lower() in ["Правила тестирования".lower()]:
    update.message.reply_text(
      "Тестирование проводится в 2 дня, 2 и 3 марта 2023 года.\nБланки ответов заполняются ручкой с черной пастой (негелевая паста). При себе претенденту необходимо иметь пропуск, который предоставляется после принятия приемной комиссией документов.\n\nВо время прохождения конкурса Претенденту запрещается: \n1) обмениваться тестами, списывать\n2) иметь/пользоваться мобильными телефонами, смарт-часами, другими гаджетами, калькуляторами и другими информационно-вычислительными устройствами\n4) заполнять лист ответоа после истечения времени, выносить лист ответов, сборник тестов/черновик из аудитории тестирования",
      reply_markup=ru_custom_keyboard)
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
      "Бот был разработан для использования НИШ ХБН г. Петропавловска.\nРазработчики:\nАсхат Аубакиров, aubakirov_a@ptr.nis.edu.kz,\nhttps://www.linkedin.com/in/askhattio/\nАзат Кабиден",
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
  else:
    update.message.reply_text("Используйте команду /start или /cancel")


def kz_get_info(update: Update, context: CallbackContext):

  if update.message.text.lower() in ["Құжаттарды қабылдау".lower()]:
    update.message.reply_text(
      "Құжат қабылдау 2022 жылғы 1 желтоқсаннан 2023 жылғы 10 қаңтарға дейін",
      reply_markup=kz_custom_keyboard)
    return STATE1
  elif update.message.text.lower() in ["Қажетті құжаттар тізімі".lower()]:
    update.message.reply_text(
      "Үміткерлер конкурстық іріктеуге қатысу үшін қабылдау комиссиясына келесі құжаттарды тапсырады:\n\n1) Конкурсқа қатысу үшін өтініш (жуктеу) беру (қабылдау комиссиясында толтыруға болады);\n\n2) Сауалнама (жуктеу) толтыру (қабылдау комиссиясында толтыруға болады);\n\n3) Үміткердің туу туралы куәлігінің көшірмесі, үміткердің ЖСН-і, бар болған жағдайда жеке бас құжатының көшірмесі, заңды өкілдің ЖСН-і көрсетілген жеке куәлігінің көшірмесі;\n\n4) Үміткердің соңғы оқу жылындағы үлгерімі мен тәртібінің, егер үміткер оқу жылын аяқтамаған жағдайда оқуын жалғастыратын болса, оқу жылының I жарты жылдығындағы үлгерімі мен тәртібі туралы табелінің көшірмесі. Талап етілген құжаттар оқитын мектеп басшысының қолымен расталып, тиісті білім беру ұйымының мөрімен бекітілуі керек (Ескерту: құжаттарды 6-сыныптың 1-ші жартыжылдығы аяқталғанға дейін тапсырсаңыз 5-сыныптың табелі қабылданады, 6-сыныптың 1-ші жарты жылдығы аяқталған соң тапсырсаңыз 6-сыныптың 1-ші жартыжылдық табелі қабылданады).\n\nБілім беру деңгейі мен оқу бағдарламасының айырмашылығы салдарынан Қазақстан Республикасының білім беру ұйымдарының сыныптарынан өзгеше болатын шетелдік білім беру мекемелері мен халықаралық мектептердің оқушыларынан басқа орта білім беру ұйымдарының 7 сыныбында білім алатын үміткерлердің келесі оқу жылында Зияткерлік мектептердің осы сыныбында қайта білім алуға құқықтары жоқ;\n\nОқу бағдарламасы мен бағалау шкалалары Қазақстан Республикасының білім беру ұйымдарының оқу бағдарламалары мен бағалау шкалаларынан ерекшеленетін шетелдік білім беру ұйымдарында немесе халықаралық мектептерде оқитын үміткерлер оқитын мектебінен бағдарламаның мазмұны мен бағалау шкалаларын түсіндіретін ресми хаттары оқу үлгерімі табеліне (бағалау транскрипті) қоса тіркеледі.\n\n5) Үміткердің графикалық файл түріндегі 1 МБ (мегабайт) кем емес көлемі 3х4 см. цифрлі фотосуреті немесе үміткердің фототүсірілімі құжат тапсыру кезінде қабылдау комиссиясында жасалынады.\n\nФотосурет ақшыл түсті фонда қатаң анфаста орындалады, бейтарап бет көрінісі мен ауызы жабық болуы қажет, бет пішіні фотосуреттің жалпы көлемінің 75% алуы тиіс. Компьютерлік сканерлеу, модельдеу немесе ксерокөшірмелеу әдісімен жасалынған суреттер қабылданбайды. Суретке түсіру кезінде бас киім және көзілдірік рұқсат етілмейді. Көздері ашық, анық көрінетін және шашымен жабылмаған. Фотосуреттің көлемі 450х600 пиксельден кем емес рұқсат ету шамасымен 600 пиксель/дюйм (dpi) төмен емес болуы тиіс.\n\nКөрсетілген барлық құжаттар мұқабасы түссіз 10 файлдық пластикалық папкаға салынады.",
      reply_markup=kz_custom_keyboard)
    return STATE1
  elif update.message.text.lower() in [
      "Қабылдау комиссиясының жұмыс уақыты".lower()
  ]:
    update.message.reply_text(
      "Қабылдау комиссиясының жұмыс кестесі: \nДүйсенбі-жұма күндері 9.00-ден 18.00-ге дейін \nСенбі күні 9.00-ден 13.00-ге дейін.\nТүскі үзіліс уақыты: 12.00 -13.00-ге дейін\nМереке күндері: 2022 жылғы 16, 31 желтоқсан, 2023 жылғы 1, 2, 7 қаңтар\nДемалыс күні: 2022 жылғы 17 желтоқсан",
      reply_markup=kz_custom_keyboard)
    return STATE1
  elif update.message.text.lower() in ["Тестілеу күндері".lower()]:
    update.message.reply_text(
      "Кешенді тестілеу 2023 жылдың 2-3 наурызында өткізіледі.",
      reply_markup=kz_custom_keyboard)
    return STATE1
  elif update.message.text.lower() in ["Тестілеудегі пәндер тізімі".lower()]:
    update.message.reply_text(
      "2 наурыз: Жаратылыстану-математикалық бағыттағы пәндерді игеру қабілетін бағалау тесті:\nМатематика, Сандық сипаттамалар, Жаратылыстану\nТесттің ұзақтылығы: 120 минут \n3 наурыз: Тілдік тест: Қазақ тілі, Орыс тілі, Ағылшын тілі\nТесттің ұзақтылығы: 120 минут",
      reply_markup=kz_custom_keyboard)
    return STATE1
  elif update.message.text.lower() in ["Байқау тестілеуі".lower()]:
    update.message.reply_text(
      "Байқау тестілеу келесі күндерге жоспарланған:\n\n24 желтоқсан\n24 желтоқсанға тіркеу 14-21.12.2022 ж. ашық.\n\n14 қаңтар\nТіркеу 28.12.2022-01.11.2023 аралығында ашық. \n\n28 қаңтар\nТіркеу 18-25.01.2023 ж.\n\n11 ақпан\nТіркелу 01-08.02.2023 ж. аралығында ашық \n\nБағасы: 12 000 теңге\nБрондау: https://trialtest.nis.edu.kz/",
      reply_markup=kz_custom_keyboard)
    return STATE1
  elif update.message.text.lower() in ["Тест мысалдары".lower()]:
    update.message.reply_text(
      "Тест мысалдары:\nОрыс тілінде: https://www.nis.edu.kz/ru/applicants/konkurs-tasks/?id=7323\nҚазақ тілінде: https://www.nis.edu.kz/kz/applicants /konkurs-tasks/?id=7324",
      reply_markup=kz_custom_keyboard)
    return STATE1
  elif update.message.text.lower() in ["\"Өркен\" гранты туралы".lower()]:
    update.message.reply_text(
      "Грант туралы ақпарат жақын арада мына сілтемеде жарияланады: https://www.nis.edu.kz/kz/applicants/student/",
      reply_markup=kz_custom_keyboard)
    return STATE1
  elif update.message.text.lower() in ["Тестілеу ережелері".lower()]:
    update.message.reply_text(
      "Тестілеу 2 күн, 2023 жылдың 2 және 3 наурызында өткізіледі.\nЖауап үлгілері қара сиялы қаламмен (гельсіз паста) толтырылады. Үміткердің өзімен бірге қабылдау комиссиясы құжаттарды қабылдағаннан кейін берілетін рұқсат қағазы болуы керек.\n\nКонкурс кезінде Талапкерге: \n1) тест алмасуға, алдау\n2) ұялы телефонның болуы/пайдалануына тыйым салынады. телефондар, смарт сағаттар, басқа да гаджеттер, калькуляторлар және басқа да ақпаратты есептеу құрылғылары\n4) уақыт өткеннен кейін жауап парағын толтыру, тестілеу аудиториясынан жауап парағын, тест кітапшасын/ жобасын шығару",
      reply_markup=kz_custom_keyboard)
    return STATE1
  elif update.message.text.lower() in ["Тест нәтижелері".lower()]:
    update.message.reply_text(
      "Конкурстық іріктеу нәтижелерімен мына сілтеме бойынша танысуға болады: https://www.nis.edu.kz/kz/applicants/konkurs-results/",
      reply_markup=kz_custom_keyboard)
    return STATE1
  elif update.message.text.lower() in ["Байланыстар мен мекенжай".lower()]:
    update.message.reply_text(
      "Мекен-жайы: Петропавл қ., көш. Ибраева, 22А\nТелефон: +7 (7152) 55-97-22",
      reply_markup=kz_custom_keyboard)
    return STATE1
  elif update.message.text.lower() in ["Бот туралы".lower()]:
    update.message.reply_text(
      "Бот Петропавл қаласындағы НЗМ ХБН пайдалану үшін әзірленген.\nӘзірлеушілер:\nАсхат Аубакиров, aubakirov_a@ptr.nis.edu.kz,\nhttps://www.linkedin.com/in/askhattio/\nАзат Кабиден",
      reply_markup=kz_custom_keyboard)
    return STATE1
  elif update.message.text.lower() in ["Сұрақ қою".lower()]:
    update.message.reply_text(
      "Барлық сұрақтар бойынша +7(7152) 55-97-22 телефонына хабарласыңыз немесе aubakirov_a@ptr.nis.edu.kz электронды поштасына жазыңыз.",
      reply_markup=kz_custom_keyboard)
    return STATE1
  elif update.message.text.lower() in [
      "Қосымша: Солтүстік Қазақстан облысына арналған интернат".lower()
  ]:
    update.message.reply_text(
      "Интернат Солтүстік Қазақстан облысынан келген үміткерлерге беріледі",
      reply_markup=kz_custom_keyboard)
    return STATE1
  elif update.message.text.lower() in ["Жиі қойылатын сұрақтар".lower()]:
    update.message.reply_text(
      "1) Қандай жағдайларда құжаттарды қабылдаудан бас тартуға болады?\nҚұжаттарды қабылдаудан бас тартуға мыналар негіз болуы мүмкін:\n- конкурстық іріктеуге қатысуға өтінімді белгіленген мерзімнен кешіктіру;\n- толық емес құжат ұсыну. құжаттар тізімі.\n\n2) Құжаттарды басқа тұлға арқылы беруге бола ма?\n-Қабылдау комиссиясына үшінші тұлғаның сенімхатсыз берген құжаттары қабылданбайды. Егер адамның қол қоюға құқығы бар сенімхаты болса, онда құжаттар қабылданады.",
      reply_markup=kz_custom_keyboard)
    return STATE1
  elif update.message.text.lower() in ["Шығу".lower()]:
    update.message.reply_text(
      "Бот аяқталуда.\nҚайтадан бастау үшін /start жіберіңіз",
      reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END
  else:
    update.message.reply_text("/cancel немесе /start командасын пайдаланаңыз")


def cancel(update: Update, context: CallbackContext):
  update.message.reply_text(
    f"Ботпен жұмысты қайта бастау үшін /start пайдаланыңыз\nЧтобы начать работу с бото заново, используйте /start",
    reply_markup=ReplyKeyboardRemove())
  return ConversationHandler.END


choice_regex = re.compile(
  r"^(Қазақ тілі|Русский|Басынан бастау/Начать заново)$", re.IGNORECASE)
kz_choice1_regex = re.compile(
  r"^(Құжаттарды қабылдау|Қажетті құжаттар тізімі|Қабылдау комиссиясының жұмыс уақыты|Тестілеу күндері|Тестілеудегі пәндер тізімі|Байқау тестілеуі|Тест мысалдары|\"Өркен\" гранты туралы|Тестілеу ережелері|Тест нәтижелері|Байланыстар мен мекенжай|Бот туралы|Сұрақ қою|Қосымша: Солтүстік Қазақстан облысына арналған интернат|Жиі қойылатын сұрақтар|Шығу)$",
  re.IGNORECASE)

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
print("bot is listening")
updater.idle()
