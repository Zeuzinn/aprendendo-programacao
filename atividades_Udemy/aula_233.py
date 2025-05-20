class MyError(Exception):
    ...

# 'Exception' funciona como qualquer erro em Python (ValueError, ZeroDivisionError, etc.)
# mas com nome e comportamento próprios se você quiser adicionar.

class OterError(Exception):
    ...

def levantar():  # Cria uma instância da exceção 'MyError'
    exception_ = MyError('A', 'B', 'C')
    raise exception_   # Lança 'raise' essa exceção.

try:
    levantar()  
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OterError('Vou lançar de novo')  # Cria uma nova exceção do tipo 'OterError'
    raise exception_ from error  
    # Usa 'raise' para relançar esse novo erro,
    # mas indicando que ele foi causado pela exceção anterior
