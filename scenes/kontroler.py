from scene_loader import BaseScene
from config import MESSAGE_KEYBOARD
from config import SAVE_DEFAULT_TABLE, DEFAULT_TABLE
from utils.mixin import mixin_kontoler_creater
import vk_api


class Scene(BaseScene):
    def message_handler(self, event):
        text = event.obj.text
        id = event.object.peer_id
        data = self.model.select().where(self.model.user_id == id).first()
        upload = vk_api.VkUpload(self.vk_bot)
        if text == MESSAGE_KEYBOARD['kontroler_keyb_clear_stop']:
            temporary_data = self.getter.get_data_bus(type='clean', time=data.time, sort=data.sort)
            mixin_kontoler_creater(self.vk_bot, event, data, temporary_data, upload, DEFAULT_TABLE, SAVE_DEFAULT_TABLE)
        elif text == MESSAGE_KEYBOARD['kontroler_keyb_dirty_stop']:
            temporary_data = self.getter.get_data_bus(type='dirty', time=data.time, sort=data.sort)
            mixin_kontoler_creater(self.vk_bot, event, data, temporary_data, upload, DEFAULT_TABLE, SAVE_DEFAULT_TABLE)
        elif text == MESSAGE_KEYBOARD['kontroler_keyb_bus']:
            data.scens = 'kontroler_bus'
            data.save()
            self.vk_bot.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=self.keyboard.keyboard_bus(), message=self.lang['kontroler_bus_msg'])
        elif text == MESSAGE_KEYBOARD['kontroler_keyb_trolleybus']:
            data.scens = 'kontroler_trolleybus'
            data.save()
            self.vk_bot.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=self.keyboard.keyboard_trolley_buses(), message=self.lang['kontroler_trolleubus_msg'])
        elif text == MESSAGE_KEYBOARD['back_keyb']:
            data.scens = 'kontroler'
            data.save()
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.keyboard_menu(), message=self.lang['menu_msg'], random_id=0)
