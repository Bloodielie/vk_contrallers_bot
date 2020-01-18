from scene_loader import BaseScene
from config import MESSAGE_KEYBOARD
from utils.validation import check_bus
from config import FONT_PNG, SAVE_DEFAULT_TABLE_TROLLEYBUSES, DEFAULT_TABLE_BUS
from utils.pil import img_busstop
from utils.utils import create_attachment, text_display
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
            if data.display == 'Фото':
                img_busstop(name_png=SAVE_DEFAULT_TABLE_TROLLEYBUSES, _dict=_data, cordinates_x=(60, 650, 1250), cordinate_y=45, y_step=92,
                            color=(34, 34, 34), font=FONT_PNG, name_png_first=DEFAULT_TABLE_BUS)
                self.vk_bot.messages.send(peer_id=event.object.peer_id, random_id=0,
                                          attachment=create_attachment(upload, SAVE_DEFAULT_TABLE_TROLLEYBUSES))
            else:
                text = text_display(temporary_data)
                self.vk_bot.messages.send(peer_id=event.object.peer_id, random_id=0, message=text)
        elif text == MESSAGE_KEYBOARD['back_keyb']:
            data.scens = 'kontroler'
            data.save()
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.keyboard_controllers(), message=self.lang['kontroler_msg'], random_id=0)
