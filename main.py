import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import pandas as pd

TOKEN = "5078688865:AAFzYpvzBBSUC_AIpVT5lZRhPkqkFA-AJmg"
bot = telebot.TeleBot(TOKEN)

# commands = {
#     'start': 'Телеграм ботту башынан баштоо',
#     'help': 'Буйруктар жонундо маалымат',
#     #'gubernator': 'Президенттин ыйгарым укуктуу өкүлүнүн атына жазылган арыз \n(Баткен облусунун губернаторуна компенсация боюнча)',
#     #'yurist': 'Баткендеги юристтер менен байланышуу, юридикалык жардам алуу',
#     'interbilim': 'Оштогу "Интербилим" эл аралык борбору жөнүндө, байланышуу',
#     'crushact': 'База данных актов комиссии гражданской защиты выдает информацию по его кейсу',
#     #'familyhelp': 'Ссылки на закон и положения, какие документы нужно собрать и куда обращаться',
#     'peoplehelplink': 'Ссылки на законы и положения, какие документы нужно собрать и куда обращаться'
# }

df1 = pd.read_excel('dbtelegram_bot.xlsx', sheet_name='Сгоревшие дома Лейлек')
df2 = pd.read_excel('dbtelegram_bot.xlsx', sheet_name='Сгоревшие дома Баткен')
df3 = pd.read_excel('dbtelegram_bot.xlsx', sheet_name='Сгоревшие сараи Лейлек')
df4 = pd.read_excel('dbtelegram_bot.xlsx', sheet_name='Пострадавшие от мародерства Лей')
df5 = pd.read_excel('dbtelegram_bot.xlsx', sheet_name='Угнанный или сгоревший транспор')

def markup_inline():
    markup = InlineKeyboardMarkup()
    markup.width = 2

    markup.add(InlineKeyboardButton(text='✍️ Арыз жазуу', callback_data='aryz_jazuu')) \
        .add(InlineKeyboardButton('🌎 Оштогу "Интербилим" эл аралык борбору жөнүндө, байланышуу ',
                                  callback_data='interbilim_info')) \
        .add(InlineKeyboardButton('‍🌐 Сизге керек боло турган интернеттеги ссылкалар',
                                  callback_data='peoplehelplink')) \
        .add(InlineKeyboardButton('💴 Өзгөчө кырдаал: Зыянды баалоо боюнча маалымат', callback_data='crushact')) \

        
        #.add(InlineKeyboardButton('📖 Баардык буйрутмалар (командалар)', callback_data='listcommands'))
        #.add(InlineKeyboardButton('💴 Баткен - Үй тууралуу Компенсация маалыматы', callback_data='batkencrushact')) \
        #.add(InlineKeyboardButton('💴 ТЕСТ', callback_data='crushInfo')) \

        #.add(InlineKeyboardButton('💴 Өзгөчө кырдаалдардан келтирилген зыянды '
                          #        '\nбаалоо боюнча маалымат алуу', callback_data='crushact')) \


    return markup

def markup_inlineCrushAct():
    markup = InlineKeyboardMarkup()
    markup.width = 2

    markup.add(InlineKeyboardButton('💴 Лейлек - Үй тууралуу Компенсация маалыматы', callback_data='crushactleilekhouse')) \
        .add(InlineKeyboardButton('💴 Баткен - Үй тууралуу Компенсация маалыматы', callback_data='batkencrushact')) \
        #.add(InlineKeyboardButton('📖 Баардык буйрутмалар (командалар)', callback_data='listcommands'))

    return markup

def keyBoardAryz():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, one_time_keyboard=True)
    keyboard.row('✍️ Айыл өкмөтүнө арыз жазуу')
    keyboard.row('✍️ Жабыркаган жашоочулардын кылмыш иштердин жыйынтыктары боюнча РИИБга (РОВД) арыз')
    keyboard.row('✍️ Кадастр мамлекеттик мекемесине арыз')
    keyboard.row('✍️ Келтирилген зыяндын актын алуу боюнча арыз жазуу')

    keyboard.row('ℹ️ Башкы менюга кайтуу')

    return keyboard

