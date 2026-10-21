class NodoArbolB:
    # Representa un nodo dentro del Árbol B (B-Tree)
    # Cada clave es un token (nombre de variable o función) y su valor es una lista de referencias (ID de archivo y línea)
    def __init__(self, es_hoja: bool = True, orden_minimo: int = 4):
        self.es_hoja = es_hoja
        self.orden_minimo = orden_minimo  # Orden mínimo m del Árbol B (ej. m = 4)
        self.claves = []   # Lista de tokens (variables o funciones)
        self.valores = []  # Lista de referencias compuestas por IDs de archivos y líneas
        self.hijos = []    # Punteros a los nodos hijos

class ArbolB:
    # Implementa un Árbol B para simular un motor de búsqueda de alta eficiencia para la opción "Buscar en todos los archivos"
    # Permite indexar todas las variables y funciones creadas por el usuario en el Workspace
    def __init__(self, orden_minimo: int = 4):
        self.raiz = NodoArbolB(es_hoja=True, orden_minimo=orden_minimo)
        self.orden_minimo = orden_minimo

    def insertar_o_actualizar(self, token: str, archivo_id: str, linea: int) -> None:
        # Inserta o actualiza un token en el Árbol B asociándolo con su archivo y línea correspondiente
        raiz = self.raiz
        if len(raiz.claves) >= (2 * self.orden_minimo) - 1:
            nuevo_nodo = NodoArbolB(es_hoja=False, orden_minimo=self.orden_minimo)
            self.raiz = nuevo_nodo
            nuevo_nodo.hijos.append(raiz)
            self._dividir_hijo(nuevo_nodo, 0, raiz)
            self._insertar_no_lleno(nuevo_nodo, token, archivo_id, linea)
        else:
            self._insertar_no_lleno(raiz, token, archivo_id, linea)

    def _dividir_hijo(self, padre: NodoArbolB, i: int, hijo: NodoArbolB) -> None:
        # Divide un nodo hijo cuando excede su capacidad máxima permitida en el Árbol B
        t = self.orden_minimo
        nuevo_hijo = NodoArbolB(es_hoja=hijo.es_hoja, orden_minimo=t)
        
        punto_medio = t - 1
        nuevo_hijo.claves = hijo.claves[punto_medio + 1:]
        nuevo_hijo.valores = hijo.valores[punto_medio + 1:]
        
        clave_subir = hijo.claves[punto_medio]
        valor_subir = hijo.valores[punto_medio]

        if not hijo.es_hoja:
            nuevo_hijo.hijos = hijo.hijos[punto_medio + 1:]
            hijo.hijos = hijo.hijos[:punto_medio + 1]

        hijo.claves = hijo.claves[:punto_medio]
        hijo.valores = hijo.valores[:punto_medio]

        padre.hijos.insert(i + 1, nuevo_hijo)
        padre.claves.insert(i, clave_subir)
        padre.valores.insert(i, valor_subir)

    def _insertar_no_lleno(self, nodo: NodoArbolB, token: str, archivo_id: str, linea: int) -> None:
        # Inserta un token recursivamente en un nodo que no está lleno
        i = len(nodo.claves) - 1

        if nodo.es_hoja:
            if token in nodo.claves:
                idx = nodo.claves.index(token)
                if (archivo_id, linea) not in nodo.valores[idx]:
                    nodo.valores[idx].append((archivo_id, linea))
            else:
                while i >= 0 and token < nodo.claves[i]:
                    i -= 1
                nodo.claves.insert(i + 1, token)
                nodo.valores.insert(i + 1, [(archivo_id, linea)])
        else:
            while i >= 0 and token < nodo.claves[i]:
                i -= 1
            i += 1
            if len(nodo.hijos[i].claves) >= (2 * self.orden_minimo) - 1:
                self._dividir_hijo(nodo, i, nodo.hijos[i])
                if token > nodo.claves[i]:
                    i += 1
            self._insertar_no_lleno(nodo.hijos[i], token, archivo_id, linea)

    def buscar_global(self, token: str) -> list:
        # Busca un token específico en el Árbol B y muestra en qué archivos y líneas se encuentra
        return self._buscar_recursivo(self.raiz, token)

    def _buscar_recursivo(self, nodo: NodoArbolB, token: str) -> list:
        i = 0
        while i < len(nodo.claves) and token > nodo.claves[i]:
            i += 1

        if i < len(nodo.claves) and token == nodo.claves[i]:
            return nodo.valores[i]

        if nodo.es_hoja:
            return []

        return self._buscar_recursivo(nodo.hijos[i], token)
