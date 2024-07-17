from flet import (
    ResponsiveRow,
    Column,
    Text,
    TextField,
    Container,
    icons,
    Icon,
    IconButton,
    Image,
    MainAxisAlignment,
    CrossAxisAlignment
)
from views.panel_alerts import PanelAlerts
class ViewRegistro(ResponsiveRow):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.expand = True
        self.panel_alert = PanelAlerts(page)
        page.dialog = self.panel_alert
    def draw(self):
        title = Text(
            value='REGISTRO',
            weight='W_600',
        )
        btn_update_pago = IconButton(
            icon=icons.PAID,
            col=2
        )
        btn_update_lista = IconButton(
            icon=icons.PAID,
            col=2
        )
        btn_update_datos = IconButton(
            icon=icons.PAID,
            col=2
        )
        searh = TextField(
            hint_text='Busqueda por cedula',
            col=3
        )
        linea_acciones = ResponsiveRow(
            [
                btn_update_lista, btn_update_pago, btn_update_datos, searh, TextField
            ]
        )
        body = Column(
            [
                title,
                linea_acciones
            ]
        )
        self.controls = [body]
    def build(self):
        self.draw()
