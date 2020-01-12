from scene_loader import BaseScene
from config import MESSAGE_KEYBOARD
from utils.utils import deconverting_time, converting_time


class Scene(BaseScene):
    def message_handler(self, event):
        text = event.obj.text
        id = event.object.peer_id
        data = self.model.select().where(self.model.user_id == id).first()
        if deconverting_time(text) in range(21601):
            times = deconverting_time(text)
            data.time = times
            data.save()
            final_time = converting_time(times)
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.keyboard_menu(), message=self.lang['settings_time_inside_msg'].format(final_time=final_time), random_id=0)
        elif text == MESSAGE_KEYBOARD['back_keyb']:
            data.scens = 'settings'
            data.save()
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.se(), message=self.lang['start_keyb_settings'], random_id=0)