def keyBoardCrush():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, one_time_keyboard=True)
    keyboard.row('ℹ️ Лейлек айылы - өрттөлгөн үйлөр компенсация жөнүндө маалымат')
    keyboard.row('ℹ️ Баткен айылы - өрттөлгөн үйлөр компенсация жөнүндө маалымат')
    keyboard.row('🚗 Лейлек айылы - өрттөлгөн же уурдалган авто унаа компенсация жөнүндө маалымат')
    keyboard.row('🚗 Баткен айылы - өрттөлгөн же уурдалган авто унаа компенсация жөнүндө маалымат')
    keyboard.row('ℹ️ Лейлек айылы - мародерлук кесепетинин айынан жабыр таткандар жөнүндө маалымат')
    keyboard.row('ℹ️ Башкы менюга кайтуу')

    return keyboard

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_first_name = str(message.chat.first_name)
    welcome_message = '\nМенин атым Жер Там Бот! Мен виртуалдык юрист болом.' \
                      '\nМен сизге арыздарды түзүүгө жардам берип' \
                      '\nжана жабыр тарткан жашоочуларга жеңилдетилген салыктар, ' \
                      '\nпособие жана башка мүмкүнчүлүктөр жөнүндө маалымат берем'
    readyMessage = 'Эгерде сиз баштаганы даяр болсонуз, томонку буйруктарды басыныз!'

    # help_text = 'Буйруктардын тизмеси: '
    # for key, value in commands.items():
    #     help_text += '\n/' + key + ": " + value

    bot.send_message(message.chat.id, f'Саламатсызбы, {user_first_name}! {welcome_message}'
                                      f'\n\n{readyMessage}', reply_markup=markup_inline())

