""" #TestField básico exemplo
import flet
from flet import ElevatedButton, Page, Text, TextField, icons


def main(page: Page):
    def button_clicked(e):
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}', '{tb5.value}'."
        page.update()

    t = Text()
    tb1 = TextField(label="Standard")
    tb2 = TextField(label="Disabled", disabled=True, value="First name")
    tb3 = TextField(label="Read-only", read_only=True, value="Last name")
    tb4 = TextField(label="With placeholder",
                    hint_text="Please enter text here")
    tb5 = TextField(label="With an icon", icon=icons.EMOJI_EMOTIONS)
    b = ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(tb1, tb2, tb3, tb4, tb5, b, t)


flet.app(target=main) """

""" #TestField multiline exemplo
import flet
from flet import Page, TextField


def main(page: Page):
    page.add(
        TextField(label="standard", multiline=True),
        TextField(
            label="disabled",
            multiline=True,
            disabled=True,
            value="line1\nline2\nline3\nline4\nline5",
        ),
        TextField(
            label="Auto adjusted height with max lines",
            multiline=True,
            min_lines=1,
            max_lines=3,
        ),
    )


flet.app(target=main)

 """

""" #TestField com evento change exemplo
import flet
from flet import ElevatedButton, Page, Text, TextField

def main(page: Page):
    def textbox_changed(e):
        t.value = e.control.value
        page.update()

    t = Text()
    tb = TextField(
        label="Textbox with 'change' event:",
        on_change=textbox_changed,
    )

    page.add(tb, t)


flet.app(target=main) """

""" #Password.py exemplo
import flet
from flet import Page, TextField

def main(page: Page):
    page.add(
        TextField(
            label="Password with reveal button", password=True, can_reveal_password=True
        )
    )


flet.app(target=main) """

""" """ #Prefix/Sufix exemplo
import flet
from flet import Page, TextField, icons

def main(page: Page):
    page.add(
        TextField(label="With prefix", prefix_text="https://"),
        TextField(label="With suffix", suffix_text=".com"),
        TextField(
            label="With prefix and suffix", prefix_text="https://", suffix_text=".com"
        ),
        TextField(
            label="My favorite color",
            icon=icons.FORMAT_SIZE,
            hint_text="Type your favorite color",
            helper_text="You can type only one color",
            counter_text="0 symbols typed",
            prefix_icon=icons.COLOR_LENS,
            suffix_text="...is your color",
        ),
    )


flet.app(target=main)

""" #TestField style exemplo
import flet as ft

def main(page: ft.Page):
    page.theme_mode = "light"

    def textbox_changed(e):
        t.value = e.control.value
        page.update()

    # ft.TextStyle object has 6 properties: size, weight, italic, font_family, color, bgcolor
    tb = ft.TextField(
        text_style=ft.TextStyle(
            size=15, italic=True, color=ft.colors.DEEP_ORANGE_600, bgcolor='limeaccent200'),

        label="Textbox with 'change' event and style:",
        label_style=ft.TextStyle(
            size=17, weight='bold', italic=True, color=ft.colors.BLUE, bgcolor=ft.colors.RED_700),

        hint_text="hint_text",
        hint_style=ft.TextStyle(size=15, weight='bold', italic=True,
                                color=ft.colors.PINK_ACCENT, bgcolor="brown400"),

        helper_text="helper_text",
        helper_style=ft.TextStyle(
            size=14, weight='bold', color=ft.colors.DEEP_PURPLE, bgcolor=ft.colors.BLUE_50),

        counter_text="counter_text",
        counter_style=ft.TextStyle(
            size=14, italic=True, color=ft.colors.YELLOW, bgcolor=ft.colors.GREEN_500),

        on_change=textbox_changed,
    )

    t = ft.Text()

    page.add(tb, t)


ft.app(target=main)
 """
""" #Underline exemplo
import flet
from flet import Page, TextField

def main(page: Page):
    page.add(
        TextField(label="Underlined", border="underline",
                  hint_text="Enter text here"),
        TextField(
            label="Underlined filled",
            border="underline",
            filled=True,
            hint_text="Enter text here",
        ),
        TextField(label="Borderless", border="none",
                  hint_text="Enter text here"),
        TextField(
            label="Borderless filled",
            border="none",
            filled=True,
            hint_text="Enter text here",
        ),
    )


flet.app(target=main) """
