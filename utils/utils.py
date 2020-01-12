from time import time


class BusStopGet:
    def __init__(self, vk):
        self.vk = vk

    def get_post(self, time_back_hours=7200, count=100, group_id=72869598):
        # Функция получающая посты со стены сообщества за указанное время(можно коректировать количество постов для проверки)
        wall = self.vk.method('wall.get', values={'owner_id': -group_id, 'count': count})
        for i in wall['items']:
            hours_now = int(i['date'])
            hours_back = int(time()) - time_back_hours
            if hours_now >= hours_back:
                temporary_tuple = (i['text'].lower(), i['date'])
                yield temporary_tuple

    def get_post_un_time(self, count=100, group_id=72869598):
        """ Получения постов """
        wall = self.vk.method('wall.get', values={'owner_id': -group_id, 'count': count})
        for i in wall['items']:
            temporary_tuple = (i['text'].lower(), i['date'])
            yield temporary_tuple


def create_attachment(vk_upload, path_content, type_content='photo'):
    """ Создание ссылки для отправки attachment """
    photo = vk_upload.photo_messages(path_content)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    return f'{type_content}{owner_id}_{photo_id}_{access_key}'


def converting_time(sec_time: int):
    """ Добавления правильного окончания для времени """
    hours = sec_time // 3600
    minutes = None
    if sec_time % 3600 == 0.0:
        pass
    else:
        minutes = int((sec_time - hours * 3600) / 60)

    if hours == 1:
        hours_prefix = "час"
    else:
        hours_prefix = "часа"

    min_prefix = "минут"
    if hours == 0:
        return f'{minutes} {min_prefix}'
    elif minutes:
        return f'{hours} {hours_prefix} {minutes} {min_prefix}'
    else:
        return f'{hours} {hours_prefix}'


def deconverting_time(time: str):
    """ Декодирование окончания в секунды """
    _str = time.split()
    sec = 0
    if len(_str) == 2:
        if _str[1] == "час":
            sec += 3600
        elif _str[1] == "часа":
            if len(_str) == 2:
                sec += int(_str[0]) * 3600
        elif _str[1] == "мин":
            sec = 1800
    else:
        sec += (int(_str[0]) * 3600) + 1800
    return sec


def text_display(data: dict):
    """ Представление словаря в тексте """
    text = '\n'.join([f'{stop[0]}, {stop[1][0]}, {stop[1][1]}' for stop in data])
    if text:
        return text
    else:
        return 'Остутствуют сообщения людей.'
