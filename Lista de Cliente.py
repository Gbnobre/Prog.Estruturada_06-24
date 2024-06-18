lista_de_clientes = []
contador = 0

while contador < 20:
    cliente = input('Insira o nome do cliente para entrar na lista de espera: ')
    lista_de_clientes.append(cliente)
    contador = contador+1

    print('\033[35;1m')
    print('FILA DE CLIENTES >', (lista_de_clientes))
    print('\033[0m')
    if contador == 3:
        
        fim = input('Ainda tem cliente para atendimento? (SIM OU NÃO) ')  
     
        if fim == 'não' or fim == 'NÃO':
            break

while contador > 0:
    atendimento = input('Nome de cliente que ja foi atendido: ')
    lista_de_clientes.remove(atendimento) 
    
    print('\033[35;1m')
    print('FILA DE CLIENTES >', (lista_de_clientes))
    print('\033[0m')

    if contador == 0:
        pritn('TODOS OS CLIENTE FORAM ATENDIDOS') 
    


print('FILA DE CLIENTES >', (lista_de_clientes))
   
           
