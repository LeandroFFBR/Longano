import flet as ft

# Dados de exemplo para autenticação
USUARIOS_VALIDOS = {
    "farmacia123": "senha123",
    "farmacia456": "senha456"
}

def TelaLogin(page: ft.Page):
    page.window.always_on_top= True
    page.bgcolor = "transparent"
    page.decoration = ft.BoxDecoration(
        image= ft.DecorationImage(
            src= "assets/image/capa_login.png",
            fit= ft.ImageFit.COVER,
        )
    )
    def autenticar(e):
        usuario = usuario_input.value
        senha = senha_input.value

        if usuario in USUARIOS_VALIDOS and USUARIOS_VALIDOS[usuario] == senha:
            from pagina_produtos import PaginaProdutos
            PaginaProdutos(page)  # Redireciona para a próxima página
        else:
            mensagem.value = "Usuário ou senha inválidos."
            mensagem.color = "red"
            page.update()

    def alternar_visibilidade_senha(e):
        senha_input.password = not senha_input.password
        icone_olho.icon = "visibility" if not senha_input.password else "visibility_off"
        page.update()

    # Limpa a página para renderizar a tela de login
    page.clean()

    # Campos de entrada
    usuario_input = ft.TextField(label="Usuário", width=300, bgcolor="white")
    senha_input = ft.TextField(label="Senha", password=True, width=300, color="white", bgcolor="blue900")

    # Ícone para mostrar/ocultar senha
    icone_olho = ft.IconButton(
        icon="visibility_off",  # Ícone inicial (senha oculta)
        on_click=alternar_visibilidade_senha
    )

    # Mensagem de erro/sucesso
    mensagem = ft.Text("", size=14)

    # Botão de login
    botao_entrar = ft.ElevatedButton("Entrar", on_click=autenticar)

    # Layout da tela de login
    page.add(
        ft.Column(
            [
                ft.Image(
                    src="assets/image/logo_longano.png",
                    width=250,  # Largura do logotipo
                    height=250,  # Altura do logotipo
                    fit=ft.ImageFit.CONTAIN  # Ajusta a imagem dentro do tamanho especificado
                ),
                ft.Text("Login", size=20),
                usuario_input,
                ft.Row([ft.Container(senha_input, margin=ft.margin.only(left=50)), ft.Container(icone_olho)], alignment=ft.MainAxisAlignment.CENTER),
                botao_entrar,
                mensagem
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )
    page.update()
