import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Text(
            value="Olá, Flet!",
            size=24,
            color=ft.colors.RED_400,
            weight=ft.FontWeight.BOLD,
            italic=True,
            text_align=ft.TextAlign.CENTER,
            max_lines=1,
            overflow=ft.TextOverflow.ELLIPSIS,
            selectable=True
        )
    )


ft.app(target=main)