@bot.callback_query_handler(func=lambda call:True)
def call_back_menus(call):
    cid = call.message.chat.id

    if call.data =='aryz_jazuu':
       bot.send_message(cid, 'ℹ️ Төмөнкү менюдан керектүү басманы басыңыз!', reply_markup=keyBoardAryz())
       bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'yurist_call':
        bot.send_message(cid, 'Тел: 0312 123 456')
        bot.send_message(cid, 'Башкы меню: ', reply_markup=markup_inline())
    elif call.data == 'peoplehelplink':
        linksDict = {
            'link1': 'https://mlsp.gov.kg/kg/16-zhashka-chejinki-baldary-bar-muktazh-zharandarga-j-b-l-l-rg-j-b-l-g-k-m-k-ar-ajlyk-zh-l-kpul/',
            'link2': 'http://cbd.minjust.gov.kg/act/view/ru-ru/12231/30?cl=ky-kg&mode=tekst',
            'link3': 'http://cbd.minjust.gov.kg/act/view/ru-ru/111670/50?cl=ky-kg&mode=tekst',
            'link4': 'http://cbd.minjust.gov.kg/act/view/ru-ru/112294/10?cl=ky-kg&mode=tekst',
            'link5': 'https://www.sti.gov.kg/docs/default-source/ppkr/zkr_113_100921.pdf?sfvrsn=2',
            'link6': 'https://mlsp.gov.kg/kg/soczialdyk-zh%d3%a9l%d3%a9kpulga/',
            'link7': 'http://socfond.kg/kg/pensioners/23-Pieriechien-nieobkhodimykh-dokumientov-dlia-naznac/',
            'link8': 'http://cbd.minjust.gov.kg/act/view/ru-ru/12230/25?cl=ky-kg&mode=tekst',
            'link9': 'http://cbd.minjust.gov.kg/act/view/ru-ru/93624/55?cl=ky-kg&mode=tekst'
        }

        bot.send_message(cid, f"1) 16 жашка чейин балдарга көмөкпул алуу "
                              f"учун кандай документтер керек? - {linksDict['link1']}"
                              f"\n2) 16 жашка чейин балдарга көмөкпул алуу жөнүңдөгү жобо (положение) - {linksDict['link2']}"
                              f"\n3) Жөлөкпул мыйзамы - {linksDict['link3']}"
                              f"\n4) Кыргыз Республикасынын Баткен областына өзгөчө статус берилгенине байланыштуу айрым мыйзам актыларына өзгөртүүлөрдү киргизүү жөнүндө - {linksDict['link4']}"
                              f"\n5) Кыргыз Республикасынын «Баткен облусунун статусу жөнүндө» мыйзамы - {linksDict['link5']}"
                              f"\n6) Пенсиялык камсыз кылууга укугу жок адамдарга ар айлык социалдык жөлөкпул -“социалдык жөлөкпул” - {linksDict['link6']} "
                              f"\n7) Перечень необходимых документов для назначения пенсии по случаю потери кормильца - {linksDict['link7']}"
                              f"\n8) Мамлекеттик жөлөкпулдарды чектөөгө кайрылуу тартиби жана мамлекеттик жөлөкпулдарды чектөө тартиби жөнүндө ЖОБО - {linksDict['link8']}"
                              f"\n9) Жаранды ден соолугунун мүмкүнчүлүгү чектелүү адам деп эсептөө жөнүндө - {linksDict['link9']}")
        bot.send_message(cid, 'Башкы меню: ', reply_markup=markup_inline())
    elif call.data == 'interbilim_info':
        bot.send_message(cid, "Интербилим: "
                              "\n Ленин көчөсү 335/11"
                              "\n Тел: 03222 7 15 34"
                              "\nСайт: www.interbilimosh.kg"
                              "\nЭлектрондук дареги: interbilim.osh@gmail.com "
                              "\nInstagram: https://www.instagram.com/interbilimosh/"
                              "\nFacebook: https://www.facebook.com/interbilim.osh"
                              "\nВебсайт: https://www.interbilimosh.kg/"
                              "\nКартадагы адрес: ")
        bot.send_location(cid, 40.53369812331325, 72.79563171315304)
        bot.send_message(cid,'Башкы меню: ', reply_markup=markup_inline())
    # elif call.data == 'listcommands':
    #     help_text = 'Буйруктардын тизмеси: '
    #     for key, value in commands.items():
    #         help_text += '\n/' + key + ": " + value
    #     bot.send_message(cid, help_text)
    #     bot.send_message(cid, 'Башкы меню: ', reply_markup=markup_inline())
    elif call.data == 'crushact':
        message_comp_insrtuction = 'Лейлек айылы боюнча Өзгөчө кырдаалдардан келтирилген зыянды баалоо боюнча маалымат алуу үчүн' \
                                '\nУшундай форматта ФИО-ну жазыңыз Абылов Мурат Абдисатарович:'

        bot.send_message(cid, message_comp_insrtuction)
    elif call.data == 'batkencrushact':
        message_comp_insrtuction = 'Баткен айылы боюнча Өзгөчө кырдаалдардан келтирилген зыянды баалоо боюнча маалымат алуу үчүн' \
                                   '\nУшундай форматта ФИО-ну жазыңыз Абылов Мурат Абдисатарович:'

        bot.send_message(cid, message_comp_insrtuction)
    elif call.data == 'crushInfo':
        bot.send_message(cid, 'Выберите ', reply_markup=markup_inlineCrushAct())

    elif call.data == 'crushactleilekhouse':
        answer = 'Лейлек рулит!'
        bot.send_message(call.message.chat.id, answer)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        #bot.send_message(cid, 'Башкы меню: ', reply_markup=markup_inline())

# @bot.message_handler(commands=['help'])
# def command_help(message):
#     help_text = 'Буйруктардын тизмеси: '
#     for key, value in commands.items():
#         help_text += '\n/' + key + ": " + value
#     bot.reply_to(message, help_text)


# @bot.message_handler(commands=['aryz_jazuu_aokmot'])
# def download_ayil_okmotu(message):
#     cid = message.chat.id
#     bot.send_document(cid, open('Заявление.pdf', 'rb'))
#     bot.send_message(message.chat.id, "Бул документти печатька чыгарып "
#                                       "\nкеректуу жерлерге ФИО жана колунузду коюнуз!")

@bot.message_handler(commands=['rowd'])
def download_rowd(message):
    cid = message.chat.id

    bot.send_document(cid, open('Заявление.pdf', 'rb'))
    bot.send_message(message.chat.id, "Эгерде РОВД-га кайрылам деп жатсаныз "
                                      "\nБул документти печатька чыгарып "
                                      "\nкеректуу жерлерге ФИО жана колунузду коюнуз!")

@bot.message_handler(func=lambda message: message.text == "ℹ️ Башкы менюга кайтуу")
def main_menu(message):
    cid = message.chat.id
    bot.send_message(cid, 'Башкы меню', reply_markup=markup_inline())


