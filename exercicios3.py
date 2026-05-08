# Exercícios de Funções

# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
def soma_numeros(lista):
    return sum(lista)


lista_numeros = [1, 2, 3, 4, 5]
print(soma_numeros(lista_numeros))


# 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
def se_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
def reverter_string(s):
    return s[::-1]


# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
def argumentos_totais(lista_numeros, numero):
    pares = []
    for i in range(len(lista_numeros)):
        for j in range(i + 1, len(lista_numeros)):
            if lista_numeros[i] + lista_numeros[j] == numero:
                pares.append((lista_numeros[i], lista_numeros[j]))
    return pares

# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas


def chaves_ordenadas(dicionario):
    return sorted(dicionario.keys())
