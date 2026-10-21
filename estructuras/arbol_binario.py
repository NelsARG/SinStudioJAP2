from modelos.nodos import NodoBinario

class ArbolBinarioExpresiones:
    # Implementa un Árbol Binario para parsear y evaluar expresiones matemáticas
    # Los nodos hoja almacenan operandos y los internos operadores (+, -, *, /)
    
    def __init__(self):
        self.raiz = None

    def construir_desde_expresion(self, expresion: str) -> None:
        # Parsea una cadena de texto y construye el árbol binario de expresiones
        # Limpiamos los espacios en blanco de la expresión antes de procesarla
        expresion_limpia = expresion.replace(" ", "")
        self.raiz = self._parsear_expresion(expresion_limpia)

    def _parsear_expresion(self, expr: str) -> NodoBinario:
        # Método auxiliar recursivo para descomponer la expresión en un árbol de nodos binarios
        
        # Buscamos operadores de menor precedencia (+ o -) fuera de paréntesis
        parentesis = 0
        for i in range(len(expr) - 1, -1, -1):
            char = expr[i]
            if char == ')':
                parentesis += 1
            elif char == '(':
                parentesis -= 1
            elif parentesis == 0 and char in ('+', '-'):
                nodo = NodoBinario(char)
                nodo.izquierdo = self._parsear_expresion(expr[:i])
                nodo.derecho = self._parsear_expresion(expr[i+1:])
                return nodo

        # Buscamos operadores de mayor precedencia (* o /) fuera de paréntesis
        parentesis = 0
        for i in range(len(expr) - 1, -1, -1):
            char = expr[i]
            if char == ')':
                parentesis += 1
            elif char == '(':
                parentesis -= 1
            elif parentesis == 0 and char in ('*', '/'):
                nodo = NodoBinario(char)
                nodo.izquierdo = self._parsear_expresion(expr[:i])
                nodo.derecho = self._parsear_expresion(expr[i+1:])
                return nodo

        # Si la expresión completa está envuelta en paréntesis, los removemos
        if expr.startswith('(') and expr.endswith(')'):
            return self._parsear_expresion(expr[1:-1])

        # Si no hay operadores externos, es un operando (número o variable) hoja
        return NodoBinario(expr)

    def evaluar(self) -> float:
        # Recorre el árbol en postorden para evaluar la expresión y devolver el resultado numérico
        if not self.raiz:
            return 0.0
        return self._evaluar_postorden(self.raiz)

    def _evaluar_postorden(self, nodo: NodoBinario) -> float:
        # Caso base: si el nodo es una hoja (no tiene hijos), retornamos su valor numérico
        if not nodo.izquierdo and not nodo.derecho:
            return float(nodo.valor)

        # Evaluamos recursivamente los subárboles izquierdo y derecho
        val_izq = self._evaluar_postorden(nodo.izquierdo)
        val_der = self._evaluar_postorden(nodo.derecho)

        # Aplicamos la operación matemática según el operador almacenado en el nodo
        if nodo.valor == '+':
            return val_izq + val_der
        elif nodo.valor == '-':
            return val_izq - val_der
        elif nodo.valor == '*':
            return val_izq * val_der
        elif nodo.valor == '/':
            if val_der == 0:
                raise ValueError("Error: División entre cero.")
            return val_izq / val_der
        
        raise ValueError(f"Operador desconocido: {nodo.valor}")
