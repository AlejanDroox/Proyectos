---
tags:
  - bases
  - vanilla
fecha: 28/06/2024
---

### Clase sobre el Uso de `raise` para Manejo de Errores en Python

El uso de `raise` en Python permite lanzar excepciones de manera explícita. Esto es útil para manejar errores de manera controlada y asegurar que tu código responde adecuadamente a situaciones inesperadas. En esta clase, veremos el uso básico y medio de `raise`.

#### Uso Básico de `raise`

`raise` se utiliza para lanzar una excepción. Aquí hay un ejemplo básico:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b

try:
    resultado = divide(10, 0)
except ValueError as e:
    print(e)
```

En este ejemplo:
- La función `divide` lanza una excepción `ValueError` si el divisor es cero.
- El bloque `try...except` captura la excepción y maneja el error imprimiendo un mensaje.

#### Definición de Excepciones Personalizadas

Puedes definir tus propias excepciones personalizadas heredando de la clase base `Exception`:

```python
class MiExcepcionPersonalizada(Exception):
    def __init__(self, mensaje, codigo):
        super().__init__(mensaje)
        self.codigo = codigo

def funcion_con_error():
    raise MiExcepcionPersonalizada("Ocurrió un error", 500)

try:
    funcion_con_error()
except MiExcepcionPersonalizada as e:
    print(f"Error: {e}, Código: {e.codigo}")
```

En este ejemplo:
- `MiExcepcionPersonalizada` es una excepción personalizada que acepta un mensaje y un código de error.
- La función `funcion_con_error` lanza la excepción personalizada.
- El bloque `try...except` captura la excepción y maneja el error imprimiendo el mensaje y el código.

#### Uso Avanzado de `raise`

Además de lanzar excepciones, puedes re-lanzar una excepción capturada con `raise`:

```python
def procesamiento_de_datos(datos):
    try:
        if not isinstance(datos, list):
            raise TypeError("Se esperaba una lista.")
        # Procesamiento de datos...
    except TypeError as e:
        print(f"Error de tipo: {e}")
        raise  # Re-lanza la excepción

try:
    procesamiento_de_datos("no es una lista")
except TypeError as e:
    print(f"Caught re-raised error: {e}")
```

En este ejemplo:
- La función `procesamiento_de_datos` lanza una excepción `TypeError` si los datos no son una lista.
- El bloque `try...except` dentro de la función captura la excepción y la re-lanza.
- El bloque `try...except` fuera de la función captura la excepción re-lanzada.

#### Uso de `raise` con Excepciones Encadenadas

Python 3 permite encadenar excepciones utilizando `from` para mantener el contexto de la excepción original:

```python
def funcion1():
    raise ValueError("Error en funcion1")

def funcion2():
    try:
        funcion1()
    except ValueError as e:
        raise RuntimeError("Error en funcion2") from e

try:
    funcion2()
except RuntimeError as e:
    print(f"Excepción encadenada: {e}")
    print(f"Contexto original: {e.__cause__}")
```

En este ejemplo:
- `funcion1` lanza una excepción `ValueError`.
- `funcion2` captura esta excepción y lanza una nueva excepción `RuntimeError` usando `from` para encadenar la excepción original.
- El bloque `try...except` captura la excepción `RuntimeError` y muestra el mensaje y el contexto de la excepción original.

#### Buenas Prácticas

1. **Usa Excepciones Específicas**: Siempre que sea posible, utiliza excepciones específicas en lugar de la clase base `Exception`.
2. **Manejo Adecuado de Excepciones**: Asegúrate de manejar adecuadamente las excepciones y no simplemente silenciarlas.
3. **Documenta tu Código**: Añade documentación para explicar por qué se lanzan ciertas excepciones.
4. **Mantén el Contexto**: Usa excepciones encadenadas para mantener el contexto de los errores.

Con estas técnicas, puedes mejorar significativamente el manejo de errores en tus aplicaciones Python, haciendo tu código más robusto y fácil de mantener.