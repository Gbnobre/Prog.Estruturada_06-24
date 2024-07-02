n = int(input('Digite um número '))
total = 0

if n == 1:
    print(n , 'Não é primo')
elif n == 0:
    print(n, 'Não é primo')

if n > 1:
    primo = True 
    for i in range(2, int (n**0.5) + 1):
        if n % i == 0:
            primo = False
            break
    if primo:
        print(n, 'é primo')
    else:
        print(n, 'não é primo')