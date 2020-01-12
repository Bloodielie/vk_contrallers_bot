from .utils import create_attachment, text_display
from config import SAVE_DEFAULT_TABLE_BUS, DEFAULT_TABLE_BUS, FONT_PNG, JSON_BUS_STOP, bus_number, MESSAGE_KEYBOARD
from .validation import BusStopCheck, temporary_list, check_bus
from .pil import img_busstop
import vk_api


def mixin_konroler_bus_(event, model, vk_bot, keyboard, lang):
    text = event.obj.text
    id = event.object.peer_id
    data = model.select().where(model.user_id == id).first()
    if text in bus_number:
        upload = vk_api.VkUpload(vk_bot)
        bus_check = BusStopCheck()
        temporary_data = temporary_list(time_=data.time, path_file=JSON_BUS_STOP)
        _data = bus_check.sort_busstop(check_bus(type_bus='bus', data=temporary_data, bus_number=text), _sort=data.sort)
        if data.display == 'Фото':
            img_busstop(name_png=SAVE_DEFAULT_TABLE_BUS, _dict=_data, cordinates_x=(60, 650, 1250), cordinate_y=45, y_step=92,
                        color=(34, 34, 34), font=FONT_PNG, name_png_first=DEFAULT_TABLE_BUS)
            vk_bot.messages.send(peer_id=event.object.peer_id, random_id=0,
                                      attachment=create_attachment(upload, SAVE_DEFAULT_TABLE_BUS))
        else:
            text = text_display(_data)
            vk_bot.messages.send(peer_id=event.object.peer_id, random_id=0, message=text)
    elif text == MESSAGE_KEYBOARD['back_keyb']:
        data.scens = 'kontroler_bus'
        data.save()
        vk_bot.messages.send(peer_id=event.object.peer_id, keyboard=keyboard.keyboard_bus(), message=lang['menu_msg'], random_id=0)

