from flet import (
    AlertDialog, Page, TextButton, Text, Icon, icons,colors, Column, Row, MainAxisAlignment, CrossAxisAlignment, Banner
)

class PanelAlerts(AlertDialog):
    """
    Un controlador para gestionar distintos tipos de AlertDialog.
    Crea alert dialogs básicos y los guarda en variables.
    """
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.STYLE_BANNER_ERROR = {
            'bgcolor': colors.AMBER_100,
            'leading': Icon(icons.WARNING_AMBER_ROUNDED, color=colors.AMBER, size=40),
            'actions': [TextButton("Aceptar", on_click=self.close_banner)]
        }
        self.STYLE_BANNER_FINE = {
            'bgcolor': colors.BLUE_100,
            'leading': Icon(icons.CHECK, color=colors.AMBER, size=40),
            'actions': [TextButton("Aceptar", on_click=self.close_banner)],
        }
        self.msg_error_unexp = 'Ha ocurrido un error inesperado. Inténtelo nuevamente.\nSi el error persiste, llame a servicio técnico.'
        self.alerts = {}
        self.draw_basic_alerts()
        self.content = self.alerts['example']
    def draw_basic_alerts(self):
        """Crea alert dialogs básicos y los guarda en variables."""
        self.alerts['example'] = self.draw_example_alert()
        self.alerts['error'] = self.draw_error_alert()

    def draw_example_alert(self):
        """Crea un alert dialog de ejemplo."""
        title = Text("Ejemplo de Alerta", size=24)
        content = Text("Este es un ejemplo de alerta.")
        btn_aceptar = TextButton(text='Aceptar', on_click=lambda _: self.close())
        
        body = Column(
            [
                title,
                content,
                Row([btn_aceptar], alignment=MainAxisAlignment.CENTER),
            ],
            width=400,
            height=200,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER
        )
        return body

    def draw_error_alert(self):
        """Crea un alert dialog para mostrar errores."""
        title = Text("Error", size=24, color=colors.RED)
        content = Text(self.msg_error_unexp)
        btn_aceptar = TextButton(text='Aceptar', on_click=lambda _: self.close())
        
        body = Column(
            [
                title,
                content,
                Row([btn_aceptar], alignment=MainAxisAlignment.CENTER),
            ],
            width=400,
            height=200,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER
        )
        return body

    def set_custom_alert(self, body_alert, name_alert: str):
        """
        Agrega una alerta personalizada a la clase PanelAlerts.
        
        Args:
            body_alert: El contenido del alert dialog personalizado.
            name_alert (str): El nombre con el que se identificará la alerta.
        
        Example:
            custom_body = Column([
                Text("Alerta Personalizada", size=24, weight='w_600'),
                Text("Este es el contenido de la alerta personalizada."),
                TextButton("Cerrar", on_click=lambda _: panel_alerts.close())
            ])
            panel_alerts.set_custom_alert(custom_body, "custom_alert")
        """
        exist = self.alerts.get(name_alert, False)
        if exist:
            raise Exception(f"El nombre {name_alert} ya se encuentra en uso, considere usar otro")
        self.alerts[name_alert] = body_alert

    def change_alert(self, alert_name):
        """Cambia el contenido del AlertDialog según el nombre especificado."""
        self.content = self.alerts.get(alert_name)
        self.open = True
        self.page.update()

    def show_banner(self, is_error: bool, text: str):
        """Muestra un banner con un mensaje específico."""
        style = self.STYLE_BANNER_ERROR if is_error else self.STYLE_BANNER_FINE
        self.page.banner = Banner(content=Text(text), **style)
        self.page.banner.open = True
        self.page.update()
    def open_alert(self):
        self.open = True
        self.page.update()
    def close_banner(self, e):
        """Cierra el banner actualmente abierto."""
        self.page.banner.open = False
        self.page.update()

    def close(self, *entries):
        """Cierra el AlertDialog y limpia las entradas especificadas."""
        for entry in entries:
            entry.value = ''
        self.open = False
        self.page.update()
