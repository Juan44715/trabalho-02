from functools import reduce  

def calc_media():
    alunos = {}  

    while True:
        entrada = input('Digite o nome do aluno e as notas com pesos (ex: João 8,9,10,2) ou "finalizar" para encerrar o sistema: ')
        
        if entrada.lower() == 'finalizar':  
            break
        
        try:
            partes = entrada.split()
            nome = partes[0]  
            notas = list(map(float, partes[1:]))  

            if len(notas) < 2:
                print('Digite pelo menos uma nota e um peso.')
                continue
            
            alunos[nome] = notas  
        except ValueError:
            print('Formato inválido. Use nome seguido das notas e peso.')

    def calc_media_notas(notas):
        if len(notas) < 2:
            return 0  
        
        pesos = notas[-1]  
        return reduce(lambda x, y: x + y, notas[:-1]) / pesos  

    medias = {aluno: calc_media_notas(notas) for aluno, notas in alunos.items()}  
    
    print(f'Médias ponderadas: {medias}')  

calc_media()