@bot.message_handler(func=lambda message: message.text == "✍️ Айыл өкмөтүнө арыз жазуу")
def command_text_ayilokmot(message):
    cid = message.chat.id
    bot.send_document(cid, open('Башкы прокуратурадан кылмыш иштери боюнча кат.pdf', 'rb'))
    bot.send_document(cid, open('Келтирилген зыяндын актын алуу боюнча айыл өкмөтүнө арыз.pdf', 'rb'))
    bot.send_document(cid, open('Кенемте акча (компенсация) боюнча Баткен облусунун губернаторуна арыз.pdf', 'rb'))
    bot.send_message(cid,
                     "Сиз бул арызды колуңуз менен көчүрүп же принтерден печать кылып алып, колуңузду коюп коюңуз."
                     "\nБир копиясын жергиликтүү өкулгө, мамлекеттик органга берип, экинчи копиясына арызды кабыл алган\nадистин аты-жөнүн,колун жана датаны жаздырып алыңыз."
                     "\nАдистин телефон номерин жазып алыңыз. Арыздын экинчи копиясын сактап коюңуз."
                     "\nЖергиликтүү өкул мыйзам боюнча 14 күндүн ичинде жооп берет."
                     "\nБирок сиз адиске чалып, арызыңыз жөнүндө сураштырып туруңуз."
                     "\nАрызды жөнөтүп жана жооп алгандан кийин, юристиңиз менен байланышыңыз.")

    bot.send_message(cid, 'ℹ️ Керектуу басманы басыңыз, же башкы менюга кайтыш учун '
                         '\n"Башкы менюга кайтуу" деген басмасын басыңыз', reply_markup=keyBoardAryz())


@bot.message_handler(func=lambda message: message.text == "✍️ Жабыркаган жашоочулардын кылмыш иштердин жыйынтыктары боюнча РИИБга (РОВД) арыз")
def command_text_ayilokmot(message):
    cid = message.chat.id
    bot.send_message(cid,
                     "Лейлек районунун  РИИБдо № 03-038-2021-000219 сотко чейин иликтөө иштери жүргүзүү боюнча кылмыш иши козголгон"
                     "\n\nБаткен районунун  РИИБдо № 03-031-2021-000114 сотко чейин иликтөө иштери жүргүзүү боюнча кылмыш иши козголгон"
                     "\n\nБашкы прокуратурада № 03-150-2021-000036 сотко чейин иликтөө иштери жүргүзүү боюнча кылмыш иши козголгон")

    bot.send_document(cid, open('Башкы прокуратурадан кылмыш иштери боюнча кат.pdf', 'rb'))
    bot.send_message(cid,
                     "Сиз бул арызды колуңуз менен көчүрүп же принтерден печать кылып алып, колуңузду коюп коюңуз."
                     "\nБир копиясын жергиликтүү өкулгө, мамлекеттик органга берип, экинчи копиясына арызды кабыл алган\nадистин аты-жөнүн,колун жана датаны жаздырып алыңыз."
                     "\nАдистин телефон номерин жазып алыңыз. Арыздын экинчи копиясын сактап коюңуз."
                     "\nЖергиликтүү өкул мыйзам боюнча 14 күндүн ичинде жооп берет."
                     "\nБирок сиз адиске чалып, арызыңыз жөнүндө сураштырып туруңуз."
                     "\nАрызды жөнөтүп жана жооп алгандан кийин, юристиңиз менен байланышыңыз.")

    bot.send_message(cid, 'ℹ️ Керектуу басманы басыңыз, же башкы менюга кайтыш учун '
                          '\n"Башкы менюга кайтуу" деген басмасын басыңыз', reply_markup=keyBoardAryz())


@bot.message_handler(func=lambda message: message.text == "✍️ Кадастр мамлекеттик мекемесине арыз")
def command_text_ayilokmot(message):
    cid = message.chat.id
    bot.send_document(cid, open('Техникалык паспорт алуу үчүн Кадастр мекемесине арыз.pdf', 'rb'))
    bot.send_document(cid, open('Мамлекеттик акт (кызыл китеп) алуу үчүн Кадастр мекемесине арыз.pdf', 'rb'))
    bot.send_message(cid, "Сиз бул арызды колуңуз менен көчүрүп же принтерден печать кылып алып, колуңузду коюп коюңуз."
                          "\nБир копиясын жергиликтүү өкулгө, мамлекеттик органга берип, экинчи копиясына арызды кабыл алган\nадистин аты-жөнүн,колун жана датаны жаздырып алыңыз."
                          "\nАдистин телефон номерин жазып алыңыз. Арыздын экинчи копиясын сактап коюңуз."
                          "\nЖергиликтүү өкул мыйзам боюнча 14 күндүн ичинде жооп берет."
                          "\nБирок сиз адиске чалып, арызыңыз жөнүндө сураштырып туруңуз."
                          "\nАрызды жөнөтүп жана жооп алгандан кийин, юристиңиз менен байланышыңыз.")

    bot.send_message(cid, 'ℹ️ Керектуу басманы басыңыз, же башкы менюга кайтыш учун '
                          '\n"Башкы менюга кайтуу" деген басмасын басыңыз', reply_markup=keyBoardAryz())

