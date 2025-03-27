import flet as ft 

def main(page: ft.Page):
    page.title = "Icons with different colors and sizes"
    def example():

        return ft.Row(
            [
                ft.Icon(name=ft.Icons.FAVORITE, color=ft.Colors.PINK),
                ft.Icon(name=ft.Icons.AUDIOTRACK, color=ft.Colors.GREEN_400, size=30),
                ft.Icon(name=ft.Icons.BEACH_ACCESS, color=ft.Colors.BLUE, size=50),
                ft.Icon(name="settings", color="#c1c1c1"),
            ]
        )

    # Add the example column to the page
    page.add(example())

ft.app(target=main)