from .utils import create_attachment, text_display
from config import SAVE_DEFAULT_TABLE_BUS, DEFAULT_TABLE_BUS, FONT_PNG, bus_number, MESSAGE_KEYBOARD
from .validation import check_bus
from .pil import img_busstop
import vk_api


def mixin_konroler_bus_(event, model, vk_bot, keyboard, lang, getter):
    text = event.obj.text
    id = event.object.peer_id
    data = model.select().where(model.user_id == id).first()
    if text in bus_number:
        upload = vk_api.VkUpload(vk_bot)
        temporary_data = getter.get_data_bus(type='dirty', time=data.time, sort=data.sort)
        _data = check_bus(type_bus='bus', data=temporary_data, bus_number=text)
        mixin_kontoler_creater(vk_bot, event, data, _data, upload, DEFAULT_TABLE_BUS, SAVE_DEFAULT_TABLE_BUS)
    elif text == MESSAGE_KEYBOARD['back_keyb']:
        data.scens = 'kontroler_bus'
        data.save()
        vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=keyboard.keyboard_bus(), message=lang['menu_msg'], random_id=0)


def mixin_kontoler_creater(vk_bot, event, data, temporary_data, upload, DEFAULT_TABLE, SAVE_DEFAULT_TABLE):
    if data.display == 'Фото':
        img_busstop(name_png=SAVE_DEFAULT_TABLE, _dict=temporary_data, cordinates_x=(60, 650, 1250), cordinate_y=45, y_step=92,
                    color=(34, 34, 34), font=FONT_PNG, name_png_first=DEFAULT_TABLE)
        vk_bot.messages.send(peer_id=event.object.peer_id, random_id=0, attachment=create_attachment(upload, SAVE_DEFAULT_TABLE))
    else:
        text = text_display(temporary_data)
        vk_bot.messages.send(peer_id=event.object.peer_id, random_id=0, message=text)
