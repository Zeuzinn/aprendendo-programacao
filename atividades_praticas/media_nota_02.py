def obter_nota(contador):
    while True:
        try:
            nota = float(input(f"Nota {contador + 1}: "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota deve ser entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


def calcular_media(notas):
    return sum(notas) / len(notas)


def exibir_resultado(media):
    print(f"Média: {media:.1f}")
    if media >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado.")


def calculadora_media():
    notas = []
    for i in range(3):
        notas.append(obter_nota(i))

    media = calcular_media(notas)
    exibir_resultado(media)


calculadora_media()