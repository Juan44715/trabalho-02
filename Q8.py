from functools import reduce  #tentar usar reduce sem importar primeiro fica dificil ne

def contar_letras():
    palavras = []  

    while True:
        entrada = input('Digite uma palavra ou "finalizar" para contar as letras: ')
        
        if entrada.lower() == 'finalizar':  
            break
        
        if not entrada.isalpha():  #ISALPHA PRA DEIXAR SO LETRA
            print('Por favor, digite apenas palavras.')
            continue 
        
        palavras.append(entrada)  
    

    tamanhos = list(map(lambda palavra: len(palavra), palavras))
    

    total_letras = reduce(lambda x, y: x + y, tamanhos, 0)
    
    print(f'Total de letras: {total_letras}')  

contar_letras() #esquecer toda vez de chamar a função é burrice ja