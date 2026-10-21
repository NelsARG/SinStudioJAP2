from modelos.nodos import NodoNArio

class ArbolNArio:
    
    #Implementa un Árbol N-ario para representar un sistema de archivos virtual dentro del IDE.
    #Cada nodo representa una carpeta o un archivo de código.
    
    def __init__(self, nombre_raiz: str = "workspace"):
        # Inicializa la raíz del espacio de trabajo con un nodo carpeta principal
        self.raiz = NodoNArio(nombre_raiz, es_carpeta=True)
        self.nodo_actual = self.raiz

    def crear_carpeta(self, nombre: str) -> None:
        
        #Crea un nuevo directorio en el nivel actual del Workspace.
        #Permite la creación de carpetas infinitamente anidadas.
        
        nueva_carpeta = NodoNArio(nombre, es_carpeta=True)
        self.nodo_actual.agregar_hijo(nueva_carpeta)

    def cambiar_directorio(self, nombre: str) -> bool:
        
        #Cambia el directorio de trabajo actual navegando por los hijos del nodo
       # o permitiendo subir al nodo padre mediante '..'.
        
        # Comando para retroceder al directorio superior
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
        
        #Imprime la estructura jerárquica completa del proyecto recorriendo el árbol N-ario
       # mediante un recorrido en preorden.
        
        return self._preorden_recorrido(self.raiz, 0)

    def _preorden_recorrido(self, nodo: NodoNArio, nivel: int) -> str:
        # Método auxiliar recursivo para formatear la salida jerárquica
        resultado = "    " * nivel + f"📂 {nodo.nombre}\n" if nodo.es_carpeta else "    " * nivel + f"📄 {nodo.nombre}\n"
        for hijo in nodo.hijos:
            resultado += self._preorden_recorrido(hijo, nivel + 1)
        return resultado
