import flet as ft
# Importe do arquivo onde salvou os widgets personalizados
from Custom_Flet_widgets import CustomTextField


def main(page: ft.Page):
    def on_text_change(e):
        print("Texto alterado:", e.control.value)

    text_input = CustomTextField(label="Nome", hint_text="Digite algo...", on_change=on_text_change)

    page.add(text_input)


ft.app(target=main)
