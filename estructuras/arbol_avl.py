from modelos.nodos import NodoAVL

class ArbolAVL:
    # Implementa un Árbol AVL 
     # Permite sugerir palabras completas al introducir un prefijo usando recorridos inorden
    
    def __init__(self):
        self.raiz = None

    def _obtener_altura(self, nodo: NodoAVL) -> int:
        # Retorna la altura de un nodo para el cálculo del balanceo
        if not nodo:
            return 0
        return nodo.altura

    def _obtener_factor_balance(self, nodo: NodoAVL) -> int:
        # Calcula el factor de balance (diferencia de alturas entre subárboles)
        if not nodo:
            return 0
        return self._obtener_altura(nodo.izquierdo) - self._obtener_altura(nodo.derecho)

    def _rotar_derecha(self, y: NodoAVL) -> NodoAVL:
        # Realiza una rotación simple a la derecha para balancear el árbol
        x = y.izquierdo
        T2 = x.derecho

        # Realizar rotación
        x.derecho = y
        y.izquierdo = T2

        # Actualizar alturas
        y.altura = max(self._obtener_altura(y.izquierdo), self._obtener_altura(y.derecho)) + 1
        x.altura = max(self._obtener_altura(x.izquierdo), self._obtener_altura(x.derecho)) + 1

        return x

    def _rotar_izquierda(self, x: NodoAVL) -> NodoAVL:
        # Realiza una rotación simple a la izquierda para balancear el árbol
        y = x.derecho
        T2 = y.izquierdo

        # Realizar rotación
        y.izquierdo = x
        x.derecho = T2

        # Actualizar alturas
        x.altura = max(self._obtener_altura(x.izquierdo), self._obtener_altura(x.derecho)) + 1
        y.altura = max(self._obtener_altura(y.izquierdo), self._obtener_altura(y.derecho)) + 1

        return y

    def insertar(self, palabra: str, descripcion: str = "") -> None:
        # Inserta una nueva palabra clave en el árbol AVL, balanceando la estructura mediante rotaciones si es necesario
        self.raiz = self._insertar_recursivo(self.raiz, palabra, descripcion)

    def _insertar_recursivo(self, nodo: NodoAVL, palabra: str, descripcion: str) -> NodoAVL:
        # Inserción estándar de BST
        if not nodo:
            return NodoAVL(palabra, descripcion)

        if palabra < nodo.palabra:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, palabra, descripcion)
        elif palabra > nodo.palabra:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, palabra, descripcion)
        else:
            # Si la palabra ya existe, actualizamos su descripción y retornamos el nodo sin cambios
            nodo.descripcion = descripcion
            return nodo

        # Actualizar la altura del nodo actual
        nodo.altura = 1 + max(self._obtener_altura(nodo.izquierdo), self._obtener_altura(nodo.derecho))

        # Obtener el factor de balance para verificar si se desbalanceó
        balance = self._obtener_factor_balance(nodo)

        # Caso Izquierda-Izquierda
        if balance > 1 and palabra < nodo.izquierdo.palabra:
            return self._rotar_derecha(nodo)

        # Caso Derecha-Derecha
        if balance < -1 and palabra > nodo.derecho.palabra:
            return self._rotar_izquierda(nodo)

        # Caso Izquierda-Derecha
        if balance > 1 and palabra > nodo.izquierdo.palabra:
            nodo.izquierdo = self._rotar_izquierda(nodo.izquierdo)
            return self._rotar_derecha(nodo)

        # Caso Derecha-Izquierda
        if balance < -1 and palabra < nodo.derecho.palabra:
            nodo.derecho = self._rotar_derecha(nodo.derecho)
            return self._rotar_izquierda(nodo)

        return nodo

    def sugerir_por_prefijo(self, prefijo: str) -> list:
        # Busca en el árbol AVL y retorna todas las palabras clave que coincidan con el prefijo dado
        sugerencias = []
        self._inorden_sugerencias(self.raiz, prefijo.lower(), sugerencias)
        return sugerencias

    def _inorden_sugerencias(self, nodo: NodoAVL, prefijo: str, resultados: list) -> None:
        # Recorrido inorden para recolectar sugerencias alfabéticamente
        if not nodo:
            return

        # Podamos ramas si es necesario, o exploramos simétricamente
        self._inorden_sugerencias(nodo.izquierdo, prefijo, resultados)
        
        if nodo.palabra.lower().startswith(prefijo):
            resultados.append(nodo.palabra)
            
        self._inorden_sugerencias(nodo.derecho, prefijo, resultados)
