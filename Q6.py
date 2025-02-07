def classificar_pares_impares():
    numeros = []  

    while True:
        entrada = input('Digite um número para adicionar à lista ou "finalizar" para classificar os números: ')
        
        if entrada.lower() == 'finalizar':  
            break
        
        if not entrada.lstrip('-').isdigit():  
            print('Por favor, digite um número válido.')
            continue 
        
        numeros.append(int(entrada))  
    

    pares = list(filter(lambda x: x % 2 == 0, numeros))
    impares = list(filter(lambda x: x % 2 != 0, numeros))
    

    resultado = {"pares": pares, "ímpares": impares}
    
    print(f'Resultado: {resultado}')  


classificar_pares_impares() #NÃO esquecer de chamar a função de novo
