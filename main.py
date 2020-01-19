#!/usr/bin/python
# -*- coding: utf-8 -*-
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import token, BOT_GROUP_ID, login, password, start_msg
from keyboard import Keyboard
from database import User
from scene_loader import Loader
from config import MESSAGE, MESSAGE_KEYBOARD
import logging
from utils.api_getter import ApiGetter

logging.basicConfig(filename="error.log", format='\n%(asctime)s - %(name)s - %(levelname)s - %(message)s')


vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, BOT_GROUP_ID)
vk_bot = vk_session.get_api()

vk = vk_api.VkApi(login=login, password=password)
vk.auth()

load = Loader()
keyboard = Keyboard()
getter_data = ApiGetter('http://127.0.0.1:8000/bus_stop')


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
                    elif text == MESSAGE_KEYBOARD['start_keyb_info']:
                        vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=keyboard.keyboard_menu(), message=MESSAGE["info_msg"],
                                             random_id=0)
                    elif text == MESSAGE_KEYBOARD['menu_keyb']:
                        vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=keyboard.keyboard_menu(), message=MESSAGE["menu_msg"],
                                             random_id=0)

                    scene = data.scens
                    load.init_scene(scene, vk_bot, keyboard, MESSAGE, User, getter_data).message_handler(event)
        except Exception as e:
            logging.error("Exception", exc_info=True)
            print(e)
            continue


if __name__ == '__main__':
    main_function()
