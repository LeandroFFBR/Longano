import flet as ft

def CadastroCliente(page: ft.Page, plano_escolhido):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    plano_escolhido = str(plano_escolhido)

    caminho_original = 'assets/document/Contrato_de_Adesão_Assistência_Funeral.docx'
    caminho_novo = 'assets/document/Contrato_de_Adesão_Assistência_Funeral_Modificado_XML.docx'

    def formatar_cep(e):
        texto = cep_input.value.replace("-", "")[:8]
        formatado = (
            f"{texto[:5]}-{texto[5:]}" if len(texto) > 5 else texto
        )
        cep_input.value = formatado
        page.update()

    def formatar_cpf(e):
        """Formata automaticamente o campo CPF enquanto o usuário digita."""
        texto = cpf_input.value.replace(".", "").replace("-", "")[:11]  # Remove pontos e traços e limita a 11 caracteres
        formatado = (
            f"{texto[:3]}.{texto[3:6]}.{texto[6:9]}-{texto[9:]}" if len(texto) > 9 else
            f"{texto[:3]}.{texto[3:6]}.{texto[6:]}" if len(texto) > 6 else
            f"{texto[:3]}.{texto[3:]}" if len(texto) > 3 else texto
        )
        cpf_input.value = formatado
        page.update()

    def formatar_data(e):
        """Formata automaticamente o campo Data enquanto o usuário digita."""
        texto = data_input.value.replace("/", "")[:8]  # Remove barras e limita a 8 caracteres
        formatado = (
            f"{texto[:2]}/{texto[2:4]}/{texto[4:]}" if len(texto) > 4 else
            f"{texto[:2]}/{texto[2:]}" if len(texto) > 2 else texto
        )
        data_input.value = formatado
        page.update()

    def formatar_telefone(e):
        """Formata automaticamente o campo Telefone enquanto o usuário digita."""
        texto = telefone_input.value.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")[:11]
        formatado = (
            f"({texto[:2]}) {texto[2:7]}-{texto[7:]}" if len(texto) > 7 else
            f"({texto[:2]}) {texto[2:]}" if len(texto) > 2 else texto
        )
        telefone_input.value = formatado
        page.update()

    def salvar_dados(e):
        loading_indicator = ft.AlertDialog(
        modal=True,  # Impede interação com o fundo
        title=ft.Text("um minuto por favor..."),
        content=ft.ProgressRing(width=50, height=50),
        )
        page.overlay.append(loading_indicator)
        loading_indicator.open = True
        page.update()
        loading_indicator.title = ft.Text("importando contrato1")
        page.update()
        from contrato1 import substituir_xml
        loading_indicator.title = ft.Text("importando avisaapi")
        page.update
        from avisaapi import zap_boas_vindas, zap_pay, zap_contrato, zap_bem_vindo_pdf
        loading_indicator.title = ft.Text("importando clicksign")
        page.update()
        from clicksign import upload_contrato, criar_signatario, adicionar_signatario_ao_contrato
        loading_indicator.title = ft.Text("importando api_asaas")
        page.update()
        from api_asaas import cadastrar_cliente, gerar_cobranca, data_atual, hora_atual, nf, pix, plano_abrev, plano_valor, data_YMD
        loading_indicator.title = ft.Text("importando firebase")
        page.update()
        from firebase import iniciar_firebase
        loading_indicator.title = ft.Text("importações concluidas")
        page.update()
        db = iniciar_firebase()
        loading_indicator.title = ft.Text("iniciando firebase")
        page.update()
        data_YMDAY = data_YMD()
        data = data_atual()
        hora = hora_atual()

        substituir_xml(caminho_original, caminho_novo, nome_input.value, cpf_input.value, endereco_input.value, cep_input.value, telefone_input.value, plano_escolhido, plano_valor[plano_escolhido], data, "25")
        
        plano = plano_abrev[plano_escolhido]

        cliente_id = cadastrar_cliente(nome_input.value,email_input.value, cpf_input.value.replace(".", "").replace("-",""), telefone_input.value.replace("(", "").replace(")","").replace("-", ""), endereco_input.value, cep_input.value, numero.value, complemento.value, plano_escolhido)
        if cliente_id:
            cobranca = gerar_cobranca(cliente_id, 9.90, pagamento_dropdown.value)
            if cobranca:
                pix_json= pix(cobranca["id"])
                url_pay = cobranca["invoiceUrl"]
                nf(cliente_id, 9.90, data_YMDAY)
                contrato_id = upload_contrato("assets/document/Contrato_de_Adesão_Assistência_Funeral_Modificado_XML.docx")
                signatario_id = criar_signatario(nome_input.value, email_input.value, cpf_input.value.replace(".", "").replace("-",""), telefone_input.value.replace("(", "").replace(")", "").replace("-", ""))
                url_contrato = adicionar_signatario_ao_contrato(contrato_id,signatario_id)
                cel_zap = telefone_input.value.replace("(", "").replace(")", "").replace("-", "")
                zap_boas_vindas(cel_zap, nome_input.value)
                zap_pay(cel_zap, url_pay)
                zap_contrato(cel_zap, url_contrato["url"])
                zap_bem_vindo_pdf(cel_zap)
                if pix_json:
                    try:
                        """Salva os dados no banco de dados e exibe uma mensagem de sucesso."""
                        cliente_data = {
                            "nome": nome_input.value,
                            "cpf": cpf_input.value,
                            "data_nascimento": data_input.value,
                            "telefone": telefone_input.value,
                            "Cep": cep_input.value,
                            "endereco": endereco_input.value,
                            "numero": numero.value,
                            "complemento": complemento.value,
                            "email": email_input.value,
                            "farmaceutico_responsavel": farmaceutico_input.value,
                            "forma_pagamento": pagamento_dropdown.value,
                            "status_pagamento": "",
                            "data_atual": data,
                            "hora_atual": hora,
                            "id_cliente": cliente_id,
                            "id_pag_pix": cobranca["id"],
                            "contrato_id": contrato_id,
                            "signatario_id": signatario_id,
                            "url_contrato": url_contrato
                        }
                        cliente_data["status_pagamento"] = cobranca["status"]
                        db.collection(plano).add(cliente_data)
                        # Exibe o popup de sucesso e limpa os campos
                        def fechar_popup(e):
                            page.close(sucesso_dialog)
                            CadastroCliente(page, plano_escolhido)
                        loading_indicator.open = False
                        page.update()
                        sucesso_dialog = ft.AlertDialog(
                            title=ft.Text("Sucesso"),
                            content=ft.Text("Dados cadastrados com sucesso!"),
                            actions=[
                                ft.ElevatedButton("OK", on_click=fechar_popup)
                            ],
                        )
                        page.overlay.append(sucesso_dialog)
                        sucesso_dialog.open = True
                        page.update()
                    except Exception as e:
                        print(f"Erro ao salvar dados: {e}")
                        erro_dialog = ft.AlertDialog(
                            title=ft.Text("Erro"),
                            content=ft.Text("Erro ao salvar os dados! Por favor, tente novamente."),
                            actions=[
                                ft.ElevatedButton("OK", on_click=lambda _: page.dialog.close())
                            ],
                        )
                        page.dialog = erro_dialog
                        erro_dialog.open = True
                        page.update()

    def voltar_produtos(e):
        """Volta para a página de produtos."""
        from pagina_produtos import PaginaProdutos
        PaginaProdutos(page)

    # Campos de entrada
    nome_input = ft.TextField(label="Nome Completo", width=350)
    cpf_input = ft.TextField(label="CPF", width=350, on_change=formatar_cpf)
    data_input = ft.TextField(label="Data de Nascimento", width=350, on_change=formatar_data)
    telefone_input = ft.TextField(label="Telefone", width=350, on_change=formatar_telefone)
    cep_input = ft.TextField(label="CEP", width=350, on_change=formatar_cep)
    endereco_input = ft.TextField(label="Endereço", width=350)
    complemento = ft.TextField(label="Complemento", width=140)
    numero= ft.TextField(label="Nº", width=70)
    email_input = ft.TextField(label="E-mail", width=350)
    farmaceutico_input = ft.TextField(label="Farmacêutico(a) Responsável", width=350)

    # Dropdown para a forma de pagamento
    pagamento_dropdown = ft.Dropdown(
        label="Forma de Pagamento",
        width=350,
        options=[
            ft.dropdown.Option("Pix")
        ],
    )

    # Limpa a página para renderizar a tela de cadastro
    page.clean()

    # Layout da página
    page.add(
        ft.Column(
            [
                ft.Text(f"Cadastro de Cliente - {plano_escolhido}", size=20, weight="bold"),
                nome_input,
                cpf_input,
                data_input,
                telefone_input,
                cep_input,
                ft.Row(
                [ft.Container(endereco_input, margin= ft.margin.only(left=210)),
                 ft.Container(numero),
                 ft.Container(complemento)],
                 spacing=2,
                 alignment=ft.MainAxisAlignment.CENTER),
                email_input,
                farmaceutico_input,
                pagamento_dropdown,
                ft.Row(
                    [
                        ft.ElevatedButton("Finalizar o Cadastro", on_click=salvar_dados, bgcolor="green", color="white"),
                        ft.ElevatedButton("Voltar", on_click=voltar_produtos, bgcolor="red", color="white"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )
