---
tags:
  - bases
  - vanilla
---

### Clase sobre `**kwargs` en Python: Empaquetado y Desempaquetado

#### ¿Qué son `**kwargs`?

`**kwargs` es una convención en Python que permite a una función aceptar un número arbitrario de argumentos con nombre (keyword arguments). La función recibe estos argumentos como un diccionario, donde las claves son los nombres de los argumentos y los valores son los valores de los argumentos.
![[ejemplo kargs2.png]]
#### Implementación

**Empaquetado con `**kwargs`**:
Cuando defines una función con `**kwargs`, estás indicando que la función puede recibir un número variable de argumentos con nombre. Estos argumentos se empaquetan en un diccionario.

**Desempaquetado con `**kwargs`**:
Cuando llamas a una función y pasas un diccionario usando `**`, el diccionario se desempaqueta en argumentos con nombre que se pasan a la función.

![[ejemplo kargs1.png]]
#### Funcionalidad y Utilidad

**Funcionalidad**:
- Permite flexibilidad en la definición de funciones.
- Facilita el paso de un número variable de argumentos con nombre.
- Útil para funciones que necesitan manejar configuraciones o parámetros opcionales.

**Utilidad**:
- Creación de funciones genéricas y reutilizables.
- Paso de configuraciones a funciones de manera limpia y ordenada.
- Simplificación de la llamada a funciones con muchos parámetros opcionales.

#### Ejemplos Prácticos

**Empaquetado con `**kwargs`**:

```python
def ejemplo_kwargs(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# Llamada a la función
ejemplo_kwargs(nombre="Juan", edad=30, ciudad="Madrid")

# Output:
# <class 'dict'>
# nombre = Juan
# edad = 30
# ciudad = Madrid
```

**Desempaquetado con `**kwargs`**:

```python
def saludar(nombre, edad, ciudad):
    print(f"Hola, {nombre}. Tienes {edad} años y vives en {ciudad}.")

# Diccionario de argumentos
datos = {"nombre": "Ana", "edad": 25, "ciudad": "Barcelona"}

# Desempaquetado del diccionario
saludar(**datos)

# Output:
# Hola, Ana. Tienes 25 años y vives en Barcelona.
```

#### Ejemplo Completo: Combinación de `*args` y `**kwargs`

```python
def funcion_completa(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

# Llamada a la función con *args y **kwargs
funcion_completa(1, 2, 3, nombre="Carlos", edad=28)

# Output:
# args: (1, 2, 3)
# kwargs: {'nombre': 'Carlos', 'edad': 28}
```

#### Uso en Clases

**Empaquetado en Clases**:

```python
class Persona:
    def __init__(self, **kwargs):
        self.nombre = kwargs.get('nombre', 'Desconocido')
        self.edad = kwargs.get('edad', 0)
        self.ciudad = kwargs.get('ciudad', 'Desconocida')

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Ciudad: {self.ciudad}")

# Crear una instancia de Persona usando kwargs
persona = Persona(nombre="Luis", edad=35, ciudad="Valencia")
persona.mostrar_info()

# Output:
# Nombre: Luis, Edad: 35, Ciudad: Valencia
```

#### Buenas Prácticas

1. **Documenta tus funciones**: Indica qué argumentos con nombre espera la función.
2. **Usa nombres claros para los argumentos**: Facilita la comprensión y uso de la función.
3. **Combina con `*args` cuando sea necesario**: Permite recibir tanto argumentos posicionales como con nombre.

### Conclusión

El uso de `**kwargs` en Python proporciona una gran flexibilidad para el diseño de funciones y métodos. Permite escribir código más limpio y manejable, especialmente cuando se trabaja con una cantidad variable de argumentos. Además, facilita la reutilización de funciones en diferentes contextos, mejorando la eficiencia y la mantenibilidad del código.