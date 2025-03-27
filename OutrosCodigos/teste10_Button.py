import flet as ft


def main(page: ft.Page):
    def botao_clicado(e):
        print("Botão pressionado!")
    btn = ft.ElevatedButton(
        text="Clique Aqui",
        icon=ft.icons.PLAY_ARROW,
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        on_click=botao_clicado
    )

    page.add(btn)


ft.app(target=main)