@bot.message_handler(func=lambda message: message.text == "✍️ Келтирилген зыяндын актын алуу боюнча арыз жазуу")
def command_text_ayilokmot(message):
    cid = message.chat.id
    bot.send_document(cid, open('Келтирилген зыяндын актын алуу боюнча айыл өкмөтүнө арыз.pdf', 'rb'))
    bot.send_message(cid, "Сиз бул арызды колуңуз менен көчүрүп же принтерден печать кылып алып, колуңузду коюп коюңуз."
                          "\nБир копиясын жергиликтүү өкулгө, мамлекеттик органга берип, экинчи копиясына арызды кабыл алган\nадистин аты-жөнүн,колун жана датаны жаздырып алыңыз."
                          "\nАдистин телефон номерин жазып алыңыз. Арыздын экинчи копиясын сактап коюңуз."
                          "\nЖергиликтүү өкул мыйзам боюнча 14 күндүн ичинде жооп берет."
                          "\nБирок сиз адиске чалып, арызыңыз жөнүндө сураштырып туруңуз."
                          "\nАрызды жөнөтүп жана жооп алгандан кийин, юристиңиз менен байланышыңыз.")

    bot.send_message(cid, 'ℹ️ Керектуу басманы басыңыз, же башкы менюга кайтыш учун '
                          '\n"Башкы менюга кайтуу" деген басмасын басыңыз', reply_markup=keyBoardAryz())

@bot.message_handler(func=lambda message: message.text == "ℹ️ Лейлек айылы - өрттөлгөн үйлөр компенсация жөнүндө маалымат")
def command_text_crush(message):
    pass

@bot.message_handler(commands=['interbilim'])
def interbilim_info(message):
    cid = message.chat.id
    bot.send_message(cid, "Интербилим: "
                          "\n ул. Ленина 335/11"
                          "\n Тел: 03222 22952, 03222 21534"
                          "\nСайт: www.interbilimosh.kg"
                          "\nКартадагы адрес: ")
    bot.send_location(cid, 40.53369812331325, 72.79563171315304)

