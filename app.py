import flet as ft
def main(page: ft.Page):
    page.title = "Hello world!"
    page.add(ft.Text("Hello World!")) 

    def button_click(e):
        page.add(ft.Text("Hello World!"))

    page.add(ft.ElevatedButton("Click me", on_click=button_click))  
ft.app(target=main)