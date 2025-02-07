'''Escreva uma função que, utilizando map e uma função lambda, receba uma lista
de números inteiros e retorne uma nova lista com todos os elementos dobrados.
Exemplo de entrada: [1, 2, Exemplo de saída: [2, 4, 6, 8]'''

num = [float(input("Digite o numero a ser dobrado: "))]
dobrado = list(map(lambda x: x * 2, num))
print(f'O dobro de {num} é {dobrado}')