@bot.message_handler(commands=['crushact'])
@bot.message_handler(func=lambda message:True)
def compensassion_count(message):
    cid = message.chat.id

    fio = message.text

    compessasion_data= df1.loc[df1["ФИО"] == fio][["ФИО","Өрттөлгөн турак жайдын саны","Курулуштун суммасы(мин. сом)","Буюмдардын жана эмеректердин суммасы (мин.сом)","Жалпы  келтирилген чыгымдардын суммасы (миң сом)","Адрес"]]
    compessasion_list = compessasion_data.values.tolist()

    compessasion_data2 = df2.loc[df2["ФИО"] == fio][
        ["ФИО", "Өрттөлгөн турак жайдын саны", "Курулуштун суммасы(мин. сом)",
         "Буюмдардын жана эмеректердин суммасы (мин.сом)", "Жалпы  келтирилген чыгымдардын суммасы (миң сом)", "Адрес"]]
    compessasion_list2 = compessasion_data2.values.tolist()

    compessasion_data3 = df3.loc[df3["ФИО"] == fio][
        ["ФИО", "Өрттөлгөн турак жайдын саны", "Курулуштун суммасы(мин. сом)",
         "Буюмдардын жана эмеректердин суммасы (мин.сом)", "Жалпы  келтирилген чыгымдардын суммасы (миң сом)", "Адрес"]]
    compessasion_list3 = compessasion_data3.values.tolist()

    compessasion_data4 = df4.loc[df4["ФИО (тонолгон)"] == fio][
        ["ФИО (тонолгон)", "Адрес", "Буюмдардын жана эмеректердин суммасы (миң сом)",
         "Жалпы  келтирилген чыгымдардын суммасы (миң сом)"]]
    compessasion_list4 = compessasion_data4.values.tolist()

    compessasion_data5 = df5.loc[df5["ФИО"] == fio][
        ["ФИО", "Дареги", "Техниканын түрү", "Жалпы келтирилген чыгымдардын суммасы (сом)"]]
    compessasion_list5 = compessasion_data5.values.tolist()

    count = 1

    if not (compessasion_list or compessasion_list2 or compessasion_list3 or compessasion_list4 or compessasion_list5):
        bot.send_message(cid,'Сиз жазган ФИО боюнча төлөнө турган компенсация жөнүндө маалымат жок!')

    elif compessasion_list and compessasion_list4:
        bot.send_message(cid,f'\nБул турак жай Лейлек айылы боюнча катталган'
              f'\nСиз жазган ФИО боюнча {len(compessasion_list)} уйго компенсация бар')

        for i in compessasion_list:
            bot.send_message(cid,f'========================'
                  f'\n{count}-чи уйго болгон компенсация жонундо маалымат: '
                  f'\n----------------------'
                  f'\nФИО: {i[0]}'
                  f'\nӨрттөлгөн турак жайдын саны: {i[1]}'
                  f'\nАдрес: {i[5]}'
                  f'\nКурулуштун суммасы (миң сом): {float(i[2])} сом'
                  f'\nБуюмдардын жана эмеректердин суммасы (миң сом): {float(i[3])} сом'
                  f'\nЖалпы  келтирилген чыгымдардын суммасы (миң сом): {float(i[4])} сом')

            count += 1

        count = 1
        bot.send_message(cid,('#') * 40)
        bot.send_message(cid,f'\nБул ФИО Лейлек айылында тонолгон адамдардын бирине кирет'
              f'\nСиз жазган ФИО боюнча {len(compessasion_list4)} сарайга компенсация бар')

        for i in compessasion_list4:
            bot.send_message(cid,f'========================'
                  f'\n{count}-чи компенсация жонундо маалымат: '
                  f'\n----------------------'
                  f'\nФИО: {i[0]}'
                  f'\nАдрес: {i[1]}'
                  f'\nБуюмдардын жана эмеректердин суммасы (мин.сом): {float(i[2])} сом'
                  f'\nЖалпы  келтирилген чыгымдардын суммасы (миң сом): {float(i[3])} сом')

            count += 1


    elif compessasion_list:
        bot.send_message(cid,f'\nБул турак жай Лейлек айылы боюнча катталган'
              f'\nСиз жазган ФИО боюнча {len(compessasion_list)} уйго компенсация бар')

        for i in compessasion_list:
            bot.send_message(cid,f'========================'
                  f'\n{count}-чи уйго болгон компенсация жонундо маалымат: '
                  f'\n----------------------'
                  f'\nФИО: {i[0]}'
                  f'\nӨрттөлгөн турак жайдын саны: {i[1]}'
                  f'\nАдрес: {i[5]}'
                  f'\nКурулуштун суммасы (миң сом): {float(i[2])} сом'
                  f'\nБуюмдардын жана эмеректердин суммасы (миң сом): {float(i[3])} сом'
                  f'\nЖалпы  келтирилген чыгымдардын суммасы (миң сом): {float(i[4])} сом')

            count += 1

    elif compessasion_list2:
        bot.send_message(cid,f'\nБул турак жай Баткен айылы боюнча катталган'
              f'\nСиз жазган ФИО боюнча {len(compessasion_list2)} уйго компенсация бар')

        for i in compessasion_list2:
            bot.send_message(cid,f'========================'
                  f'\n{count}-чи уйго болгон компенсация жонундо маалымат: '
                  f'\n----------------------'
                  f'\nФИО: {i[0]}'
                  f'\nӨрттөлгөн турак жайдын саны: {i[1]}'
                  f'\nАдрес: {i[5]}'
                  f'\nКурулуштун суммасы: {float(i[2])} сом'
                  f'\nБуюмдардын жана эмеректердин суммасы (мин.сом): {float(i[3])} сом'
                  f'\nЖалпы  келтирилген чыгымдардын суммасы (миң сом): {float(i[4])} сом')

            count += 1

    elif compessasion_list3:
        bot.send_message(cid,f'\nБул сарай Лейлек айылы боюнча катталган'
              f'\nСиз жазган ФИО боюнча {len(compessasion_list3)} сарайга компенсация бар')

        for i in compessasion_list3:
            bot.send_message(cid,f'========================'
                  f'\n{count}-чи сарайга болгон компенсация жонундо маалымат: '
                  f'\n----------------------'
                  f'\nФИО: {i[0]}'
                  f'\nӨрттөлгөн турак жайдын саны: {i[1]}'
                  f'\nАдрес: {i[5]}'
                  f'\nКурулуштун суммасы(миң сом): {float(i[2])} сом'
                  f'\nБуюмдардын жана эмеректердин суммасы (миң сом): {float(i[3])} сом'
                  f'\nЖалпы  келтирилген чыгымдардын суммасы (миң сом): {float(i[4])} сом')

            count += 1

    elif compessasion_list4:
        bot.send_message(cid,f'\nБул ФИО Лейлек айылында тонолгон адамдардын бирине кирет'
              f'\nСиз жазган ФИО боюнча {len(compessasion_list4)} сарайга компенсация бар')

        for i in compessasion_list4:
            bot.send_message(cid,f'========================'
                  f'\n{count}-чи компенсация жонундо маалымат: '
                  f'\n----------------------'
                  f'\nФИО: {i[0]}'
                  f'\nАдрес: {i[1]}'
                  f'\nБуюмдардын жана эмеректердин суммасы (мин.сом): {float(i[2])} сом'
                  f'\nЖалпы  келтирилген чыгымдардын суммасы (миң сом): {float(i[3])} сом')

            count += 1

    elif compessasion_list5:
        bot.send_message(cid,f'\nБул ФИО боюнча Автоунаа боюнча төлөнө турган компенсация бар!'
              f'\nСиз жазган ФИО боюнча {len(compessasion_list5)} автоунаа боюнча компенсация бар!')

        for i in compessasion_list5:
            bot.send_message(cid,f'========================'
                  f'\n{count}-чи компенсация жонундо маалымат: '
                  f'\n----------------------'
                  f'\nФИО: {i[0]}'
                  f'\nАдрес: {i[1]}'
                  f'\nТехниканын түрү: {i[2]}'
                  f'\nЖалпы келтирилген чыгымдардын суммасы (сом): {float(i[3])} сом')

            count += 1

    bot.send_message(cid, 'Башкы меню: ', reply_markup=markup_inline())

