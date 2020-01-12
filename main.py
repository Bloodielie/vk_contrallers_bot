#!/usr/bin/python
# -*- coding: utf-8 -*-
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import token, BOT_GROUP_ID, login, password, start_msg, wait_json_write
from keyboard import Keyboard
from time import sleep
from utils.write_data_json import write_dirty_post, write_clean_post
import threading
from database import User
from scene_loader import Loader
from config import MESSAGE, MESSAGE_KEYBOARD
import logging

logging.basicConfig(filename="error.log", format='\n%(asctime)s - %(name)s - %(levelname)s - %(message)s')


vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, BOT_GROUP_ID)
vk_bot = vk_session.get_api()

vk = vk_api.VkApi(login=login, password=password)
vk.auth()

load = Loader()
keyboard = Keyboard()


def main_function():
    """ основной функционал """
    while True:
        try:
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    id = event.object.peer_id
                    text = event.obj.text
                    data = User.select().where(User.user_id == id).first()
                    if not data:
                        User.create(user_id=id)
                    if text.lower() in start_msg:
                        """ отвечает за начало диалога с юзером """
                        data.scens = "kontroler"
                        data.save()
                        vk_bot.messages.send(peer_id=event.object.peer_id, message=MESSAGE['start_msg'], keyboard=keyboard.keyboard_menu(),
                                             random_id=0)
                    elif text == MESSAGE_KEYBOARD['start_keyb_kontroler']:
                        """ Кнопка контролеров """
                        data.scens = "kontroler"
                        data.save()
                        vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=keyboard.keyboard_controllers(), message=MESSAGE["kontroler_msg"],
                                             random_id=0)
                    elif text == MESSAGE_KEYBOARD['start_keyb_settings']:
                        """ Кнопка настройки комманд """
                        data.scens = "settings"
                        data.save()
                        vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=keyboard.keyboard_help(), message=MESSAGE["settings_msg"],
                                             random_id=0)
                    elif text == MESSAGE_KEYBOARD['menu_keyb']:
                        vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=keyboard.keyboard_menu(), message=MESSAGE["menu_msg"],
                                             random_id=0)

                    scene = data.scens
                    load.init_scene(scene, vk_bot, keyboard, MESSAGE, User).message_handler(event)
        except Exception as e:
            logging.error("Exception", exc_info=True)
            print(e)
            continue


def write_in_json_file():
    """ Запись данных во 2 файл """
    while True:
        write_dirty_post(vk)
        write_clean_post(vk)
        sleep(wait_json_write)


my_thread_1 = threading.Thread(target=main_function)
my_thread_2 = threading.Thread(target=write_in_json_file)

my_thread_1.start()
my_thread_2.start()
