from lista_enlazada import ListaEnlazada, ListaCaracteres

def unir_y_ordenar_lista(lista1, lista2):
    """Combina dos listas de caracteres, las ordena y retorna una nueva lista."""
    l1 = lista1.a_lista()
    l2 = lista2.a_lista()
    lista_combinada = l1 + l2
    lista_combinada.sort()
    
    lista_ordenada = ListaCaracteres()
    for caracter in lista_combinada:
        lista_ordenada.agregar_final(caracter)
    return lista_ordenada

def main():
    # Ejercicio 1: Lista con múltiplos de 3, eliminar múltiplos de 2
    lista_numeros = ListaEnlazada()
    for i in range(3, 31, 3):  # Múltiplos de 3 hasta 30
        lista_numeros.agregar_final(i)

    print("Lista original con múltiplos de 3:")
    lista_numeros.mostrar_lista()

    lista_numeros.eliminar_multiplos_de_2()
    print("Lista después de eliminar múltiplos de 2:")
    lista_numeros.mostrar_lista()

    # Ejercicio 2: Operaciones con listas de caracteres
    lista1 = ListaCaracteres()
    lista2 = ListaCaracteres()

    for c in ['a', 'c', 'e']:
        lista1.agregar_final(c)

    for c in ['b', 'd', 'f']:
        lista2.agregar_final(c)

    print("Lista 1:")
    lista1.mostrar_lista()

    print("Lista 2:")
    lista2.mostrar_lista()

    mayor_lista1 = lista1.encontrar_mayor()
    mayor_lista2 = lista2.encontrar_mayor()

    if mayor_lista1 and mayor_lista2:
        if mayor_lista1 > mayor_lista2:
            print(f"La lista 1 tiene el mayor carácter: {mayor_lista1}")
        else:
            print(f"La lista 2 tiene el mayor carácter: {mayor_lista2}")
    elif mayor_lista1:
        print(f"La lista 1 tiene el único carácter: {mayor_lista1}")
    elif mayor_lista2:
        print(f"La lista 2 tiene el único carácter: {mayor_lista2}")
    else:
        print("Ambas listas están vacías.")

    lista_ordenada = unir_y_ordenar_lista(lista1, lista2)
    print("Lista unida y ordenada:")
    lista_ordenada.mostrar_lista()

if __name__ == "__main__":
    main()
