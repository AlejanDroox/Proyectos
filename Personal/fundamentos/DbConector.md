```python
class DbConnector:

    """clase que crea y cierra la Conexion"""

    def __init__(self, config):

        self.engine = create_engine(config)

        session = sessionmaker(bind=self.engine)

        self.session = session()
    def close_session(self):

        """cierra la Conexion """

        if self.session:

            self.session.close()

    def reopen_session(self):

        """reabre la Conexion """

        if not self.session:

            session = sessionmaker(bind=self.engine)

            self.session = session()
```
Esto es prácticamente es el controlador de la conexión con la base de datos,