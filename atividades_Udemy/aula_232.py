from abc import ABC, abstractmethod

class Notificacao(ABC):
    # Notificacao herda de ABC, ou seja, é uma classe abstrata.
    def __init__(self, mensagem):
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self) -> bool:...   
    # 'bool' indica que o método deve retornar um booleano 'True' ou 'False' 
    # O método 'enviar' é abstrato. 
    # Toda subclasse é obrigada a implementar esse método.
    

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail : enviando -', self.mensagem)
        return True
    # Mostra a mensagem e retorna 'True' indicando que a notificação foi enviada com sucesso.
        

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS : enviando -', self.mensagem)
        return False
    # Mostra a mensagem e retorna 'False' indicando que a notificação não foi enviada .


def notificar(notificacao: Notificacao): 
    # Essa função recebe um objeto do tipo 'Notificacao' (ou qualquer subclasse dela)
    notificacao_enviada = notificacao.enviar()  
    # Chama o método 'enviar()'
    # Verifica se o retorno é 'True' ou 'False'.

    if notificacao_enviada:
        print('Notificação enviada')
    else:    
        print('Notificação não enviada')


notificacao_email = NotificacaoEmail('Testando E-MAIL')
notificar(notificacao_email)
notificacao_sms = NotificacaoSMS('Testando SMS')
notificar(notificacao_sms)