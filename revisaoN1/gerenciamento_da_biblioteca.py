livros = {
    101: {"titulo": "A Caverna", "autor": "José Saramago", "ano": 2000},
    102: {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    103: {"titulo": "O Primo Basílio", "autor": "José de Alencar", "ano": 1878},
    104: {"titulo": "A Moreninha", "autor": "Joaquim Manuel de Macedo", "ano": 1844},
    105: {"titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis", "ano": 1881},
    106: {"titulo": "O Guarani", "autor": "José de Alencar", "ano": 1857},
    107: {"titulo": "Senhora", "autor": "José de Alencar", "ano": 1875},
    108: {"titulo": "Iracema", "autor": "José de Alencar", "ano": 1865},
    109: {"titulo": "A Moreninha", "autor": "Joaquim Manuel de Macedo", "ano": 1844},
    110: {"titulo": "O Cortiço", "autor": "Aluísio Azevedo", "ano": 1890},
    111: {"titulo": "A Escrava Isaura", "autor": "Bernardo Guimarães", "ano": 1875},
    112: {"titulo": "O Primo Basílio", "autor": "José de Alencar", "ano": 1878},
    113: {"titulo": "O Alienista", "autor": "Machado de Assis", "ano": 1882},
    114: {"titulo": "Brás Cubas", "autor": "Machado de Assis", "ano": 1881},
    115: {"titulo": "O Guarani", "autor": "José de Alencar", "ano": 1857},
    116: {"titulo": "Iracema", "autor": "José de Alencar", "ano": 1865}
}

#Qual é o título do livro com ID 112?
livro112 = livros[112]
livro_titulo = livro112["titulo"]
print(f'Esse é o título do livro com ID 112: {livro_titulo} ')

#Liste todos os títulos dos livros escritos por José de Alencar.
print("OS LIVROS SÃO:")
for chave in livros:
    valor = livros[chave]
    if valor["autor"] == "José de Alencar":
        print(valor["titulo"])

#Encontre o livro mais recente (ou seja, com o ano de publicação mais alto).
anoMaisRecente = 0
livroMaisRecente = None

for id in livros:
    livro = livros[id]
    if livro["ano"] > anoMaisRecente:
        anoMaisRecente = livro["ano"]
        livroMaisRecente = livro["titulo"]
print(f"O livro mais recente é '{livroMaisRecente}', publicado em {anoMaisRecente}.")

#Quantos livros foram publicados antes de 1880?
cont = 0
for id in livros:
    livro = livros[id]
    if livro["ano"] < 1880:
        cont += 1
print(f'Números de livros publicados antes de 1880: {cont}')

#Qual é o ID do livro mais antigo (ou seja, com o ano de publicação mais baixo)?
anoMaisAntigo = 2050
livroMaisAntigo = None
for id in livros:
    livro = livros[id]
    if livro["ano"] < anoMaisAntigo:
        anoMaisAntigo = livro["ano"]
        livroMaisAntigo = id

print("ID do livro mais antigo:", livroMaisAntigo)

anoDoLivroMaisAntigo = livros[livroMaisAntigo]["ano"]
print("Ano de publicação do livro mais antigo:", anoDoLivroMaisAntigo)

#Crie um novo dicionário contendo apenas os livros publicados depois do ano 1880 e com seus respectivos títulos e autores.
novosLivros = {}

for id in livros:
    livro = livros[id]
    if livro["ano"] > 1880:
        novosLivros[id] = {
            "titulo": livro["titulo"],
            "autor": livro["autor"],
            "ano": livro["ano"]
        }
print("Livros publicados após 1880:")
print(novosLivros)

