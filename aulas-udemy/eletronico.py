from uso_log import LogFileMixin

class Eletronico:
    def __init__(self,nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True
            
    def ligar(self):
        if self._ligado:
            self._ligado = False


class Smarthphone(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()
 
        if self._ligado:
            msg = f'{self._nome} esta ligado'
            self.log_success(msg)
 
    def desligar(self):
        super().desligar()
        if not self._ligado:
            msg = f'{self._nome} esta Desligado'
            self.log_success(msg)

            