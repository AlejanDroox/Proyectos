from flet import (
    NavigationDrawer,
    NavigationDrawerDestination,
    Icon, icons,
    Divider,
    Container,
    TextButton
)
from utils.globals import DIRECCIONES
class Drawer(NavigationDrawer):
    def __init__(self):
        super().__init__()
        self.controls = [
            Container(height=12),
            NavigationDrawerDestination(
                label="Control de entrada",
                icon=icons.ENGINEERING_OUTLINED,
                selected_icon_content=Icon(icons.ENGINEERING),
            ),
            Divider(thickness=2),
            NavigationDrawerDestination(
                icon_content=Icon(icons.REPORT_OUTLINED),
                label="REGISTRO",
                selected_icon=icons.REPORT,
                
            ),
            NavigationDrawerDestination(
                icon_content=Icon(icons.HELP_OUTLINE_SHARP),
                label="AYUDA",
                selected_icon=icons.HELP,
            ),
        ]
        self.on_change = self.change
    def change(self, e):
        if e.data == '1':
            self.page.go(DIRECCIONES['REGISTRO'])
        elif e.data == '0':
            self.page.go(DIRECCIONES['ENTRADA'])