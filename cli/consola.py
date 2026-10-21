from estructuras.arbol_n_ario import ArbolNArio
from estructuras.arbol_binario import ArbolBinarioExpresiones
from estructuras.arbol_avl import ArbolAVL
from estructuras.arbol_b import ArbolB

class ConsolaCLI:
    # Implementa la Consola de Línea de Comandos utilizando el Patrón Command
    
    
    def __init__(self):
        self.arbol_n_ario = ArbolNArio()
        self.arbol_binario = ArbolBinarioExpresiones()
        self.arbol_avl = ArbolAVL()
        self.arbol_b = ArbolB()
        self.ejecutando = True

    def iniciar(self):
        # Inicia el bucle principal de la interfaz de comandos del Mini IDE
        print("=== Synthetix Studio CLI ===")
        print("Escribe 'help' para ver los comandos disponibles o 'exit' para salir.")
        
        while self.ejecutando:
            try:
                prompt = f"[{self.arbol_n_ario.nodo_actual.nombre}]> "
                comando_input = input(prompt).strip()
                if not comando_input:
                    continue
                
                self.procesar_comando(comando_input)
            except Exception as e:
                print(f"Error: {e}")

    def procesar_comando(self, entrada: str):
        # Analiza la entrada del usuario y ejecuta la acción correspondiente en la estructura adecuada
        partes = entrada.split(maxsplit=1)
        comando = partes[0].lower()
        argumento = partes[1] if len(partes) > 1 else ""

        # Comandos del Árbol N-ario[cite: 3]
        if comando == "mkdir":
            if not argumento:
                print("Uso: mkdir <nombre_carpeta>")
                return
            self.arbol_n_ario.crear_carpeta(argumento)
            print(f"Carpeta '{argumento}' creada exitosamente.")

        elif comando == "cd":
            if not argumento:
                print("Uso: cd <nombre_carpeta>")
                return
            exito = self.arbol_n_ario.cambiar_directorio(argumento)
            if not exito:
                print(f"Directorio no encontrado o inválido: {argumento}")

        elif comando == "tree":
            print(self.arbol_n_ario.imprimir_arbol())

        # Comando del Árbol Binario
        elif comando == "eval":
            if not argumento:
                print('Uso: eval "<expresion>"')
                return
            expr_limpia = argumento.strip('"').strip("'")
            self.arbol_binario.construir_desde_expresion(expr_limpia)
            resultado = self.arbol_binario.evaluar()
            print(f"Resultado: {resultado}")

        # Comandos del Árbol AVL
        elif comando == "add-keyword":
            if not argumento:
                print("Uso: add-keyword <palabra>")
                return
            self.arbol_avl.insertar(argumento, descripcion="Palabra clave del lenguaje")
            print(f"Palabra clave '{argumento}' agregada al diccionario AVL.")

        elif comando == "suggest":
            if not argumento:
                print("Uso: suggest <prefijo>")
                return
            sugerencias = self.arbol_avl.sugerir_por_prefijo(argumento)
            print(f"Sugerencias para '{argumento}': {sugerencias}")

        # Comandos del Árbol B
        elif comando == "index-all":
            # Simula el escaneo de archivos abiertos y actualización del Árbol B
            self.arbol_b.insertar_o_actualizar("main", "main.py", 10)
            self.arbol_b.insertar_o_actualizar("contador", "utils.py", 5)
            print("¡Árbol B indexado exitosamente con los tokens del Workspace!")

        elif comando == "find-global":
            if not argumento:
                print("Uso: find-global <token>")
                return
            referencias = self.arbol_b.buscar_global(argumento)
            if referencias:
                print(f"Token '{argumento}' encontrado en las referencias (Archivo, Línea): {referencias}")
            else:
                print(f"Token '{argumento}' no encontrado en el índice global.")

        elif comando == "exit" or comando == "salir":
            print("Saliendo de Synthetix Studio...")
            self.ejecutando = False

        elif comando == "help":
            print("Comandos disponibles:")
            print("  mkdir <nombre>          - Crea una carpeta en el Workspace (Árbol N-ario)")
            print("  cd <nombre>             - Cambia de directorio o sube con '..' (Árbol N-ario)")
            print("  tree                    - Muestra la jerarquía de archivos en preorden (Árbol N-ario)")
            print('  eval "<expresion>"      - Evalúa una expresión matemática en postorden (Árbol Binario)')
            print("  add-keyword <palabra>   - Inserta una palabra clave con balanceo (Árbol AVL)")
            print("  suggest <prefijo>       - Sugiere palabras clave por prefijo (Árbol AVL)")
            print("  index-all               - Indexa variables y funciones (Árbol B)")
            print("  find-global <token>     - Busca un token globalmente en archivos (Árbol B)")
            print("  exit                    - Sale de la aplicación")
        else:
            print(f"Comando desconocido: '{comando}'. Escribe 'help' para ver la lista de comandos.")
