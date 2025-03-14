import flet as ft
from customRow import CustomRow


class CustomRow(ft.Row):
    def __init__(self, controls=None, spacing=10, alignment=ft.MainAxisAlignment.START, **kwargs):
        super().__init__(controls=controls or [],
                         spacing=spacing, alignment=alignment, **kwargs)


def main(page: ft.Page):
    page.title = "App com CustomRow"
    page.padding = 20

    input_text = ft.TextField(label="Digite algo")
    row = CustomRow()

    def add_item(e):
        if input_text.value.strip():
            row.controls.append(ft.Text(input_text.value))
            input_text.value = ""
            page.update()

    add_button = ft.ElevatedButton("Adicionar", on_click=add_item)

    page.add(input_text, add_button, row)


ft.app(target=main)
