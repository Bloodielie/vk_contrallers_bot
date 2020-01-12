from scene_loader import BaseScene
from config import MESSAGE_KEYBOARD


class Scene(BaseScene):
    def message_handler(self, event):
        text = event.object.text
        id = event.object.peer_id
        if text == MESSAGE_KEYBOARD['settings_keyb_time']:
            data = self.model.select().where(self.model.user_id == id).first()
            data.scens = 'settings_time'
            data.save()
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.keyboard_time(), message=self.lang['settings_time_msg'], random_id=0)
        elif text == MESSAGE_KEYBOARD['settings_keyb_display']:
            data = self.model.select().where(self.model.user_id == id).first()
            data.scens = 'settings_display'
            data.save()
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.keyboard_display(), message=self.lang['settings_display_msg'], random_id=0)
        elif text == MESSAGE_KEYBOARD['settings_keyb_sort']:
            data = self.model.select().where(self.model.user_id == id).first()
            data.scens = 'settings_sort'
            data.save()
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.keyboard_sort(), message=self.lang['settings_sort_msg'], random_id=0)
        elif text == MESSAGE_KEYBOARD['back_keyb']:
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.keyboard_help(), message=self.lang['menu_msg'], random_id=0)
