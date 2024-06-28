print('\033[1;36m') 
print('Bem vindo a calculadora 2.0')
print('\033[31m')


simbolo = input('Digite (+) ou (-) ou (*) ou (/) > ')
print('\033[36m')

n1 = int(input('Digite o primeiro número > '))
n2 = int(input('Digite o segundo número > '))
n3 = 0

print('\033[32m')

if simbolo == '+':
    n3 = n1 + n2
    print(f'{n1} + {n2} = {n3}')

if simbolo == '-': 
    n3 = n1 - n2 
    print(f'{n1} - {n2} = {n3}')

if simbolo == '*': 
    n3 = n1 * n2 
    print(f'{n1} * {n2} = {n3}')

if simbolo == '/': 
    n3 = n1 / n2 
    print(f'{n1} / {n2} = {n3}')

print('\033[0m')