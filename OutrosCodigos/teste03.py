import flet as ft 

def main(page: ft.Page):
    def example():
        return ft.Column(
            controls=[
                ft.FilledButton(text="Filled button"),
                ft.FilledButton("Disabled button", disabled=True),
                ft.FilledButton("Button with icon", icon="add")
            ]
        )
    
    # Add the example column to the page
    page.add(example())

ft.app(target=main)