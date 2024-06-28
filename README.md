print('\033[36m')
print('Bem vindo a calculadora 2.0')
print('')

print('Digite o símbolo da operação e os 2 números para fazer o calculo')
print('\033[0m')
simbolo = input('Digite (+) ou (-) ou (*) ou (/) 》 ')

n1 = int(input('Digite o primeiro número 》 '))

n2 = int(input('Digite onsegundo número 》 '))

n3 = 0

if simbolo == '+' :
    n3 = n1 + n2
    print(f'{n1} + {n2} = {n3}')
    
if simbolo == '-' :
    n3 = n1 - n2
    print(f'{n1} - {n2} = {n3}')
    
if simbolo == '*' :
    n3 = n1 * n2
    print(f'{n1} * {n2} = {n3}')
    
if simbolo == '/' :
    n3 = n1 / n2
    print(f'{n1} / {n2} = {n3}')
