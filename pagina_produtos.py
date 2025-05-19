import flet as ft


def PaginaProdutos(page: ft.Page):
    page.bgcolor = "white"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def mostrar_detalhes(titulo, informacao):
        """Função para exibir o diálogo com as informações do seguro."""
        dialog.title = ft.Text(titulo, weight="bold", size=18)
        dialog.content = ft.Text(informacao, size=14)
        dialog.actions = [
            ft.ElevatedButton(
                "OK",
                on_click=lambda _: navegar_cadastro_cliente(titulo)  # Passa o título do plano escolhido
            )
        ]
        dialog.open = True
        page.update()

    def navegar_cadastro_cliente(plano_escolhido):
        """Função para navegar para a tela de cadastro, passando o plano escolhido."""
        dialog.open = False
        page.update()
        from cadastro_cliente import CadastroCliente
        CadastroCliente(page, plano_escolhido)  # Passa o plano como argumento

    def voltar_login(e):
        """Função para voltar à tela de login."""
        from tela_login import TelaLogin
        TelaLogin(page)

    # Diálogo para mostrar informações
    dialog = ft.AlertDialog()

    # Limpa a página para renderizar a tela de produtos
    page.clean()

    # Layout dos botões
    page.add(
    ft.Column(
        [
            ft.Text("Selecione um seguro", size=22, weight="bold"),
            ft.Row(  # Primeira linha com dois botões
                [
                    ft.Container(
                        content=ft.ElevatedButton(
                            content=ft.Column(
                                [
                                    ft.Row([ft.Image(src="assets/image/ind_basico.png", width=100, height=50),
                                    ft.Text("Básico Individual\nR$ 29,90", size=16, weight="bold",color="black")]),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            on_click=lambda _: mostrar_detalhes(
                                "Seguro de Vida Individual Básico",
                                "Sorteio mensal de R$ 5.000,00 para clientes segurados.\n"
                                "Cobertura de até R$ 6.000,00 para despesas funerárias."
                            ),
                            width=280,
                            height=100,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=15),
                                overlay_color=ft.colors.TRANSPARENT,  # Remove efeito de clique padrão
                                bgcolor=ft.colors.TRANSPARENT
                            )
                        ),
                        width=280,
                        height=100,
                        gradient=ft.LinearGradient(
                            colors=["#ff7e5f", "#feb47b"],  # Degradê do laranja para o amarelo
                            begin=ft.alignment.top_left,
                            end=ft.alignment.bottom_right
                        ),
                        border_radius=15
                    ),
                    ft.Container(
                        content=ft.ElevatedButton(
                            content=ft.Column(
                                [
                                    ft.Row([ft.Image(src="assets/image/fami_basico.png", width=100, height=50),
                                    ft.Text("Básico Familiar\nR$ 49,90", size=16, weight="bold",color="black")]),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            on_click=lambda _: mostrar_detalhes(
                                "Seguro de Vida Básico Familiar",
                                "Cobertura: Sorteio mensal de R$ 5.000,00 para clientes segurados.\n"
                                "Cobertura de até R$ 6.000,00 para despesas funerárias.\n"
                                "Seguro morte acidental de R$ 5.000,00."
                            ),
                            width=280,
                            height=100,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=15),
                                overlay_color=ft.colors.TRANSPARENT,
                                bgcolor=ft.colors.TRANSPARENT
                            )
                        ),
                        width=280,
                        height=100,
                        gradient=ft.LinearGradient(
                            colors=["#4facfe", "#00f2fe"],  # Azul degradê
                            begin=ft.alignment.top_left,
                            end=ft.alignment.bottom_right
                        ),
                        border_radius=15
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(  # Segunda linha com dois botões
                [
                    ft.Container(
                        content=ft.ElevatedButton(
                            content=ft.Column(
                                [
                                    ft.Row([ft.Image(src="assets/image/ess_familiar.png", width=100, height=50),
                                    ft.Text("Essencial Familiar\nR$ 79,90", size=16, weight="bold",color="black")]),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            on_click=lambda _: mostrar_detalhes(
                                "Seguro de Vida Essencial Familiar",
                                "Cobertura: Sorteio mensal de R$ 5.000,00 para clientes segurados.\n"
                                "Assistência residencial 24 horas para emergências.\n"
                                "Auxílio-alimentação de R$ 600,00 para apoio em situações inesperadas.\n"
                                "Cobertura de até R$ 6.000,00 para despesas funerárias.\n"
                                "Seguro morte acidental de R$ 5.000,00."
                            ),
                            width=280,
                            height=100,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=15),
                                overlay_color=ft.colors.TRANSPARENT,
                                bgcolor=ft.colors.TRANSPARENT
                            )
                        ),
                        width=280,
                        height=100,
                        gradient=ft.LinearGradient(
                            colors=["#ff9a9e", "#fad0c4"],  # Rosa claro degradê
                            begin=ft.alignment.top_left,
                            end=ft.alignment.bottom_right
                        ),
                        border_radius=15
                    ),
                    ft.Container(
                        content=ft.ElevatedButton(
                            content=ft.Column(
                                [
                                    ft.Row([ft.Image(src="assets/image/multi_fami.png", width=100, height=50),
                                    ft.Text("Multi Familiar\nR$ 120,00", size=16, weight="bold",color="black")]),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            on_click=lambda _: mostrar_detalhes(
                                "Seguro de Vida Multi Familiar",
                                "Cobertura: Sorteio mensal de R$ 5.000,00 para clientes segurados.\n"
                                "Assistência residencial 24 horas para emergências.\n"
                                "Auxílio-alimentação de R$ 600,00 para apoio em situações inesperadas.\n"
                                "Cobertura de até R$ 6.000,00 para despesas funerárias.\n"
                                "Seguro morte acidental de R$ 5.000,00.\n"
                                "Apoio psicológico para cuidar do bem-estar da sua família."
                            ),
                            width=280,
                            height=100,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=15),
                                overlay_color=ft.colors.TRANSPARENT,
                                bgcolor=ft.colors.TRANSPARENT
                            )
                        ),
                        width=280,
                        height=100,
                        gradient=ft.LinearGradient(
                            colors=["#a18cd1", "#fbc2eb"],  # Roxo degradê
                            begin=ft.alignment.top_left,
                            end=ft.alignment.bottom_right
                        ),
                        border_radius=15
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.ElevatedButton(  # Botão de sair
                "Sair",
                on_click=voltar_login,
                bgcolor="black",
                color="white",
                width=150,
                height=50,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=15),
                    elevation=5
                )
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )
)

    # Adiciona o diálogo à página
    page.overlay.append(dialog)
