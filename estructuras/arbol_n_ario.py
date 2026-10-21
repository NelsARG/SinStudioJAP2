class ArbolNArio:
    # Implementa un Árbol N-ario para representar un (Workspace) dentro del IDE
    
    def __init__(self, nombre_raiz: str = "workspace"):
        from modelos.nodos import NodoNArio
        # Inicializa la raíz del espacio de trabajo con un nodo carpeta principal
        self.raiz = NodoNArio(nombre_raiz, es_carpeta=True)
        self.nodo_actual = self.raiz

    def crear_carpeta(self, nombre: str) -> None:
        # Crea un nuevo directorio en el nivel actual del Workspace
        from modelos.nodos import NodoNArio
        nueva_carpeta = NodoNArio(nombre, es_carpeta=True)
        self.nodo_actual.agregar_hijo(nueva_carpeta)

    def crear_archivo(self, nombre: str) -> None:
        # Crea un nuevo archivo de código dentro del directorio actual del Workspace
        from modelos.nodos import NodoNArio
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
        # mediante un recorrido en preorden (estilo comando tree de Linux)
        return self._preorden_recorrido(self.raiz, 0)

    def _preorden_recorrido(self, nodo, nivel: int) -> str:
        # Método auxiliar recursivo para formatear la salida jerárquica visual
        espaciado = "    " * nivel
        icono = "/ " if nodo.es_carpeta else "* "
        resultado = f"{espaciado}{icono}{nodo.nombre}\n"
        
        for hijo in nodo.hijos:
            resultado += self._preorden_recorrido(hijo, nivel + 1)
            
        return resultado

    def obtener_todos_los_archivos(self) -> list:
        # Recorre recursivamente todo el árbol N-ario y retorna una lista con todos los nodos que son archivos
        archivos = []
        self._recorrer_buscando_archivos(self.raiz, archivos)
        return archivos

    def _recorrer_buscando_archivos(self, nodo, lista_archivos: list) -> None:
        # Método auxiliar recursivo para acumular los archivos encontrados
        if not nodo.es_carpeta:
            lista_archivos.append(nodo)
        
        for hijo in nodo.hijos:
            self._recorrer_buscando_archivos(hijo, lista_archivos)
