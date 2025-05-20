class MyError(Exception):
    ...

class OtherError(Exception):
    ...

def levantar():
    exception_ = MyError('A', 'B', 'C')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('Você errou isso')
    raise exception_

try:
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OtherError('Vou lançar de novo')
    exception_.__notes__ += error.__notes__.copy()
    exception_.add_note('Mais uma nota')
    raise exception_ from error
