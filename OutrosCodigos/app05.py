import flet as ft
from Custom_Flet_Widgets import CustomContainer


def main(page: ft.Page):
    page.title = "Aplicação CustomContainer"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#F0F0F0"

    container1 = CustomContainer(
        content=ft.Text("Este é um container personalizado!",
                        size=20, color="black"),
        bgcolor="#FFDDC1",
        border_radius=15,
        padding=20,
        shadow=True
    )

    container2 = CustomContainer(
        content=ft.Text("Outro exemplo de container", size=18, color="blue"),
        bgcolor="#C1DFFF",
        border_radius=25,
        padding=15,
        shadow=True
    )

    page.add(
        ft.Column([
            container1,
            container2
        ], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)
