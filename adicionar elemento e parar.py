lista = []
contador = 0
print('\033[1m')
print('\033[33m Digite ">pare"< para sair \033[0m')

while contador < 2:

    print('\033[1m')
    
    sacolao = input('Digite o que você vai comprar na feira > ')
    lista.append(sacolao)
    print()
    
    if sacolao == 'pare':
        break
    else:
        continue
    
print('Sua lista da feira >', lista)
print('\033[0m')

