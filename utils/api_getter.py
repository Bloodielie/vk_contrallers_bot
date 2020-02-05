import requests

class ApiGetter:
    def __init__(self, short_url):
        self.url = short_url

    def get_data_bus(self, city: str, type_stop: str, type_transport: str = 'bus', transport_number: str = None, **kwargs):
        if not transport_number:
            url = f'{self.url}/{city}/{type_stop}'
        elif type_transport == 'trolleybuses':
            name_url = self.url.replace('bus', 'trolleybuses')
            url = f'{name_url}/{city}/{type_stop}/{transport_number}'
        else:
            url = f'{self.url}/{city}/{type_stop}/{transport_number}'
        if not kwargs:
            return self.dict_in_list(requests.get(url).json())
        for name, value in kwargs.items():
            url += f'{name}={str(value)}&'
        return self.dict_in_list(requests.get(url).json())

    @staticmethod
    def dict_in_list(date: dict):
        temporary_data = []
        for data in date.keys():
            inform = date.get(data)
            _tuple = (data, [inform[0], inform[1]])
            temporary_data.append(_tuple)
        return temporary_data
