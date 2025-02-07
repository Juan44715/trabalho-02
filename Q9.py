def filtrar_tuplas():
    tuplas = []  

    while True:
        entrada = input('Digite uma tupla de números separados por vírgula (ex: 2,8) ou "finalizar" para encerrar o sistema: ')
        
        if entrada.lower() == 'finalizar':  
            break
        
        try:
            valores = tuple(map(int, entrada.split(','))) 
            tuplas.append(valores)  
        except ValueError:
            print('Por favor, digite apenas números separados por vírgula.')
    
    medias = list(map(lambda t: sum(t) / len(t), tuplas))
    
    resultado = list(filter(lambda t: sum(t) / len(t) > 5, tuplas))
    
    print(f'Tuplas filtradas: {resultado}')  

filtrar_tuplas()

