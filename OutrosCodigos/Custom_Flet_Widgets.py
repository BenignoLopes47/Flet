import flet as ft


class CustomButton(ft.ElevatedButton):
    def __init__(self, text: str, on_click=None, bgcolor="blue", text_color="white"):
        super().__init__()
        self.text = text
        self.on_click = on_click
        self.bgcolor = bgcolor
        self.text_color = text_color
        
    def build(self):
        return ft.ElevatedButton(
            text=self.text,
            bgcolor=self.bgcolor,
            color=self.text_color,
            on_click=self.on_click
        )



class CustomTextField(ft.TextField):
    def __init__(self, label: str, hint_text: str, on_change=None):
        super().__init__()
        self.label = label
        self.hint_text = hint_text
        self.on_change = on_change
        self.text_size = 16
        self.text_style = ft.TextStyle(color=ft.colors.BLACK)
        self.border_color = ft.colors.BLACK45
        self.border_width = 3
        self.bgcolor = ft.colors.WHITE
        self.color = ft.colors.BLACK
        self.cursor_color = ft.colors.BLACK
        self.cursor_width = 2
        self.cursor_height = 20
        
       

    def build(self):
        return ft.TextField(
            label=self.label,
            hint_text=self.hint_text,
            on_change=self.on_change
        )
    

class CustomContainer(ft.Container):
    def __init__(self, content, bgcolor="#FFFFFF", border_radius=10, padding=10, shadow=True):
        super().__init__(
            content=content,
            bgcolor=bgcolor,
            border_radius=border_radius,
            padding=padding,
            shadow=ft.BoxShadow(
                blur_radius=10, color=ft.colors.BLACK26) if shadow else None
        )
