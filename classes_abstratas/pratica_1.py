from abc import ABC, abstractmethod

class Console(ABC):
    
    @abstractmethod
    def ligar(self):
        ...

    @abstractmethod
    def desligar(self):
        ...
    
    @abstractmethod
    def __str__(self):
        ...

class Xbox(Console):
    def ligar(self):
        print('Ligando console...')

    def desligar(self):
        print('Desligando console...')
    
    def __str__(self):
        return "Info - XBOX SERIES X"

class Playstation(Console):
    def ligar(self):
        print('Ligando PS5...')

    def desligar(self):
        print('Desligando PS5...')
    
    def __str__(self):
        return "Info - PS5"

c1 = Xbox()
c1.ligar()
c1.desligar()

ps = Playstation()
print(ps)