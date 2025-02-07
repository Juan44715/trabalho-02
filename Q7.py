def classificar_numeros():
    numeros = []  # Lista para armazenar os números fornecidos pelo usuário

    while True:
        entrada = input('Digite um número para adicionar à lista ou "finalizar" para classificar: ')
        
        if entrada.lower() == 'finalizar':  
            break
        
        if not entrada.lstrip('-').isdigit():  # Valida números inteiros (positivos e negativos)
            print('Por favor, digite um número válido.')
            continue 
        
        numeros.append(int(entrada))  
    
    positivos = list(filter(lambda x: x > 0, numeros))
    negativos = list(filter(lambda x: x < 0, numeros))
    zeros = list(filter(lambda x: x == 0, numeros))
    
    resultado = {"positivos": positivos, "negativos": negativos, "zeros": zeros}
    
    print(f'Resultado: {resultado}')  

classificar_numeros() 