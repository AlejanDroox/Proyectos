
import flet as ft
from flet import AppBar, ElevatedButton, Page, Text, View, colors, Container
from views.entra import ViewEntrada
from utils.globals import DIRECCIONES
from views.drawer import Drawer
from views.registro import ViewRegistro
def main(page: ft.Page):
    drawer = Drawer()
    barra = AppBar(title=Text("Flet app"), bgcolor=colors.SURFACE_VARIANT)
    def route_change(e):
        
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    Container(ViewEntrada(page), expand=True),
                ],
                appbar=barra,
                drawer=drawer
            )
        )
        if page.route == DIRECCIONES['REGISTRO']:
            page.views.append(
                View(
                    DIRECCIONES['REGISTRO'],
                    [
                        Container(ViewRegistro(page), expand=True)
                    ],
                    appbar=AppBar(title=Text("Store"), bgcolor=colors.SURFACE_VARIANT),
                    drawer=drawer
                )
            )
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.theme_mode = 'light'
    page.go(page.route)
    page.add()

ft.app(target=main)