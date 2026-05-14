# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**: ChatGPT

**Prompt usado**:
> Actúa como un tutor de Python. Dame una receta paso a paso para crear un script que implemente cinco funciones simples de variables y tipos de datos: crear_saludo(nombre), suma_enteros(a,b), es_mayor_de_edad(edad), tipo_de_dato(valor) y convertir_a_float(valor). Muéstrame el código sin usar librerías externas.

**Resultado obtenido**:
Me generó un código en Python con la implementación exacta y comentarios explicando cada paso.

**¿Lo usaste tal cual o lo modificaste?**
Tomé la estructura lógica sugerida pero reescribí el código adaptándolo a la plantilla provista, eliminando comentarios redundantes para mantenerlo limpio junto a los docstrings originales.

---

### 2 - condicionales.py

**Herramienta**: ChatGPT

**Prompt usado**:
> Quiero implementar una función en Python para clasificar notas escolares (`clasificar_nota(nota: float) -> str`) y otra para saber si un año es bisiesto (`es_bisiesto(anio: int) -> bool`). Antes de darme el código, haceme 3 preguntas para confirmar cómo debe funcionar la clasificación de notas y cuáles son las reglas exactas de los años bisiestos. Después de que te responda, proponé el código.

**Resultado obtenido**:
La IA me hizo las preguntas. Le respondí con las reglas del TP (9=Sobresaliente, etc.) y luego me generó el código con condicionales `if-elif-else` correctos.

**¿Lo usaste tal cual o lo modificaste?**
Lo utilicé como base de referencia. Revisé minuciosamente la lógica generada para `es_bisiesto` y verifiqué a mano que el anidamiento de condicionales con el operador de módulo `%` cumpliera con la regla matemática antes de integrarlo.

---

### 3 - listas.py

**Herramienta**: ChatGPT

**Prompt usado**:
> Estoy resolviendo unos ejercicios de listas en Python. Tengo que implementar funciones para sumar una lista, filtrar números pares, invertir la lista (sin modificar la original), eliminar duplicados y aplanar una lista de listas. ¿Podés revisar mi idea de usar comprensiones de listas (list comprehensions) como verificador cognitivo? Mencioná pros, contras, y mostrame 3 tests de ejemplo para la función de aplanar listas.

**Resultado obtenido**:
Me explicó que las list comprehensions son más "Pythonicas" y cortas, pero pueden ser difíciles de leer si son muy complejas (como en el caso de aplanar listas). Me dio casos de prueba útiles.

**¿Lo usaste tal cual o lo modificaste?**
Lo usé como guía. Implementé la comprensión de listas para aplanar (`[item for sublist in lista for item in sublist]`) porque me pareció elegante, y usé un bucle `for` tradicional para eliminar duplicados preservando el orden.

---

### 4 - diccionarios.py

**Herramienta**: GitHub Copilot

**Prompt usado**:
> (Como comentario dentro del IDE)
> # Retorna un nuevo diccionario con claves y valores intercambiados usando dictionary comprehension

**Resultado obtenido**:
Copilot me sugirió la línea de código `return {v: k for k, v in d.items()}` instantáneamente.

**¿Lo usaste tal cual o lo modificaste?**
Adopté el concepto de "dictionary comprehension" que propuso, pero primero investigué la documentación oficial sobre cómo funcionaba la iteración sobre `.items()` para asegurarme de entender la solución antes de escribirla.

---

### 5 - loops.py

**Herramienta**: ChatGPT

**Prompt usado**:
> P1: ¿Cómo puedo calcular los primeros N números de la serie de Fibonacci usando un bucle for o while en Python?
> P2: ¿Qué pasa si N es 0 o negativo? ¿Debería devolver una lista vacía?
> P3: Mostrame la implementación de `fibonacci(n: int) -> list` que cubra esos casos borde y que empiece con [0, 1].

**Resultado obtenido**:
Me generó la función `fibonacci` validando el caso de `n <= 0` retornando `[]` y construyendo la lista progresivamente.

**¿Lo usaste tal cual o lo modificaste?**
Lo modifiqué ligeramente para agregar una validación rápida `if n == 1: return [0]` antes de inicializar la lista con `[0, 1]`.

---

### 6 - funciones.py

**Herramienta**: ChatGPT

**Prompt usado**:
> Necesito implementar una función `memoizar(func)` en Python que actúe como un decorador (o un closure) para guardar los resultados previos de una función costosa en un diccionario de caché. Analizá los pros y contras de usar una variable de entorno local (closure) vs una variable global, y luego recomendá UNO y escribí el código.

**Resultado obtenido**:
Me recomendó usar una variable de entorno local dentro de la función `memoizar` (un diccionario `cache = {}`) para evitar estado global compartido. Me dio el código del wrapper.

**¿Lo usaste tal cual o lo modificaste?**
Implementé la recomendación teórica de usar un entorno local (closure), pero desarrollé la estructura del decorador yo mismo basándome en los apuntes de la materia para asegurarme de no incluir funciones extrañas.

---

### 7 - operaciones.py

**Herramienta**: ChatGPT

**Prompt usado**:
> Tengo que implementar la función `caesar_cipher(texto: str, desplazamiento: int) -> str` en Python. Compará 2 enfoques: 
> A) Usar una constante con el abecedario y buscar los índices.
> B) Usar las funciones `ord()` y `chr()` con aritmética modular.
> Elegí el más eficiente y limpio, justificá y escribí el código. Asegurate de que solo afecte letras (ignorando puntuación).

**Resultado obtenido**:
Recomendó la opción B por ser más genérica y no requerir variables extra con el alfabeto completo. Me escribió la lógica con aritmética modular (restando y sumando la base ASCII).

**¿Lo usaste tal cual o lo modificaste?**
Me guié por la idea de usar aritmética modular que sugirió la IA, pero reconstruí el código para incorporar un manejo adecuado de mayúsculas (`ord('A')`) y minúsculas (`ord('a')`), garantizando el comportamiento correcto.

---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
Aprendí que darle un rol a la IA o pedirle explícitamente que pregunte antes de dar código ("Interacción invertida") evita que asuma cosas incorrectas.
- ¿En qué casos la IA fue útil y en cuáles no?
Fue muy útil para generar lógicas estándar (como Fibonacci o cifrado César) de manera rápida. No fue tan útil si el prompt es vago, ya que suele incluir muchas librerías externas o métodos no vistos en clase.
- ¿Qué harías diferente la próxima vez?
La próxima vez iteraría más en lugar de pedir la función completa de una sola vez, para forzar a la IA a explicarme la lógica y aprender mejor yo mismo los algoritmos subyacentes.
