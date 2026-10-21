class NodoNArio:
    # Representa un nodo dentro del sistema de archivos virtual (Workspace)
    # Cada nodo puede ser una carpeta o un archivo de código que almacena contenido
    def __init__(self, nombre: str, es_carpeta: bool = True):
        self.nombre = nombre
        self.es_carpeta = es_carpeta
        self.contenido = "" if not es_carpeta else None  # Almacena el texto/código si es un archivo
        self.hijos = []  # Lista para almacenar subcarpetas o archivos anidados
        self.padre = None

    def agregar_hijo(self, nodo_hijo):
        # Asigna el padre y añade el nodo hijo a la lista
        nodo_hijo.padre = self
        self.hijos.append(nodo_hijo)

    def eliminar_hijo(self, nombre: str):
        # Filtra la lista de hijos eliminando el que coincida con el nombre
        self.hijos = [hijo for hijo in self.hijos if hijo.nombre != nombre]


class NodoBinario:
    # Representa un nodo para el Árbol Binario de Expresiones Clásico
    # Los nodos hoja almacenan operandos (números) y los internos operadores (+, -, *, /)
    def __init__(self, valor: str):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class NodoAVL:
    # Representa un nodo para el Árbol AVL de Autocompletado y Diccionario Rápido
    # Almacena una palabra clave, una descripción y los atributos de balanceo
    def __init__(self, palabra: str, descripcion: str = ""):
        self.palabra = palabra
        self.descripcion = descripcion
        self.izquierdo = None
        self.derecho = None
        self.altura = 1  # Altura inicial para el control de balanceo O(log n)


class NodoB:
    # Representa un nodo (página) para el Árbol B (B-Tree) de Búsqueda Global
    # Almacena claves (tokens de variables/funciones) y sus referencias en archivos
    def __init__(self, es_hoja: bool = True, orden_minimo: int = 4):
        self.es_hoja = es_hoja
        self.orden_minimo = orden_minimo
        self.claves = []   # Lista de tokens (ej. nombre de variable)
        self.valores = []  # Lista de referencias (IDs de archivos y líneas)
        self.hijos = []    # Punteros a otros nodos del Árbol B
