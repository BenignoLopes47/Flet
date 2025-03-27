import flet as ft


class ThemedButton(ft.ElevatedButton):
    def __init__(self, text, icon=None, on_click=None):
        super().__init__()
        self.text = text
        self.icon = icon if icon else ft.icons.ADD
        self.on_click = on_click
        self.button_color = "#6200EE"  # Color principal
        self.text_color = "white"
        self.icon_color = "red"

       

    def build(self):
        self.bgcolor = self.button_color
        self.color = self.text_color
