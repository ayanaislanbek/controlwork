import flet  as ft

def main (page: ft.Page):
    page.title = 'Мое первое приложение'
    greeting_text = ft.Text(value = 'Hello world', color= ft.Colors.RED)

    greeting_text.value = 'Привет'
    greeting_text.color = ft.Colors.GREEN

    page.add(greeting_text)

ft.app(target=main)
