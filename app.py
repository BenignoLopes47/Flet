import flet as ft

def main(page: ft.Page):
    page.title = "Flet Counter"
    page.add(ft.Text("Hello, World!"))  

ft.app(target=main)