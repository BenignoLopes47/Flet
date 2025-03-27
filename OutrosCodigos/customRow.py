
import flet as ft


class CustomRow(ft.Row):
    def __init__(self,controls=None, spacing=10, alignment=ft.MainAxisAlignment.START, **kwargs):
        super().__init__(**kwargs)
        self.controls = controls if controls else []
        self.spacing = spacing
        self.alignment = alignment
        self.color=ft.colors.BLACK
        self.bgcolor=ft.colors.WHITE
        self.border_radius=ft.border_radius.all(5)
        self.scroll=ft.ScrollMode.ALWAYS