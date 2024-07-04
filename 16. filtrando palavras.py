palavras = ['pão', 'cachorro', 'rua', 'jovem', 'olhar', 'abacaxi', 'bolo', 'pulo', 'casa', 'todos', 'carta', 'hospital', 'aula']

letra = input('Digite uma letra: ')


palavras_filtradas = []

for palavra in palavras:
    if palavra.lower().startswith(letra):
        palavras_filtradas.append(palavra)

if palavras_filtradas:
    print(f'Palavras que começam com {letra}:')
    for palavra in palavras_filtradas:
        print(palavra)

else:
    print(f'Nenhuma palavra encontrada com a letra {letra}')