# SinStudioJAP2

# Synthetix Studio - Estructuras Jerárquicas y Búsqueda Avanzada


## Características Principales

* **Explorador de Espacio de Trabajo (Árbol N-ario):** Representa un sistema de archivos virtual con soporte para carpetas anidadas y movimientos de archivos, incluyendo un recorrido en *preorden* para la jerarquía visual estilo `tree`.
* **Evaluador de Expresiones (Árbol Binario ):** Analizador sintáctico (*parser*) que procesa expresiones matemáticas y las evalúa mediante recorridos en *postorden*.
* **Autocompletado y Diccionario Rápido (Árbol AVL):** Diccionario auto-balanceable de palabras clave con garantía de tiempos $O(\log n)$ y sugerencias al introducir prefijos mediante recorridos *inorden*.
* **Índice de Búsqueda Global (Árbol B ):** Motor de alta eficiencia para indexar variables y funciones creadas por el usuario en todo el Workspace.
* **Consola de Línea de Comandos (CLI):** Interfaz basada en comandos directos .

---

## Estructura del Proyecto

El proyecto está diseñado bajo estrictos principios de Programación Orientada a Objetos (POO) y modularización por semejanza:


.
 cli/
    consola.py          # Gestión de comandos y patrón de diseño CLI
 estructuras/
    arbol_n_ario.py     # Lógica del sistema de archivos virtual
    arbol_binario.py    # Lógica del evaluador de expresiones matemáticas
    arbol_avl.py        # Lógica del autocompletado y balanceo
    arbol_b.py          # Lógica de indexación y búsqueda global
 modelos/
    nodos.py            # Clases de nodos para cada tipo de árbol
 main.py                 # Punto de entrada principal del Mini IDE
 README.md               # Documentación del proyecto
