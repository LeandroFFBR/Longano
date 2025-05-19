import zipfile
from lxml import etree

def substituir_xml(caminho_arquivo_original, caminho_arquivo_novo, nome, cpf, rua, cep, cel, plano, valor, data, vencimento):
    """
    Abre um arquivo DOCX, encontra e substitui 'Lucia' por 'Leandro' no word/document.xml
    usando lxml, e salva o arquivo modificado.

    Args:
        caminho_arquivo_original (str): O caminho para o arquivo DOCX original.
        caminho_arquivo_novo (str): O caminho onde o arquivo modificado será salvo.
    """
    try:
        with zipfile.ZipFile(caminho_arquivo_original, 'r') as zip_ref:
            with zip_ref.open('word/document.xml') as doc_xml:
                xml_content = doc_xml.read()
            file_list = zip_ref.infolist()
            other_files = {item.filename: zip_ref.read(item.filename) for item in file_list if item.filename != 'word/document.xml'}

        tree = etree.fromstring(xml_content)
        namespace = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        substituicoes = 0

        for element in tree.xpath('//*[local-name()="t"]', namespaces=namespace):
            if 'Nome' in element.text:
                element.text = element.text.replace('Nome', nome)

            if 'CPF' in element.text:
                element.text = element.text.replace('CPF', cpf)
            
            if 'Rua' in element.text:
                element.text = element.text.replace('Rua', rua)

            if 'CEP' in element.text:
                element.text = element.text.replace('CEP', f'CEP: {cep}')

            if 'Cel' in element.text:
                element.text = element.text.replace('Cel', f'Cel: {cel}')

            if 'Plano' in element.text:
                element.text = element.text.replace('Plano', f'Plano: {plano}')

            if 'Valor' in element.text:
                element.text = element.text.replace('Valor', f'Valor do plano: R${valor}')

            if 'Data' in element.text:
                element.text = element.text.replace('Data', f'Data: {data}')

            if 'Vencimento' in element.text:
                element.text = element.text.replace('Vencimento', f'Vencimento: Dia {vencimento}')
                substituicoes += 1

        with zipfile.ZipFile(caminho_arquivo_novo, 'w', zipfile.ZIP_DEFLATED) as zip_novo:
            # Escrever o XML modificado
            xml_string = etree.tostring(tree, encoding='utf-8', xml_declaration=True).decode('utf-8')
            zip_novo.writestr('word/document.xml', xml_string)

            # Copiar os outros arquivos
            for filename, content in other_files.items():
                zip_novo.writestr(filename, content)

        print(f"Substituições realizadas: {substituicoes}")
        print(f"Arquivo modificado salvo em: {caminho_arquivo_novo}")

    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em: {caminho_arquivo_original}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


caminho_original = 'assets/document/Contrato_de_Adesão_Assistência_Funeral.docx'
caminho_novo = 'assets/document/Contrato_de_Adesão_Assistência_Funeral_Modificado_XML.docx'