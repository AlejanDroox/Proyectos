import flet as ft

def main(page: ft.Page):
    page.title = "Demo ResponsiveRow con Imágenes"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Crear una fila responsiva con imágenes
    responsive_row = ft.ResponsiveRow(
        controls=[
            ft.Image(src="https://via.placeholder.com/150", col={"xs": 12, "sm": 6, "md": 4, "lg": 3}),
            ft.Image(src="https://via.placeholder.com/150", col={"xs": 12, "sm": 6, "md": 4, "lg": 3}),
            ft.Image(src="https://via.placeholder.com/150", col={"xs": 12, "sm": 6, "md": 4, "lg": 3}),
            ft.Image(src="https://via.placeholder.com/150", col={"xs": 12, "sm": 6, "md": 4, "lg": 3}),
        ],
    )

    # Agregar la fila responsiva a la página
    page.add(responsive_row)

ft.app(target=main)
