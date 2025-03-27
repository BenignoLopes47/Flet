import flet as ft 


def main(page: ft.Page):
    page. bgcolor = ft.colors. BLUE_GREY_800
    page.title = "Stack, Image y CircleAvatar"
    page. theme_mode = ft. ThemeMode. DARK
    page.scroll = "always"
    texto_titulo = ft.Text(value="Demostración de Stack, Image y CircleAvatar",
                            size=30, weight=ft.FontWeight.BOLD,
                            color=ft.colors.BLUE_200)

    def create_example(title, description, content):
        return ft. Container(
                content=ft.Column([
                    ft.Text(title, size=24, weight=ft.FontWeight.BOLD,
                            color=ft.colors.BLUE_200),
                    ft.Text(description, color=ft.colors.GREY_300),
                    ft. Container(content=content, padding=10, border=ft.border.all(width= 1, color=ft.colors.BLUE_GREY_400))

                ]),
                margin=ft.margin.only(bottom=20)
        )
    
    stack_ejemplo = ft.Stack( controls= [
        ft.Container(width=200, height=200, bgcolor=ft.colors.BLUE_900),
        ft.Container(width=150, height=150, bgcolor=ft.colors.BLUE_700, left=25, top=25),
        ft.Container(width=100, height=100, bgcolor=ft.colors.BLUE_500, left=50, top=50),
        ft.Text ( value= "Stack Demo", color=ft.colors.WHITE, size=12, left=70, top=90)
    ], width=200, height=200)

    
    stack_example = create_example(title="Stack",
                                   description="Stack permite organizar elementos en una pila, un elemento encima de otro. ",
                                   content=stack_ejemplo)
    
    imagen_internet = ft. Image(src="https://picsum.photos/200/200", width=200)
    imagen_local = ft. Image(src="images/imagem.jpg", width=200)
    columna_imagen = ft.Column([
        imagen_internet,
        ft.Text(value="Imagen desde URL", size=14, color=ft.colors.GREY_300),
        imagen_local,
        ft.Text(value="Imagen local (si esta disponible)", size=14, color=ft.colors.GREY_300)

        ])
    image_example = create_example(title="Image", description="Image muestra imagenes de diferentes fuentes.",
                                    content=columna_imagen)

    imagen_internet_avatar = ft.CircleAvatar(
        foreground_image_src="https://avatars.githubusercontent.com/u/5479691",
        radius=50,
        )
    
    circulo_texto = ft.CircleAvatar(
        content=ft. Text(value="AB", color=ft.colors.BLUE_GREY_800),
        radius=50,
        bgcolor=ft.colors.BLUE_200
    )
    fila = ft.Row([
        imagen_internet_avatar,
        circulo_texto])
    


    circleavatar_example = create_example(
                                          title="CircleAvatar", description="CircleAvatar crea un avatar circular",
                                          content=fila)
    separador = ft.Divider(color=ft.colors.BLUE_GREY_400)

    page.add(texto_titulo, separador, stack_example,separador, image_example,separador, circleavatar_example)







ft.app(target=main)