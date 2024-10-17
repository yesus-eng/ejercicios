from nodo import Nodo

class ListaEnlazada:
    """Clase para manejar una lista enlazada simple."""
    def __init__(self):
        self.cabeza = None
    
    def agregar_final(self, valor):
        """Agrega un nuevo nodo al final de la lista."""
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar_lista(self):
        """Muestra la lista enlazada."""
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.valor))
            actual = actual.siguiente
        print(" -> ".join(elementos) + " -> None")

    def eliminar_multiplos_de_2(self):
        """Elimina los nodos cuyo valor sea múltiplo de 2."""
        while self.cabeza and self.cabeza.valor % 2 == 0:
            self.cabeza = self.cabeza.siguiente
        
        actual = self.cabeza
        while actual and actual.siguiente:
            if actual.siguiente.valor % 2 == 0:
                actual.siguiente = actual.siguiente.siguiente
            else:
                actual = actual.siguiente

class ListaCaracteres(ListaEnlazada):
    """Clase para manejar una lista de caracteres, heredando de ListaEnlazada."""
    def encontrar_mayor(self):
        """Encuentra el carácter con el mayor valor en la lista."""
        if not self.cabeza:
            return None
        mayor = self.cabeza.valor
        actual = self.cabeza.siguiente
        while actual:
            if actual.valor > mayor:
                mayor = actual.valor
            actual = actual.siguiente
        return mayor

    def a_lista(self):
        """Convierte la lista enlazada en una lista de Python."""
        actual = self.cabeza
        lista = []
        while actual:
            lista.append(actual.valor)
            actual = actual.siguiente
        return lista
