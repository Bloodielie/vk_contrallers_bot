import requests


class ApiGetter:
    def __init__(self, short_url):
        self.url = short_url

    def get_data_bus(self, type: str, **kwargs):
        url = f'{self.url}/{type}?'
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
