lista1 = []
lista2 = []
contador = 0

while contador < 2:
    print('\033[33m')
    print('\033[4m Digite >"pare"< para sair') 
    print('\033[0m', '\033[1m')
    
    
    mercado = input('O que você vai comprar no mercado? ')
    print('\033[31m')
    lista1.append(mercado)
    if not mercado == 'pare':
        print(lista1)
  
    if mercado == 'pare':
        break
    
lista1.remove('pare')
      
print('Sua lista dor mercado >', lista1)

while contador < 2:
    print('\033[33m')
    print('\033[4m Digite "pare" para sair') 
    print('\033[0m', '\033[1m')
    
    farmacia = input('O que você vai comprar na farmacia? ')
    print('\033[32m')
    lista2.append(farmacia)
    if not farmacia == 'pare':
        print(lista2)
  
    if farmacia == 'pare':
        break
    
lista2.remove('pare')
      
print('Sua lista da farmácia >', lista2)
print('\033[1;35m')
print('Sua lista completa >', lista1 + lista2 )
print('\033[0m')


    
        

    
  
    
    