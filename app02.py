import flet as ft
from custom_textfield import CustomTextField

def main(page: ft.Page):
    def on_text_change(e):
        print("Texto alterado:", e.control.value)

    text_input = CustomTextField(label="Nome")

    page.add(text_input)


ft.app(target=main)
