---
tags:
  - db
  - libreria
  - intermedio
fecha: 28/06/2024
---
### Alembic: Introducción y Guía de Uso

**Alembic** es una herramienta de migración de bases de datos para Python, utilizada en conjunto con SQLAlchemy. Permite gestionar cambios en el esquema de la base de datos de manera controlada y reproducible.

#### Ventajas de Usar Alembic
- **Control de Versiones**: Permite mantener un historial de cambios en el esquema de la base de datos.
- **Reversibilidad**: Facilita la reversión de cambios, permitiendo volver a estados anteriores de la base de datos.
- **Automatización**: Genera automáticamente scripts de migración basados en los cambios detectados en los modelos SQLAlchemy.
- **Integración**: Se integra fácilmente con SQLAlchemy, proporcionando una solución completa para el manejo de bases de datos en aplicaciones Python.

#### Desventajas de Usar Alembic
- **Curva de Aprendizaje**: Puede tener una curva de aprendizaje empinada para desarrolladores nuevos en SQLAlchemy o manejo de bases de datos.
- **Complejidad Inicial**: La configuración inicial puede ser un poco compleja para proyectos muy pequeños o simples.

#### Implementación de Alembic

**1. Instalación:**
```bash
pip install alembic
```

**2. Configuración Inicial:**
Para iniciar un proyecto de Alembic, navega a tu directorio de proyecto y ejecuta:
```bash
alembic init alembic
```
Esto creará una carpeta `alembic` y un archivo `alembic.ini`.

**3. Configuración de `alembic.ini`:**
Edita `alembic.ini` para apuntar a tu base de datos. Busca la línea `sqlalchemy.url` y configúrala así:
```ini
sqlalchemy.url = sqlite:///mi_base_de_datos.db
```

**4. Configuración de `alembic/env.py`:**
En `alembic/env.py`, configura la meta información de la base de datos importando tu modelo:
```python
from myapp.models import Base
target_metadata = Base.metadata
```

**5. Crear una Migración:**
Para crear una nueva migración, usa:
```bash
alembic revision --autogenerate -m "Comentario de la migración"
```
Esto generará un archivo en la carpeta `alembic/versions` con los cambios detectados en tu modelo.

**6. Aplicar Migraciones:**
Para aplicar las migraciones a tu base de datos, usa:
```bash
alembic upgrade head
```

#### Ejemplo Básico

**Define tu modelo en `myapp/models.py`:**
```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///mi_base_de_datos.db')
Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    identificacion = Column(String, unique=True)
    telefono = Column(String)
    email = Column(String)

class RegistroEntrada(Base):
    __tablename__ = 'registro_entrada'
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    fecha_entrada = Column(String)
    motivo = Column(String)
    cliente = relationship("Cliente")

Base.metadata.create_all(engine)
```

**Configura Alembic en `alembic/env.py`:**
```python
from myapp.models import Base

# Otras configuraciones

target_metadata = Base.metadata
```

**Crear y aplicar migraciones:**
```bash
alembic revision --autogenerate -m "Inicial"
alembic upgrade head
```

