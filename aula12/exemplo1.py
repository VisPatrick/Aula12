import pandas as pd

produtos = ['Notebook', 'Smartphone', 'Tablet', 'Smarwatch', 'Cãmera']
quantidade_estoque = [15, 30, 20, 10, 25]


estoque = pd.Series(quantidade_estoque, index=produtos)

print('\n', "Série Estoque de Produtos: ")
print(estoque)


print('\n', 'Quantidade de Notbook estoque: ')
print(estoque['Notebook'])


print('\n', 'Estoque de Notebook e Câmera: ')
print(estoque[['Notebook', 'Cãmera']].values)


print('\n', 'Produtos com estoque abaixo de 20 unidades: ')
print(estoque[estoque < 20])


print('\n', 'Aumentando o estoque em 5 unidades para todos os produtos: ')
print(estoque + 5)


estoque.loc ['Headphone'] = None
print("\nEstoque com o valor nulo (Headphone)")
print(estoque)


precos = pd.Series([3500, 2500, 1200, 000, 1500], index=produtos)



print("\nValor total do estoque por produto (preço 8 quantidade): ")
print(precos * estoque)