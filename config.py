from utils.json import JsonUtils

login = ''
password = ''
token = ''
BOT_GROUP_ID =

db_name = 'controller_base_vk'
user = 'postgres'
host = 'localhost'
password_db = 

MEMBER_path = 'json/member.json'

SAVE_DEFAULT_TABLE = 'png/table.gif'
SAVE_DEFAULT_TABLE_CLEAR = 'png/tableclear.gif'
DEFAULT_TABLE = 'png/таблица.png'

DEFAULT_TABLE_BUS = 'png/таблицадляавтобуса.png'
SAVE_DEFAULT_TABLE_BUS = 'png/tablebus.gif'
SAVE_DEFAULT_TABLE_TROLLEYBUSES = 'png/tabletrolleybuses.png'

JSON_BUS = 'json/busstop.json'
JSON_TROLLEYBUSES = 'json/trolleybusesstop.json'

FONT_PNG = 'font/impact.ttf'

STOP = 'json/stopbus.json'
stop_bus = JsonUtils(STOP).get_json()

start_msg = ["старт", "го", "поехали", "начать", "запуск", "пуск"]

MESSAGE = {
    "start_msg": 'Привет! Я Контролер бот для г.Брест.\n Использую клавиатуру ниже чтобы использовать меня.',
    "kontroler_msg": 'Контроллеры.',
    "settings_msg": 'Доступные настройки.',
    "menu_msg": 'Главное меню.',
    "kontroler_bus_msg": "Автобусы",
    "kontroler_trolleubus_msg": "Троллейбусы",
    "settings_sort_msg": "Настройка сортировки постов.",
    "settings_sort_inside_msg": "Теперь сообщения сортируются по {msg_pref}",
    "settings_display_msg": 'Настройка отображения постов.',
    "settings_display_inside_msg": 'Теперь информация отображается {display}',
    "settings_time_msg": 'Настройка времени получения постов.',
    "settings_time_inside_msg": 'Время отборки постов изменено на {final_time}',
    'info_msg': 'Бот для отслеживать контроллеров в г.Бресте.\nПочти точно такой же бот в Telegram:\nhttps://t.me/anticontrollersbot'
}

MESSAGE_KEYBOARD = {
    'back_keyb': 'Назад',
    'menu_keyb': 'Меню',
    'start_keyb_kontroler': 'Контроллеры',
    'start_keyb_settings': 'Настройки',
    'start_keyb_info': 'Информация',
    'kontroler_keyb_clear_stop': 'Чистые остановки',
    'kontroler_keyb_dirty_stop': 'Грязные остановки',
    'kontroler_keyb_bus': 'Автобусы',
    'kontroler_keyb_bus_1': 'Автобусы 1 стр[1-15Б]',
    'kontroler_keyb_bus_2': 'Автобусы 2 стр[15В-28]',
    'kontroler_keyb_bus_3': 'Автобусы 3 стр[29-44]',
    'kontroler_keyb_bus_4': 'Автобусы 4 стр[44А-50]',
    'kontroler_keyb_trolleybus': 'Троллейбусы',
    'settings_keyb_time': 'Время',
    'settings_keyb_display': 'Отображение',
    'settings_keyb_display_inside_1': 'Фото',
    'settings_keyb_display_inside_2': 'Текст',
    'settings_keyb_sort': 'Сортировка',
    'settings_keyb_sort_inside_1': 'Время',
    'settings_keyb_sort_inside_2': 'Сообщения',
}

bus_number = ['1', '1А', '2', '2А', '3', '4', '5', '6', '7', '8', '9', '10', '11', '11А', '12', '12А', '13', '13А', '14', '15', '15А', '15Б', '16', '17', '18', '19', '20', '21', '21А', '21Б', '22', '23', '23А', '23Б', '24', '24А', '25', '26', '27', '27А', '28', '29', '30', '30А', '31', '32', '33', '34', '35', '36', '37', '37А', '38', '39', '39А', '39Б', '40', '41', '42', '43', '44', '44А', '45', '46', '47', '50']