#@bot.message_handler(func=lambda message:True)
@bot.message_handler(commands=['batkencrushact'])
@bot.message_handler(func=lambda message:True)
def compensassion_countBatken(message):
    cid = message.chat.id

    fio = message.text
    compessasion_data= df.loc[df["ФИО"] == fio][["ФИО","Өрттөлгөн турак жайдын саны","Курулуштун суммасы(мин. сом)","Буюмдардын жана эмеректердин суммасы (мин.сом)","Жалпы  келтирилген чыгымдардын суммасы (миң сом)","Адрес"]]
    compessasion_list = compessasion_data.values.tolist()

    count = 1

    if not compessasion_list:
        bot.send_message(cid,'Сиз жазган ФИО боюнча үйгө берилет турган компенсация жөнүндө маалымат жок!')
    else:
        bot.send_message(cid, f'БАТКЕН Сиз жазган ФИО боюнча {len(compessasion_list)} уйго компенсация бар')

    for i in compessasion_list:

        bot.send_message(cid, f'========================'
                              f'\n{count}-чи уйго болгон компенсация жонундо маалымат: '
                              f'\n----------------------'
                              f'\nФИО: {i[0]}'
                              f'\nӨрттөлгөн турак жайдын саны: {i[1]}'
                              f'\nАдрес: {i[5]}'
                              f'\nКурулуштун суммасы: {float(i[2])*1000} сом'
                              f'\nБуюмдардын жана эмеректердин суммасы (мин.сом): {float(i[3])*1000} сом'
                              f'\nЖалпы  келтирилген чыгымдардын суммасы (миң сом): {float(i[4])*1000} сом')

        count+=1

    bot.send_message(cid, 'Башкы меню: ', reply_markup=markup_inline())


bot.polling(none_stop=True)

