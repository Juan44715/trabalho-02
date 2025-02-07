'''Crie uma função que, utilizando reduce e uma função lambda, receba uma lista de
números inteiros e retorne a soma total dos números.
Exemplo de entrada: [1, 2, 3, 4]
Exemplo de saída: 10'''
from functools import reduce
def somar_valores ():
    num = []
    while True:
        try:
            numero = input('Digite um numero para adicionar à lista ou "finalizar" para somar os numeros: ')
            if numero.lower() == 'finalizar':
                break
            num.append(float(numero))
        except ValueError:
            print('Por favor,digite um numero valido')
        # NÃO USA LIST E REDUCE JUNTO     
    soma = reduce(lambda x, y: x + y, num)
    if soma:
        print(f'A soma total de todos os numeros da lista é: {soma}')
    else:
        print('não há soma')
somar_valores()