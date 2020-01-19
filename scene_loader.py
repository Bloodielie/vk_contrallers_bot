import os
import importlib.util


class BaseScene:
    def __init__(self, vk_bot, keyboard, lang: dict, model_db, getter):
        self.vk_bot = vk_bot
        self.lang = lang
        self.keyboard = keyboard
        self.model = model_db
        self. getter = getter

    async def message_handler(self, event):
        pass


class Loader:
    def __init__(self):
        self.scenes = self.load_scenes()

    def get_scene_by_name(self, scene_name):
        for scene in self.scenes:
            if scene.__module__ == scene_name:
                return scene

    def load_scenes(self):
        scenes = []
        files = [x.replace(".py", "") for x in os.listdir("scenes") if x not in ["__pycache__", "__init__.py"]]
        for file in files:
            scene = self.load_scene(file)
            scene_class = getattr(scene, "Scene")
            scenes.append(scene_class)
        return scenes

    @staticmethod
    def load_scene(file_name):
        spec = importlib.util.spec_from_file_location(file_name, os.path.abspath(f"scenes/{file_name}.py"))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def init_scene(self, scene_name, vk_bot, keyboard, lang, model_db, getter):
        scene = self.get_scene_by_name(scene_name)
        initialized_scene = scene(vk_bot=vk_bot, keyboard=keyboard, lang=lang, model_db=model_db, getter=getter)
        return initialized_scene
