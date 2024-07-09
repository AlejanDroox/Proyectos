---
tags:
  - funcionalidad
  - idea
  - vanilla
fecha: 28/06/2024
---
```python
def multi_call(*funciones, **kwargs):
    """
    Llama a múltiples funciones secuencialmente con los mismos argumentos.

    Args:
        *funciones: Lista de funciones a llamar.
        **kwargs: Argumentos con nombre a pasar a cada función.

    Example:
        def greet(name, age):
            print(f"Hello, {name}! You are {age} years old.")
        
        def farewell(name):
            print(f"Goodbye, {name}!")

        multi_call(greet, farewell, name="John", age=30)
    """
    for f in funciones:
        try:
            f(**kwargs)
        except Exception as e:
            print(f"Error al ejecutar {f.__name__}: {e}")


def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

def farewell(name):
    print(f"Goodbye, {name}!")

multi_call(greet, farewell, name="John", age=30)

# Output
# Hello, John! You are 30 years old.
# Goodbye, John!
```
