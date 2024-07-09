---
tags:
  - libreria
  - bases
  - db
fecha: 28/06/2024
---
### SQLAlchemy: Qué es, Ventajas y Desventajas, Implementación y Ejemplos Básicos

#### ¿Qué es SQLAlchemy?

**SQLAlchemy** es un toolkit SQL y ORM (Object-Relational Mapping) para Python. Proporciona una capa de abstracción sobre las bases de datos relacionales, permitiendo a los desarrolladores interactuar con la base de datos usando objetos Python en lugar de escribir consultas SQL directamente.

#### Ventajas de Usar SQLAlchemy

1. **Abstracción del SQL**: Facilita la interacción con la base de datos utilizando código Python, lo que puede mejorar la legibilidad y mantenibilidad del código.
2. **ORM Completo**: Permite mapear las tablas de la base de datos a clases Python, simplificando las operaciones CRUD.
3. **Compatibilidad**: Funciona con una amplia variedad de bases de datos (MySQL, PostgreSQL, SQLite, Oracle, entre otras).
4. **Flexibilidad**: Puedes usarlo tanto en modo ORM como en modo SQL puro.
5. **Soporte para Migraciones**: Integración con herramientas como Alembic para manejar migraciones de esquemas de base de datos.

#### Desventajas de Usar SQLAlchemy

1. **Curva de Aprendizaje**: Puede ser complejo de aprender para principiantes debido a su extensiva funcionalidad.
2. **Sobrecarga**: Introduce una capa adicional de abstracción que puede impactar ligeramente el rendimiento en comparación con el uso directo de SQL.
3. **Comunidad y Documentación**: Aunque tiene una buena comunidad y documentación, puede no ser tan extensa o fácil de seguir como algunas alternativas más simples.

#### Implementación de SQLAlchemy

**Instalación**:
```bash
pip install sqlalchemy
```

**Configuración Básica**:
Aquí hay un ejemplo de cómo configurar y usar SQLAlchemy con SQLite:

```python
# Importar los módulos necesarios
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Crear un motor de base de datos SQLite
engine = create_engine('sqlite:///mi_base_de_datos.db', echo=True)

# Declarar una base
Base = declarative_base()

# Definir los modelos
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

# Crear todas las tablas
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Añadir un nuevo cliente
nuevo_cliente = Cliente(nombre="Juan", apellido="Pérez", identificacion="123456", telefono="555-5555", email="juan.perez@example.com")
session.add(nuevo_cliente)
session.commit()

# Consultar clientes
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(cliente.nombre, cliente.apellido)
```

#### Ejemplo Básico de Uso

**Modelo**:
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Crear un motor de base de datos SQLite
engine = create_engine('sqlite:///mi_base_de_datos.db', echo=True)

# Declarar una base
Base = declarative_base()

# Definir el modelo Cliente
class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)

# Crear todas las tablas
Base.metadata.create_all(engine)
```

**Sesión y Operaciones CRUD**:
```python
from sqlalchemy.orm import sessionmaker

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Crear un nuevo cliente
nuevo_cliente = Cliente(nombre="Ana", apellido="García")
session.add(nuevo_cliente)
session.commit()

# Leer todos los clientes
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(cliente.nombre, cliente.apellido)

# Actualizar un cliente
cliente = session.query(Cliente).filter_by(nombre="Ana").first()
cliente.apellido = "Martínez"
session.commit()

# Eliminar un cliente
cliente = session.query(Cliente).filter_by(nombre="Ana").first()
session.delete(cliente)
session.commit()
```

### Referencias
- [Documentación Oficial de SQLAlchemy](https://www.sqlalchemy.org/)
- [Tutorial de SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)
