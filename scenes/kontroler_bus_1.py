from scene_loader import BaseScene
from utils.mixin import mixin_konroler_bus_


class Scene(BaseScene):
    def message_handler(self, event):
        mixin_konroler_bus_(event, self.model, self.vk_bot, self.keyboard, self.lang)
