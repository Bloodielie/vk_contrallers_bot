from scene_loader import BaseScene
from config import MESSAGE_KEYBOARD
from utils.validation import temporary_list, BusStopCheck
from config import JSON_BUS_STOP, FONT_PNG, SAVE_DEFAULT_TABLE, DEFAULT_TABLE, JSON_BUS_STOP_CLEAN
from utils.pil import img_busstop
from utils.utils import create_attachment, text_display
import vk_api


class Scene(BaseScene):
    def message_handler(self, event):
        text = event.obj.text
        id = event.object.peer_id
        data = self.model.select().where(self.model.user_id == id).first()
        bus_check = BusStopCheck()
        upload = vk_api.VkUpload(self.vk_bot)
        if text == MESSAGE_KEYBOARD['kontroler_keyb_clear_stop']:
            information_busstop = temporary_list(time_=data.time, path_file=JSON_BUS_STOP_CLEAN)
            temporary_data = bus_check.sort_busstop(information_busstop, _sort=data.sort)
            if data.display == 'Фото':
                img_busstop(name_png=SAVE_DEFAULT_TABLE, _dict=temporary_data, cordinates_x=(60, 650, 1250), cordinate_y=45, y_step=92,
                            color=(34, 34, 34), font=FONT_PNG, name_png_first=DEFAULT_TABLE)
                self.vk_bot.messages.send(peer_id=event.object.peer_id, random_id=0,
                                          attachment=create_attachment(upload, SAVE_DEFAULT_TABLE))
            else:
                text = text_display(temporary_data)
                self.vk_bot.messages.send(peer_id=event.object.peer_id, random_id=0, message=text)
        elif text == MESSAGE_KEYBOARD['kontroler_keyb_dirty_stop']:
            information_busstop = temporary_list(time_=data.time, path_file=JSON_BUS_STOP)
            temporary_data = bus_check.sort_busstop(information_busstop, _sort=data.sort)
            if data.display == 'Фото':
                img_busstop(name_png=SAVE_DEFAULT_TABLE, _dict=temporary_data, cordinates_x=(60, 650, 1250), cordinate_y=45, y_step=92,
                            color=(34, 34, 34), font=FONT_PNG, name_png_first=DEFAULT_TABLE)
                self.vk_bot.messages.send(peer_id=event.object.peer_id, random_id=0,
                                          attachment=create_attachment(upload, SAVE_DEFAULT_TABLE))
            else:
                text = text_display(temporary_data)
                self.vk_bot.messages.send(peer_id=event.object.peer_id, random_id=0, message=text)
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
