import flet as ft
class CustomTextField(ft.TextField):
    def __init__(self, label: str = "Digite algo...", on_change=None):
        super().__init__()
        self.label = label
        self.hint_text = "Digite algo..."
        self.prefix_icon = icon=ft.icons.SEARCH
        self.text_size = 16
        self.on_change = on_change
        self.text_field = ft.TextField(
            label=self.label, on_change=self.on_change)
        self.border_color = ft.colors.BLUE_GREY_600
        self.border_width = 3
        self.text_style = ft.TextStyle(color=ft.colors.BLACK)
        
    def build(self):
        return self.text_field
