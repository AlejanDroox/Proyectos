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

class ViewEntrada(ResponsiveRow):
    def __init__(self, page):
        super().__init__()
        self.expand = True
    def draw(self):
        image = Image(src="https://via.placeholder.com/150", col={"sm": 6, "md": 4, "lg": 3})
        text = TextField(
            label='Cedula',
            hint_text='introduce tu cedula',
            col=4,
            height=50,
            width=250
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
            expand=True
        )
        self.controls = [body]
    def build(self):
        self.draw()