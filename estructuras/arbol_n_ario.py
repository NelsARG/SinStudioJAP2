class NodoNArio:
    # Representa un nodo dentro del sistema de archivos virtual (Workspace)
    # Cada nodo puede ser una carpeta o un archivo de código
    def __init__(self, nombre: str, es_carpeta: bool = True):
        self.nombre = nombre
        self.es_carpeta = es_carpeta
        self.hijos = []  # Lista para almacenar subcarpetas o archivos anidados
        self.padre = None

    def agregar_hijo(self, nodo_hijo):
        # Asigna el padre y añade el nodo hijo a la lista
        nodo_hijo.padre = self
        self.hijos.append(nodo_hijo)

    def eliminar_hijo(self, nombre: str):
        # Filtra la lista de hijos eliminando el que coincida con el nombre
        self.hijos = [hijo for hijo in self.hijos if hijo.nombre != nombre]


class ArbolNArio:
    # Implementa un Árbol N-ario para representar un sistema de archivos virtual (Workspace) dentro del IDE
    # Permite la creación de carpetas infinitamente anidadas y gestión de archivos
    def __init__(self, nombre_raiz: str = "workspace"):
        # Inicializa la raíz del espacio de trabajo con un nodo carpeta principal
        self.raiz = NodoNArio(nombre_raiz, es_carpeta=True)
        self.nodo_actual = self.raiz

    def crear_carpeta(self, nombre: str) -> None:
        # Crea un nuevo directorio en el nivel actual del Workspace
        nueva_carpeta = NodoNArio(nombre, es_carpeta=True)
        self.nodo_actual.agregar_hijo(nueva_carpeta)

    def crear_archivo(self, nombre: str) -> None:
        # Crea un nuevo archivo de código dentro del directorio actual del Workspace
        nuevo_archivo = NodoNArio(nombre, es_carpeta=False)
        self.nodo_actual.agregar_hijo(nuevo_archivo)

    def cambiar_directorio(self, nombre: str) -> bool:
        # Cambia el directorio de trabajo actual navegando por los hijos del nodo
        # o permitiendo subir al nodo padre mediante '..'
        if nombre == "..":
            if self.nodo_actual.padre is not None:
                self.nodo_actual = self.nodo_actual.padre
                return True
            return False
        
        # Buscar el directorio hijo correspondiente
        for hijo in self.nodo_actual.hijos:
            if hijo.nombre == nombre and hijo.es_carpeta:
                self.nodo_actual = hijo
                return True
        return False

    def imprimir_arbol(self) -> str:
        # Imprime la estructura jerárquica completa del proyecto recorriendo el árbol N-ario
        # mediante un recorrido en preorden
        return self._preorden_recorrido(self.raiz, 0)

    def _preorden_recorrido(self, nodo: NodoNArio, nivel: int) -> str:
        # Método auxiliar recursivo para formatear la salida jerárquica visual
        espaciado = "    " * nivel
        icono = "-- " if nodo.es_carpeta else "- "
        resultado = f"{espaciado}{icono}{nodo.nombre}\n"
        
        for hijo in nodo.hijos:
            resultado += self._preorden_recorrido(hijo, nivel + 1)
            
        return resultado
