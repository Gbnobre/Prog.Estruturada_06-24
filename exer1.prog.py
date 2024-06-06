# 10 N° int e retorne a somada dos 10

print('\033[1m')
print('\t\t\t\t\t\t **Digite 10 números para que sejam somados**\n')

print('\033[30;1m')

soma = 0
n = 0
while n < 10:
    numero = int(input('Digite um número\n'))
    soma = soma + numero
    n = n+1
    
print('A soma de todos os números é', soma)
    