# lista de compras
compras = ['Ovos', 'Macarrão', 'Feijão', 'Arroz', 'Leite', 'Chocolate']
# exibe lista
for i in range(len(compras)):
    print(f'Índice {i}: {compras[i]}.')
# tratamento de exceção
try:
    indice = int(input('Índice do item que deseja retirar: '))
    item_retirado = compras[indice]
    # retira item da lista
    del(compras[indice])
    print(f'Item {item_retirado}, retirado com sucesso!\n')
except:
    print('Não foi possível excluir!\n')
finally:
    for i in range(len(compras)):
        print(f'Índice {i}: {compras[i]}.\n')