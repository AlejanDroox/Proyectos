Organizar todas las tablas y la declaración de las mismas en un archivo aparte es una buena práctica. Esto hace que tu código sea más limpio y mantenible. Generalmente, puedes crear un archivo llamado `models.py` o algo similar para definir todos tus modelos.

### Ejemplo de `models.py`

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    email = Column(String)
    contrasena = Column(String)

# Puedes agregar más modelos aquí
```

### Ejemplo de organización de archivos

```
project/
│
├── db_connector.py
├── models.py
├── crud_usuarios.py
└── main.py
```

### `db_connector.py`

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DbConnector:
    """Clase que crea y cierra la conexión"""

    def __init__(self, config):
        self.engine = create_engine(config)
        session = sessionmaker(bind=self.engine)
        self.session = session()

    def close_session(self):
        """Cierra la conexión"""
        if self.session:
            self.session.close()

    def reopen_session(self):
        """Reabre la conexión"""
        if not self.session:
            session = sessionmaker(bind=self.engine)
            self.session = session()
```

### `crud_usuarios.py`

```python
import bcrypt
from models import Usuario

class ControlUsuarios:
    """Clase que maneja las operaciones de los usuarios"""

    def __init__(self, db_connector):
        self.db_connector = db_connector

    def encontrar_usuario(self, nombre):
        """Busca usuario por nombre"""
        return self.db_connector.session.query(Usuario).filter_by(nombre=nombre).first()

    def create_user(self, nombre, email, password):
        """Crea un usuario"""
        usuario = self.encontrar_usuario(nombre)
        if not usuario:
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            nuevo_usuario = Usuario(nombre=nombre, email=email, contrasena=hashed.decode('utf-8'))
            self.db_connector.session.add(nuevo_usuario)
            self.db_connector.session.commit()
        else:
            raise ValueError(f'Ya hay un usuario con el nombre de "{nombre}".')

    def authenticate_user(self, nombre, password):
        """Autentica un usuario"""
        usuario = self.encontrar_usuario(nombre)
        if usuario and bcrypt.checkpw(password.encode('utf-8'), usuario.contrasena.encode('utf-8')):
            return True
        return False

    def update_user_email(self, nombre, nuevo_email):
        """Actualiza el email de un usuario"""
        usuario = self.encontrar_usuario(nombre)
        if usuario:
            usuario.email = nuevo_email
            self.db_connector.session.commit()

    def delete_user(self, nombre):
        """Elimina un usuario por nombre"""
        usuario = self.encontrar_usuario(nombre)
        if usuario:
            self.db_connector.session.delete(usuario)
            self.db_connector.session.commit()

    def get_all_users(self):
        """Obtiene todos los usuarios"""
        return self.db_connector.session.query(Usuario).all()
```

### `main.py`

```python
from db_connector import DbConnector
from models import Base
from crud_usuarios import ControlUsuarios

# Configuración de la base de datos (cambiar a tu configuración deseada)
config = 'sqlite:///mi_base_de_datos.db'

# Crear el conector
db_connector = DbConnector(config)

# Crear las tablas
Base.metadata.create_all(db_connector.engine)

# Crear la instancia de ControlUsuarios
control_usuarios = ControlUsuarios(db_connector)

# Añadir usuarios
control_usuarios.create_user('Juan', 'juan@example.com', 'password123')
control_usuarios.create_user('Maria', 'maria@example.com', 'password456')

# Autenticar usuarios
print(control_usuarios.authenticate_user('Juan', 'password123'))  # True
print(control_usuarios.authenticate_user('Maria', 'wrongpassword'))  # False

# Obtener todos los usuarios
usuarios = control_usuarios.get_all_users()
for usuario in usuarios:
    print(usuario.nombre, usuario.email)

# Actualizar el email de un usuario
control_usuarios.update_user_email('Juan', 'juan_nuevo@example.com')

# Eliminar un usuario
control_usuarios.delete_user('Maria')

# Verificar la eliminación
usuarios = control_usuarios.get_all_users()
for usuario in usuarios:
    print(usuario.nombre, usuario.email)

# Cerrar la sesión
db_connector.close_session()
```

### Actualización de Esquema

Para actualizar el esquema de la base de datos (como agregar una columna), generalmente usarías una herramienta de migración de base de datos. Una de las herramientas más populares para SQLAlchemy es **Alembic**.

#### Pasos para usar Alembic:

1. **Instalación**:

   ```bash
   pip install alembic
   ```

2. **Inicialización**:

   En el directorio raíz de tu proyecto, ejecuta:

   ```bash
   alembic init alembic
   ```

   Esto creará un directorio `alembic` con una configuración inicial.

3. **Configuración**:

   Edita el archivo `alembic.ini` para apuntar a tu base de datos:

```bash
   ini
   sqlalchemy.url = sqlite:///mi_base_de_datos.db
```

4. **Generación de Migración**:

   Cada vez que cambies el esquema de tus modelos, genera una nueva migración:

   ```bash
   alembic revision --autogenerate -m "Agregando columna de ejemplo"
   ```

   Esto creará un archivo de migración en `alembic/versions/`.

5. **Aplicar Migraciones**:

   Aplica las migraciones a la base de datos:

   ```bash
   alembic upgrade head
   ```

#### Ejemplo de agregar una columna:

Supongamos que quieres agregar una columna `edad` a la tabla `Usuario`.

1. **Actualización del Modelo**:

   ```python
   # models.py
   from sqlalchemy import Column, Integer, String
   from sqlalchemy.ext.declarative import declarative_base

   Base = declarative_base()

   class Usuario(Base):
       __tablename__ = 'usuarios'
       id = Column(Integer, primary_key=True)
       nombre = Column(String)
       email = Column(String)
       contrasena = Column(String)
       edad = Column(Integer)  # Nueva columna
   ```

2. **Generación y Aplicación de la Migración**:

   ```bash
   alembic revision --autogenerate -m "Agregando columna edad"
   alembic upgrade head
   ```

Con esto, has actualizado el esquema de tu base de datos para reflejar los cambios en tu modelo.

Si necesitas más detalles sobre cómo configurar Alembic o cualquier otra cosa, no dudes en preguntar.