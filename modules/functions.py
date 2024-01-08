import telebot
import pymysql
import time
import sys

from datetime import date
from modules import settings as conf
from templates import greetings as greet, errors as err
from datetime import datetime

#################################################################################################
VERSION = "1.0"
#################################################################################################

bot = telebot.TeleBot(conf.TOKEN)  # Инициируем бота


def check_python_version():
    required_version = conf.REQUIRED_PYTHON_VERSION
    major, minor, micro, realise_level, serial = sys.version_info
    py_version = f"{major}.{minor}.{micro}"
    if int(major) == int(required_version[0]) and int(minor) >= int(required_version[2:]):
        return py_version
    else:
        bot.send_message(
            conf.LOG_CHAT_ID,
            err.TITLE_ERROR
            + "\n"
            + get_timestamp()
            + err.ERROR_MSG_VERSION_1
            + py_version
            + "\n"
            + err.ERROR_MSG_VERSION_2
            + required_version,
        )
        bot.send_message(conf.LOG_CHAT_ID, err.INFO_TITLE + "\n" + get_timestamp() + err.ERROR_MSG_STOP)
        exit()


def get_full_name(fname="", lname="", road_name=""):  # Формируем полное имя
    full_name = f"{fname} {road_name} {lname}"
    return full_name


def calculate_age(born):  # Вычисляем возраст именинника
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    if str(age)[1] == "1":
        return f"{str(age)} год"
    elif "1" < str(age)[1] < "5":
        return f"{str(age)} года"
    elif str(age) == "11":
        return f"{str(age)} лет"
    else:
        return f"{str(age)} лет"


def get_message(fullname, bd_date, member_role=""):  # Формируем поздравление
    if fullname[5:11] != "OST MC":
        return (
            f"{greet.GREETING_TITLE}\n{greet.BD_MSG_1} {member_role} "
            f"{greet.BD_MSG_2},\n {fullname}!\n"
            f"{greet.BD_MSG_3} {calculate_age(bd_date)}!\n"
            f"\U0001F382\U0001F943"
            f"\U0001F943\U0001F943\U0001F382\n{greet.BD_MSG_4}"
        )
    else:
        return (
            f"{greet.GREETING_TITLE}\n{greet.OST_BD_MSG_1}"
            f" {calculate_age(bd_date)} {greet.OST_BD_MSG_2} "
            f"{fullname[5:11]}!\n{greet.OST_BD_TOAST}\n\U0001F943"
            f"\U0001F943\U0001F943"
        )


def get_timestamp():  # Получаем текущее значение даты/времени в формате dd.mm.yy hh:mm
    today = datetime.now()
    return today.strftime("%d.%m.%y - %H:%M - ")


def get_year():  # Получаем значение года в формате YYYY
    today = datetime.now()
    return today.strftime(" %Y ")


def send_error_message(err_obj):
    bot.send_message(conf.LOG_CHAT_ID, err.TITLE_ERROR + "\n" + get_timestamp() + str(err_obj))
    bot.send_message(conf.LOG_CHAT_ID, err.INFO_TITLE + "\n" + get_timestamp() + err.ERROR_MSG_STOP)
    exit()


def get_path_docs(file_name):  # Формируем путь к документу
    pdf_path = conf.PDF_PATH + file_name + ".pdf"
    try:
        return open(pdf_path, "rb")
    except Exception as error:
        send_error_message(error)


def get_path_photo(file_name):  # Формируем путь к изображению именника
    img_path = conf.IMAGE_PATH + file_name + ".jpg"
    try:
        return open(img_path, "rb")
    except Exception as error:
        send_error_message(error)


def post_from_db():  # Получаем данные из БД и постим сообщение
    try:
        connection = pymysql.connect(host=conf.HOST_DB, user=conf.USER_DB, passwd=conf.PASSW_DB, database=conf.NAME_DB)

        with connection:
            cursor = connection.cursor()
            retrive = (
                "SELECT * FROM `bot_bday_registry` WHERE DAYOFYEAR(curdate()) <= "
                "DAYOFYEAR(DATE_ADD(`bday`, INTERVAL (YEAR(NOW()) - YEAR(`bday`)) YEAR))"
                "AND DAYOFYEAR(curdate()) >= DAYOFYEAR(DATE_ADD(`bday`, INTERVAL (YEAR(NOW()) - YEAR("
                "`bday`)) YEAR));"
            )

            cursor.execute(retrive)
            rows = cursor.fetchall()

        flag_pause = 1
        for row in rows:
            name = "{1}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6])  # noqa: F523
            family = "{2}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6])  # noqa: F523
            roadname = "{3}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6])  # noqa: F523
            bday = "{4}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6])  # noqa: F523
            role = "{5}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6])  # noqa: F523
            s = bday.replace("-", " ")

            date_of_birth = datetime.strptime(s, "%Y %m %d")

            bot.send_photo(
                conf.CHAT_ID,
                get_path_photo(roadname),
                get_message(get_full_name(name, family, roadname), date_of_birth, role),
            )
            if len(rows) > 1 and len(rows) != flag_pause:
                time.sleep(conf.SEND_INTERVAL)
            flag_pause += 1

    except Exception as error:
        send_error_message(error)


def get_date_month():  # Получаем дату в формате dd.mm
    today = datetime.now()
    return today.strftime("%d.%m")


def happy_new_year():  # Поздравляем с Новогодними праздниками и Рождеством
    try:
        if get_date_month() == conf.NEW_YEAR:
            bot.send_photo(
                conf.CHAT_ID,
                get_path_photo(conf.NEW_YEAR_FILE),
                greet.GREETING_TITLE + "\n" + greet.NEW_YEAR_MSG_PART_1 + get_year() + greet.NEW_YEAR_MSG_PART_2,
            )
            return True
        elif get_date_month == conf.OLD_NEW_YEAR:
            bot.send_photo(conf.CHAT_ID, get_path_photo(conf.OLD_NEW_YEAR_FILE), greet.OLD_NEW_YEAR_MSG)
            return True
        elif get_date_month() == conf.CHRISTMAS:
            bot.send_photo(conf.CHAT_ID, get_path_photo(conf.CHRISTMAS_FILE), greet.CHRISTMAS)
            return True
        else:
            return False
    except Exception as error:
        send_error_message(error)


def greeting():  # Поздравляем с праздниками и именинников
    if not conf.SILENT_MODE:
        bot.send_message(conf.LOG_CHAT_ID, err.INFO_TITLE + "\n" + get_timestamp() + err.INFO_MSG_START)
    if happy_new_year():
        time.sleep(conf.SEND_INTERVAL)
        post_from_db()
    else:
        post_from_db()
    if not conf.SILENT_MODE:
        bot.send_message(conf.LOG_CHAT_ID, err.INFO_TITLE + "\n" + get_timestamp() + err.INFO_MSG_STOP)
