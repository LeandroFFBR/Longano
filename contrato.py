from docx import Document
def auto_contrato(nome, cpf, rua, cep, cel, plano, valor, data, vencimento):
    # Caminho para o documento original
    caminho_doc = 'assets/document/Contrato_de_Adesão_Assistência_Funeral.docx'

    # Carregar o documento
    doc = Document(caminho_doc)

    # Texto original a ser substituído
    texto_original = 'Lucia Maria Delbucio'

    # Novo texto a ser inserido
    novo_texto = f'{nome}\n{cpf}\n{rua}\nCEP: {cep}\nCelular: {cel}\n\n{plano}\nValor do Plano R${valor}\nData de inicio: {data}\nVencimento: {vencimento}'

    # Função para substituir texto em parágrafos
    def substituir_texto(paragrafo, texto_original, novo_texto):
        for run in paragrafo.runs:
            if texto_original in run.text:
                run.text = run.text.replace(texto_original, novo_texto)

    # Iterar sobre os parágrafos do documento
    for paragrafo in doc.paragraphs:
        substituir_texto(paragrafo, texto_original, novo_texto)

    # Salvar o documento modificado
    doc.save('assets/document/Contrato_de_Adesão_Assistência_Funeral1.docx')

auto_contrato("Leandro", "454.442.488-75", "Rua Ministro Carlos Maximiliano", "03523-010", "(11)96892-0238", "Plano Multi Familiar", "79,90", "04/03/2025", "25")