from scene_loader import BaseScene
from config import MESSAGE_KEYBOARD


class Scene(BaseScene):
    def message_handler(self, event):
        text = event.obj.text
        id = event.object.peer_id
        data = self.model.select().where(self.model.user_id == id).first()
        if text == 'Автобусы 1 стр[1-15Б]':
            data.scens = 'kontroler_bus_1'
            data.save()
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.keyboard_bus_1(), message='Автобусы 1 стр[1-15Б]', random_id=0)
        elif text == 'Автобусы 2 стр[15В-28]':
            data.scens = 'kontroler_bus_2'
            data.save()
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.keyboard_bus_2(), message='Автобусы 2 стр[15В-28]', random_id=0)
        elif text == 'Автобусы 3 стр[29-44]':
            data.scens = 'kontroler_bus_3'
            data.save()
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.keyboard_bus_3(), message='Автобусы 3 стр[29-44]', random_id=0)
        elif text == 'Автобусы 4 стр[44А-50]':
            data.scens = 'kontroler_bus_4'
            data.save()
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.keyboard_bus_4(), message='Автобусы 4 стр[44А-50]', random_id=0)
        elif text == MESSAGE_KEYBOARD['back_keyb']:
            data.scens = 'kontroler'
            data.save()
            self.vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=self.keyboard.keyboard_controllers(), message='Автобусы', random_id=0)
