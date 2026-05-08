# >Crie um estrutura de dados é a mesma coisa que criar um dicionário

# Exercícios de Listas e Dicionários
# 1. Lista de números ao quadrado
# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
numeros = list(range(1, 11))
for numero in numeros:
    print(numero ** 2)

# 2. Modificar lista de linguagens
# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

linguagens = ["Python", "Java", "C++", "JavaScript"]
linguagens.remove("C++")
linguagens.append("Ruby")
print(linguagens)

# 3. Informações(dicionário) de um livro
# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
livro = {
    "título": "1984",
    "autor": "George Orwell",
    "ano": 1948
}
for chave, valor in livro.items():
    print(f"{chave}: {valor}")


# 4. Contar ocorrências de caracteres
# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
contagem = {}
string = "hello world"
for caractere in string:
    if caractere in contagem:
        contagem[caractere] += 1
    else:
        contagem[caractere] = 1
for caractere, quantidade in contagem.items():
    print(f"{caractere}: {quantidade}")

# OR
# s é a string que queremos contar os caracteres, e o retorno é um dicionário onde as chaves são os caracteres e os valores são as contagens.


def contar_ocorrencias(s: str) -> dict:
    contagem = {}
    for caractere in s:
        if caractere in contagem:
            # get é um método de dicionário que retorna o valor para a chave especificada, ou um valor padrão se a chave não existir. Nesse caso, estamos usando get para obter a contagem atual do caractere, e se ele não existir no dicionário, retornamos 0. Em seguida, somamos 1 para atualizar a contagem.
            contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem


print(contar_ocorrencias("hello world"))
# _______


# s é a string que queremos contar os caracteres, e o retorno é um dicionário onde as chaves são os caracteres e os valores são as contagens.
def contar_ocorrencias(s: str) -> dict:
    contagem = {}
    for caractere in s:
        contagem[caractere] += 1
    else:
        contagem[caractere] = 1
    return contagem


print(contar_ocorrencias("hello world"))


# 5. Preço total da lista de compras
# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
preco_total = sum(precos[item] for item in lista_compras)
print(f"Preço total: R$ {preco_total:.2f}")
