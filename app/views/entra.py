from flet import (
    ResponsiveRow,
    Column,
    Container,
    CrossAxisAlignment,
    MainAxisAlignment,
    padding,
    TextField,
    Text,
    Image,
)
from views.panel_alerts import PanelAlerts
class ViewEntrada(ResponsiveRow):
    def __init__(self, page):
        super().__init__()
        self.expand = True,
        self.panel_alert = PanelAlerts(page)
        page.dialog = self.panel_alert
    def draw(self):
        def search(e):
            #logica de buscar los datos correspondientes a la ci en la bd
            #self.panel_alert.show_banner(False, 'pruebita')
            self.panel_alert.open_alert()
        image = Image(
            src=r'app\assets\logo_temporal.jpeg',
            col={"sm": 6, "md": 4, "lg": 3},
            height=150,
            border_radius=18)
        text = TextField(
            label='Cedula',
            hint_text='introduce tu cedula',
            col=4,
            height=50,
            width=250,
            on_submit=search
        )
        containerfield = Container(
            content=text,
            padding=padding.only(bottom=220)
        )
        promo = Text(
            value='Este software fue desarrollado por (hay que pensar un nombre wn)',
    
        )
        body = Column(
            [
                image,
                containerfield,
                promo
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            expand=True,
        )
        self.controls = [body]
    def build(self):
        self.draw()