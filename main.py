VERSION = "1.1.1"
#################################################################################################

from modules import functions as func


def check_version():
    if (
        func.conf.VERSION == VERSION
        and func.greet.VERSION == VERSION
        and func.err.VERSION == VERSION
        and func.VERSION == VERSION
    ):
        return True
    else:
        return False


if not check_version():
    func.send_error_message(func.err.ERROR_VERSION_CONTROL)

func.check_python_version()


def start_process():
    p1 = func.multi_proc.Process(target=scheduler.start_schedule, args=()).start()


class scheduler:
    def start_schedule():
        func.schedule.every().day.at("00:02").do(func.greeting)  # Запускаем поздпавления в указанное время

        while True:
            func.schedule.run_pending()
            func.time.sleep(1)


@func.bot.message_handler(commands=["start"])
def button_message(message):
    keyboard = func.types.InlineKeyboardMarkup()
    key_ustav = func.types.InlineKeyboardButton(text=func.msg.MENU_BUTTON_USTAV, callback_data="ustav")
    keyboard.add(key_ustav)
    key_kodeks = func.types.InlineKeyboardButton(text=func.msg.MENU_BUTTON_KODEKS, callback_data="kodeks")
    keyboard.add(key_kodeks)
    func.bot.send_message(message.chat.id, func.msg.MENU_HEADER, reply_markup=keyboard)


@func.bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global user_id
    if call.data == "ustav":
        func.bot.send_document(call.message.chat.id, func.get_path_docs(func.conf.USTAV_FILE))
    elif call.data == "kodeks":
        func.bot.send_document(call.message.chat.id, func.get_path_docs(func.conf.KODEKS_FILE))


@func.bot.message_handler(commands=["stop"])
def stop_bot(message):
    if message.from_user.id == int(func.conf.ADMIN_ID):
        func.bot.send_message(message.chat.id, func.msg.EXIT_MESSAGE)
        func.bot.stop_polling()
        func.os._exit(func.os.EX_OK)


if __name__ == "__main__":  # Запускаем бота
    start_process()
    func.bot.polling(none_stop=True)


# @bot.message_handler(content_types=['text'])
# def get_roadname_query(message):  # получаем фамилию
#    roadname_query_del = message.text
#    #global retrive
#    connection = pymysql.connect(host=settings.HOST_DB, user=settings.USER_DB, passwd=settings.PASSW_DB,
#                                 database=settings.NAME_DB)
#    with connection:
#        cursor = connection.cursor()
#        sql = "DELETE FROM bot_bday_registry WHERE roadname='" + roadname_query_del + "'"
#        cursor.execute(sql)
#        connection.commit()
#        bot.send_message(settings.CHAT_ID,'Мембер ' + roadname_query_del + ' удален из базы')


# запускаем бота
# if __name__ == "__main__":
# while True:
