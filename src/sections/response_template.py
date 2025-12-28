class ManualEntryResponse:
    def __init__(self):
        pass

    def setter(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                getattr(self, key).set_value(value)

    def get_all(self):
        data = {}
        for key in self.__dict__.keys():
            attr = getattr(self, key)
            data[attr.title] = attr.value
        return data



class UploadedEntryResponse:
    def __init__(self):
        pass

    def setter(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def get_all(self):
        data = {}
        for key in self.__dict__.keys():
            value = getattr(self, key)
            data[key] = value
        return data