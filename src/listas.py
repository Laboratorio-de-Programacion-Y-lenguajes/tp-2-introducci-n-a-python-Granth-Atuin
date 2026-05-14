# ============================================================
# MÓDULO 3: Listas
# ============================================================


def suma_lista(numeros: list) -> int | float:
    """
    Retorna la suma de todos los elementos de la lista.
    """
    return sum(numeros)


def filtrar_pares(numeros: list) -> list:
    """
    Retorna una nueva lista con solo los números pares.
    """
    return [n for n in numeros if n % 2 == 0]


def invertir_lista(lista: list) -> list:
    """
    Retorna la lista invertida SIN modificar la original.
    """
    return lista[::-1]


def eliminar_duplicados(lista: list) -> list:
    """
    Retorna una nueva lista sin elementos duplicados,
    manteniendo el orden de primera aparición.
    """
    res = []
    for elem in lista:
        if elem not in res:
            res.append(elem)
    return res


def aplanar_lista(lista: list) -> list:
    """
    Dada una lista de listas, retorna todos los elementos en una sola lista.
    Ejemplo: aplanar_lista([[1,2],[3,4]]) -> [1, 2, 3, 4]
    """
    return [item for sublist in lista for item in sublist]
