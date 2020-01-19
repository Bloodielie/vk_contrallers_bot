from scene_loader import BaseScene
from config import MESSAGE_KEYBOARD


class Scene(BaseScene):
    def message_handler(self, event):
        text = event.obj.text
        id = event.object.peer_id
        data = self.model.select().where(self.model.user_id == id).first()
        if text == MESSAGE_KEYBOARD['settings_keyb_display_inside_1']:
            data.display = 'Фото'
            data.save()
            msg_prefix = "картинкой"
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.keyboard_menu(), message=self.lang['settings_display_inside_msg'].format(display=msg_prefix), random_id=0)
        elif text == 'Текст':
            data.display = 'Сообщение'
            data.save()
            msg_prefix = "текстом"
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.keyboard_menu(), message=self.lang['settings_display_inside_msg'].format(display=msg_prefix), random_id=0)
        elif text == MESSAGE_KEYBOARD['back_keyb']:
            data.scens = 'settings'
            data.save()
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.keyboard_time(), message=self.lang['start_keyb_settings'], random_id=0)
