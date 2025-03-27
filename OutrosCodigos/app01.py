import  flet
from flet import *
from flet import Page, Icons
from customWidgets import ThemedButton


def main(page: Page):
    page.title = "App con Widgets Personalizados"

# Función de ejemplo para manejar evento de click
    def on_button_click(e):
        print("¡Botón presionado!")

    # Crear una instancia de nuestro botón temático
    custom_button = ThemedButton(
        text="Click aquí",
        icon=Icons.FAVORITE,  
        on_click=on_button_click
    )

    # Agregar el botón a la pantalla
    page.add(custom_button)

flet.app(target=main)

