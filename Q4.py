'''Escreva uma função que receba uma lista de nomes e, utilizando filter, retorne
apenas os nomes com mais de 5 letras.
Exemplo de entrada: ["Ana", "Lucas", "Fernanda", "João"]
Exemplo de saída: ["Lucas", "Fernanda"]'''

def nomes_grandes ():
    name = []
    while True:
        nomes = input('Digite um nome para adicionar à lista ou "finalizar" para checar os nomes com mais de 5 letras: ')
        if nomes.lower() == 'finalizar':
            break
            # ISALPHA IMPEDE QUE O USUARIO COLOQUE NUMEROS OU CARACTERES ESPECIAIS NO NOME
        if not nomes.isalpha():
            print('Por favor, digite apenas letras.')
            continue
        name.append(nomes)
        
    nomes5 = list(filter(lambda nome: len(nome) > 5, name))
    print(f'Os nomes com mais de 5 letras são: {nomes5}')
nomes_grandes()