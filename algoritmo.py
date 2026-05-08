lista_de_numeros: list = [40, 50, 60, 70, 0, -408593, 1, 50]

# def é definir uma função, ou seja, empacotar um bloco de código para ser reutilizado posteriormente. O nome da função é "ordenar_lista" e ela recebe um argumento chamado "lista_de_numeros", que é a lista que queremos ordenar.


# recebe uma lista e retorna uma lista ordenada
def ordenar_lista_de_numeros(numeros: list) -> list:
    # A função utiliza um algoritmo de ordenação simples, conhecido como bubble sort, para ordenar a lista de números. O algoritmo percorre a lista várias vezes, comparando elementos adjacentes e trocando-os de posição se estiverem na ordem errada. O processo é repetido até que a lista esteja completamente ordenada.
    # cria uma cópia da lista original para não modificar a original
    nova_lista_de_numeros = numeros.copy()

    for i in range(len(nova_lista_de_numeros)):
        for j in range(i+1, len(nova_lista_de_numeros)):
            if nova_lista_de_numeros[i] > nova_lista_de_numeros[j]:
                nova_lista_de_numeros[i], nova_lista_de_numeros[j] = nova_lista_de_numeros[j], nova_lista_de_numeros[i]

    return nova_lista_de_numeros


nova_lista = ordenar_lista_de_numeros(lista_de_numeros)

print(lista_de_numeros)
print(nova_lista)
