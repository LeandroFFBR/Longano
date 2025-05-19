import flet as ft 
from tela_login import TelaLogin

def main(page: ft.Page):
    page.window.frameless= True
    page.window.maximized= True
    page.window.full_screen= False
    page.title = "Longano"
    
    # Inicializa a tela de login
    TelaLogin(page)

# Executa o app
ft.app(main)