from scene_loader import BaseScene
from config import MESSAGE_KEYBOARD, alias_city

class Scene(BaseScene):
    def message_handler(self, event):
        text = event.object.text
        id = event.object.peer_id
        data = self.model.select().where(self.model.user_id == id).first()
        city_name = alias_city.get(text)
        if city_name in alias_city.values():
            data.city = city_name
            data.save()
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.keyboard_menu(), message=self.lang['settings_city_msg_f'].format(city=text), random_id=0)
        elif text == MESSAGE_KEYBOARD['back_keyb']:
            data.scens = 'settings'
            data.save()
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.keyboard_time(), message=self.lang['start_keyb_settings'], random_id=0)
