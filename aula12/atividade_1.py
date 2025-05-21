import pandas as pd

livros_categoria = ['Literatura Brasileira', 'Literatura Estrangueira', 'Ciências', 'Matremática', 'História']
quantidades_livros = [12, 9, 18, 14, 20]
livros_emprestados = [4, 2, 7, 5, 6]

biblioteca = pd.Series(quantidades_livros, index=livros_categoria)

biblioteca.loc ['Filosofia'] = None
print('\n', 'Estoque sem livro (Filosifia)')
print(biblioteca)

print("\nQuantidade de livros Disponível por categoria")
print(biblioteca)


print("\nCategorias que possuem mais de cinco livros")
print(biblioteca [biblioteca > 5])

