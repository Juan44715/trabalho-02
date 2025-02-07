'''Escreva uma função que, utilizando filter e uma função lambda, receba uma lista
de números inteiros e retorne apenas os números pares.
Exemplo de entrada: [1, 2, 3, 4, 5]
Exemplo de saída: [2, 4]'''

def num_pares ():
    num = []
    while True:
        try:
            numero = input('Digite um numero para adicionar à lista ou "finalizar" para achar os numeros pares: ')
            if numero.lower() == 'finalizar':
                break
            num.append(int(numero))
            #NÃO ESQUECE O EXCEPT
        except ValueError:
            print('Por favor,digite um numero valido')
            
    pares = list(filter(lambda x: x % 2 == 0, num))
    if pares:
        print(f'Os numeros pares da lista são: {pares}')
    else:
        print('Não há numeros pares na lista')
        #NÃO ESQUECE DE CHAMAR A FUNÇÃO NO FINAL, SE N NÃO FUNCIONA
num_pares() 