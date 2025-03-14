import flet as ft

def main(page: ft.Page):
    page.title = "Teste"

    
    c1=ft.Container(
            content=ft.Text("Conteiner 1"),
            width=200,
            height=100,
            bgcolor=ft.colors.AMBER_100,
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(10),
            border=ft.border.all(2,ft.colors.RED),
            padding=10
        )
    c2=ft.Container(
            content=ft.Text("Conteiner 2"),
            width=200,
            height=100,
            bgcolor=ft.colors.YELLOW,
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(10),
            border=ft.border.all(2,ft.colors.RED),
            padding=10
        )

    page.add(ft.Row([c1,c2],alignment=ft.MainAxisAlignment.START))



ft.app(target=main)