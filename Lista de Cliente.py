lista_de_clientes = []
fim = 'SIM'

print('')

while fim == 'sim' or fim == 'SIM':
    cliente = input('Insira o nome do cliente para entrar na lista de espera: ')
    lista_de_clientes.append(cliente)
  

    print('\033[35;1m')
    print('FILA DE CLIENTES >', (lista_de_clientes))
    print('\033[0m')
        
    fim = input('Ainda tem cliente para entrar na fila? (SIM OU NÃO) ')  
    print('')
    if fim == 'não' or fim == 'NÃO':
        continue

fim_do_atendimento = 'sim'

while fim_do_atendimento == 'sim' or fim_do_atendimento == 'Sim':
    atendimento = input('Digite 1 para atender o próximo cliente: ')
    lista_de_clientes.pop(0)
        
    
    print('\033[35;1m')
    print('FILA DE CLIENTES >', (lista_de_clientes))
    print('\033[0m')

    fim_do_atendimento = input('Ainda tem cliente para atendimento?') 
    
    if fim_do_atendimento == 'não' or fim_do_atendimento == 'NÃO':
        print('\033[36;1m')
        print(' FIM DA FILA >', (lista_de_clientes))
        print('\033[0m')


           
