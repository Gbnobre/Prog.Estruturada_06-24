lista_de_alunos = []
fim = 'SIM'

print('')

while fim == 'sim' or fim == 'SIM':
    aluno = input('Insira o nome do aluno para entrar na lista: ')
    lista_de_alunos.append(aluno)
  

    print('\033[35;1m')
    print('FILA DE ALUNOS >', (lista_de_alunos))
    print('\033[0m')
        
    fim = input('Ainda tem alunos para entrar na fila? (SIM OU NÃO) ')  
    print('')
    if fim == 'não' or fim == 'NÃO':
        continue

print(lista_de_alunos)

