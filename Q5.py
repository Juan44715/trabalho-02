def ord_num():
  num = []
  while True:
    try:
      entrada = input('Digite os numeros a serem colocados na lista ou digite "finalizar" para calcular os resultados: ')
      
      if entrada.lower() == 'finalizar':
        break
      if not entrada.isdigit():
        print('por favor, insira apenas numeros')
        continue
      
      numeros = int(entrada)
      num.append(numeros)
    except ValueError:
      print('Por favor, insira um numero valido')
  ordenado = sorted(num)
  print(f'Os numeros quadrados ordenados na lista são: {ordenado}')
ord_num()