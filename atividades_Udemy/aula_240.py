class MyReprMixim:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} ({class_dict})'
        return class_repr


class Time(MyReprMixim):
    def __init__(self, nome):
        self.nome = nome


class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
argentina = Time ('Argentina')

venus = Planeta ('Vênus')
terra = Planeta ('Terra')
