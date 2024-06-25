lista = []
contador = 0

while contador < 10:
    
    n = int(input('Digite um número '))
    lista.append(n)
    print(lista)
    contador = contador+1
    if contador == 5:
        continuar = input('Deseja continuar? ')
    
        if continuar == 'sim':
            continue
    
        else:
            break

print('\033[33m') 
print('O maior número da lista é', max(lista))
print('\033[31m')
print('O menor número da lista é', min(lista))

print('\033[0m')
    
    
    
    
     