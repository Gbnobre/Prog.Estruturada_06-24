print('BEM VINDO AO VERIFICADOR DE NÚMERO PERFEITO')

n = int(input('digite um número '))
d = 1
soma = 0

while d <= n/2:
    if n%d == 0:
        soma += d
    d = d+1
if n == soma:
    print('O número é perfeito')
else:
    print('O número não é perfeito')

