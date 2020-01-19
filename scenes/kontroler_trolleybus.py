from scene_loader import BaseScene
from config import MESSAGE_KEYBOARD
from utils.validation import check_bus
from config import SAVE_DEFAULT_TABLE_TROLLEYBUSES, DEFAULT_TABLE_BUS
from utils.mixin import mixin_kontoler_creater
import vk_api


class Scene(BaseScene):
    def message_handler(self, event):
        text = event.obj.text
        id = event.object.peer_id
        data = self.model.select().where(self.model.user_id == id).first()
        if text.isdigit() and int(text) in range(10):
            upload = vk_api.VkUpload(self.vk_bot)
            temporary_data = self.getter.get_data_bus(type='dirty', time=data.time, sort=data.sort)
            _data = check_bus(type_bus='trolleybuses', data=temporary_data, bus_number=text)
            mixin_kontoler_creater(self.vk_bot, event, data, _data, upload, DEFAULT_TABLE_BUS, SAVE_DEFAULT_TABLE_TROLLEYBUSES)
        elif text == MESSAGE_KEYBOARD['back_keyb']:
            data.scens = 'kontroler'
            data.save()
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.keyboard_controllers(), message=self.lang['kontroler_msg'], random_id=0)
