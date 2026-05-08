# Exercícios intermediários e mais avançados
# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.
lista_emails = ["fulano@exemplo.com", "ciclano@exemplo.com",
                "fulano@exemplo.com", "fulano1@exemplo.com"]
emails_unicos = list(set(lista_emails))
print(emails_unicos)


# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
lista_idades = [15, 22, 17, 30, 18, 14]
idades_maiores_ou_iguais_a_18 = [
    idade for idade in lista_idades if idade >= 18]
print(idades_maiores_ou_iguais_a_18)


# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
pessoas = [
    {"nome": "Fulano", "idade": 25},
    {"nome": "Ciclano", "idade": 30},
    {"nome": "Beltrano", "idade": 20}
]
# sorted é uma função embutida em Python que retorna uma nova lista ordenada a partir dos itens de um iterável. O parâmetro key é usado para especificar uma função que será chamada em cada item da lista para determinar a chave de ordenação. Nesse caso, estamos usando uma função lambda para extrair o valor da chave "nome" de cada dicionário, o que permite ordenar as pessoas pelo nome.
pessoas_ordenadas = sorted(pessoas, key=lambda x: x["nome"])
# lambda é uma função anônima, ou seja, uma função sem nome, que pode ser definida em uma única linha. Ela é frequentemente usada para criar funções simples e rápidas, especialmente quando são necessárias como argumentos para outras funções, como no caso do sorted. A sintaxe geral de uma função lambda é: lambda argumentos: expressão. No exemplo acima, a função lambda recebe um argumento x (que representa cada dicionário na lista) e retorna o valor associado à chave "nome" desse dicionário, permitindo que o sorted ordene as pessoas com base em seus nomes.
print(pessoas_ordenadas)


# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.
numeros = [10, 20, 30, 40, 50]
# sum é uma função embutida em Python que retorna a soma de todos os itens em um iterável, como uma lista. No exemplo acima, estamos usando sum para calcular a soma de todos os números na lista "numeros". Em seguida, dividimos essa soma pelo número de elementos na lista (obtido com len(numeros)) para calcular a média.
media = sum(numeros) / len(numeros)
print(media)


# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
valores_totais = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valores_pares = [valor for valor in valores_totais if valor % 2 == 0]
valores_impares = [valor for valor in valores_totais if valor % 2 != 0]
print("Pares:", valores_pares)
print("Ímpares:", valores_impares)


# Exercícios com Dicionários
# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
produtos = [
    {"id1": 1, "nome": "Produto A", "preco": 10.0},
    {"id2": 2, "nome": "Produto B", "preco": 20.0},
    {"id3": 3, "nome": "Produto C", "preco": 30.0}
]
produto_id_para_atualizar = 2
novo_preco = 25.0
for produto in produtos:
    if produto["id2"] == produto_id_para_atualizar:
        produto["preco"] = novo_preco
        break
print(produtos)


# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# A partir do Python 3.9, você pode usar o operador de união (|) para fundir dois dicionários de forma simples e elegante. O operador | cria um novo dicionário que contém todas as chaves e valores dos dicionários originais. Se houver chaves duplicadas, os valores do segundo dicionário (dict2) irão sobrescrever os valores do primeiro dicionário (dict1). No exemplo acima, o resultado será um novo dicionário que combina as chaves e valores de ambos os dicionários, resultando em {'a': 1, 'b': 2, 'c': 3, 'd': 4}.
dict_fundido = dict1 | dict2
print(dict_fundido)

# OR
# ** é o operador de desempacotamento de dicionários, que permite combinar os pares chave-valor de ambos os dicionários em um novo dicionário. Assim como o operador |, se houver chaves duplicadas, os valores do segundo dicionário (dict2) irão sobrescrever os valores do primeiro dicionário (dict1). O resultado será o mesmo que o uso do operador |, ou seja, um novo dicionário que contém todas as chaves e valores de ambos os dicionários.
dicts_fundidos = {**dict1, **dict2}
print(dicts_fundidos)

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

estoque_produtos = {
    "Produto A": {"preco": 10.0, "quantidade": 5},
    "Produto B": {"preco": 20.0, "quantidade": 0},
    "Produto C": {"preco": 30.0, "quantidade": 3}
}

# Filtrar produtos com quantidade maior que 0
produtos_em_estoque = {produto: quantidade for produto,
                       quantidade in estoque_produtos.items() if quantidade["quantidade"] > 0}
print("Produtos em estoque:", produtos_em_estoque)


# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
dict0 = {"a": 1, "b": 2, "c": 3}
chaves = list(dict0.keys())
valores = list(dict0.values())

print("Chaves:", chaves)
print("Valores:", valores)


# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
frase = "analise de dados é como engenharia de dados, mas com mais café"
frequencia_caracteres = {}
for caractere in frase:
    if caractere in frequencia_caracteres:
        frequencia_caracteres[caractere] += 1
    else:
        frequencia_caracteres[caractere] = 1
print("Frequência de caracteres:", frequencia_caracteres)
