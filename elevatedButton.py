<<<<<<< HEAD
""" from flet import ElevatedButton, Page, Text
import flet
from flet import ElevatedButton, Page


def main(page: Page):
    page.title = "Basic elevated buttons"
    page.add(
        ElevatedButton(text="Elevated button"),
        ElevatedButton("Disabled button", disabled=True),
    )


flet.app(target=main) """

""" 
import flet
from flet import ElevatedButton, Page, Text

def main(page: Page):
    page.title = "Elevated button with 'click' event"

    def button_clicked(e):
        b.data += 1
        t.value = f"Button clicked {b.data} time(s)"
        page.update()

    b = ElevatedButton("Button with 'click' event",
                       on_click=button_clicked, data=0)
    t = Text()

    page.add(b, t)


flet.app(target=main) """
""" 
import flet as ft
def main(page: ft.Page):
    page.title = "Elevated buttons with custom content"
    page.add(
        ft.ElevatedButton(
            width=150,
            content=ft.Row(
                [
                    ft.Icon(name=ft.icons.FAVORITE, color="pink"),
                    ft.Icon(name=ft.icons.AUDIOTRACK, color="green"),
                    ft.Icon(name=ft.icons.BEACH_ACCESS, color="blue"),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
        ),
        ft.ElevatedButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value="Compound button", size=20),
                        ft.Text(value="This is secondary text"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                padding=ft.padding.all(10),
            ),
        ),
    )


ft.app(target=main) """


""" 
import flet
from flet import ElevatedButton, Page, Text
def main(page: Page):
    page.title = "Elevated buttons with icons"
    page.add(
        ElevatedButton("Button with icon", icon="chair_outlined"),
        ElevatedButton(
            "Button with colorful icon",
            icon="park_rounded",
            icon_color="green400",
        ),
    )


flet.app(target=main) """


import flet
from flet import (
BorderSide,
ButtonStyle,
ElevatedButton,
Page,
RoundedRectangleBorder,
colors,
)
        
def main(page: Page):
    page.padding = 50
    page.add(
        ElevatedButton(
            "Styled button 1",
            style=ButtonStyle(
                color={
                    "hovered": colors.WHITE,
                    "focused": colors.BLUE,
                    "": colors.BLACK,
                },
                bgcolor={"focused": colors.PINK_200, "": colors.YELLOW},
                padding={"hovered": 20},
                overlay_color=colors.TRANSPARENT,
                elevation={"pressed": 0, "": 1},
                animation_duration=500,
                side={
                    "": BorderSide(1, colors.BLUE),
                    "hovered": BorderSide(2, colors.BLUE),
                },
                shape={
                    "hovered": RoundedRectangleBorder(radius=20),
                    "": RoundedRectangleBorder(radius=2),
                },
            ),
        )
    )


flet.app(target=main)
=======
""" from flet import ElevatedButton, Page, Text
import flet
from flet import ElevatedButton, Page


def main(page: Page):
    page.title = "Basic elevated buttons"
    page.add(
        ElevatedButton(text="Elevated button"),
        ElevatedButton("Disabled button", disabled=True),
    )


flet.app(target=main) """

""" 
import flet
from flet import ElevatedButton, Page, Text

def main(page: Page):
    page.title = "Elevated button with 'click' event"

    def button_clicked(e):
        b.data += 1
        t.value = f"Button clicked {b.data} time(s)"
        page.update()

    b = ElevatedButton("Button with 'click' event",
                       on_click=button_clicked, data=0)
    t = Text()

    page.add(b, t)


flet.app(target=main) """
""" 
import flet as ft
def main(page: ft.Page):
    page.title = "Elevated buttons with custom content"
    page.add(
        ft.ElevatedButton(
            width=150,
            content=ft.Row(
                [
                    ft.Icon(name=ft.icons.FAVORITE, color="pink"),
                    ft.Icon(name=ft.icons.AUDIOTRACK, color="green"),
                    ft.Icon(name=ft.icons.BEACH_ACCESS, color="blue"),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
        ),
        ft.ElevatedButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value="Compound button", size=20),
                        ft.Text(value="This is secondary text"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                padding=ft.padding.all(10),
            ),
        ),
    )


ft.app(target=main) """



import flet
from flet import ElevatedButton, Page, Text
def main(page: Page):
    page.title = "Elevated buttons with icons"
    page.add(
        ElevatedButton("Button with icon", icon="chair_outlined"),
        ElevatedButton(
            "Button with colorful icon",
            icon="park_rounded",
            icon_color="green400",
        ),
    )


flet.app(target=main)
>>>>>>> dc41ba9ca332e234a89dbde6073d990f2f354e0f
