comidas = ['leite', 'couve','computador', 'tomate','garfo','faca','tablet','refrigerante']
bebidas = ['uva', 'colher','TV','vinho','cerveja','celular','banana']
talheres = ['arroz','iPhone', 'concha','whisky','vodka','feijão','colher de chá']

eletronicos = []

for item in comidas[:]:
    if item in ['computador', 'tablet']:
        eletronicos.append(item)
        comidas.remove(item)
    if item in ['leite', 'refrigerante']:
        bebidas.append(item)
        comidas.remove(item)
    if item in ['garfo', 'faca']:
        talheres.append(item)
        comidas.remove(item)    


for item in bebidas[:]:
    if item in ['TV', 'celular']:
        eletronicos.append(item)
        bebidas.remove(item)
    if item in ['uva',  'banana']:
        comidas.append(item)
        bebidas.remove(item)
    if item in ['colher']:
        talheres.append(item)
        bebidas.remove(item)

for item in talheres[:]:
    if item in ['iphone']:
        eletronicos.append(item)
        talheres.remove(item)
    if item in ['arroz',  'feijão']:
        comidas.append(item)
        talheres.remove(item)
    if item in ['whisky', 'vodka']:
        bebidas.append(item)
        talheres.remove(item)        

print('\57'*100)
print('\033[36m\20'*100)

print('\033[37mLista de comidas:', comidas,)
print('\033[36m\20'*100)

print('\033[37mLista de bebidas:', bebidas)
print('\033[36m\20'*100)

print('\033[37mLista de talheres:', talheres)
print('\033[36m\20'*100)

print('\033[37mLista de talheres:', eletronicos)
print('\033[36m\20'*100, '\033[0m')

print('\57'*100)