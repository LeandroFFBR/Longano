import requests
import base64

# API Key do Avisa API
API_KEY = "SUA_API_KEY_AVISAAPI"

# Base URL da API do Avisa App
BASE_URL = "https://www.avisaapi.com.br/api"

# headers
headers = {
    "Authorization": f"Bearer {API_KEY}",  # Token de autenticação no cabeçalho
    "Content-Type": "application/json"
}

# Função para enviar mensagem via WhatsApp
def zap_boas_vindas(numero, nome_cliente):
    url = f"{BASE_URL}/actions/sendMessage"

    # Mensagem personalizada
    mensagem_1 = f"""
    👩🏻‍💼 Olá {nome_cliente}!
Seguem os documentos para sua adesão:"""

    # Dados da requisição
    payload = {
        "api_key": API_KEY,  # Inclui a API Key para autenticação
        "number": f"55{numero}",  # Número no formato internacional, exemplo: 5511999999999
        "message": mensagem_1.strip()  # Mensagem formatada
    }


    # Enviar requisição POST
    requests.post(url, json=payload, headers=headers)

def zap_pay(numero, url_pay):
    url = f"{BASE_URL}/actions/sendMessage"

    # Mensagem personalizada
    mensagem_1 = f"""
    🏦 *Pagamento pix:*
    {url_pay}

    """

    # Dados da requisição
    payload = {
        "api_key": API_KEY,  # Inclui a API Key para autenticação
        "number": f"55{numero}",  # Número no formato internacional, exemplo: 5511999999999
        "message": mensagem_1.strip()  # Mensagem formatada
    }


    # Enviar requisição POST
    requests.post(url, json=payload, headers=headers)

def zap_cod_barra(numero, pix_json):
    url = f"{BASE_URL}/actions/sendMessage"

    # Mensagem personalizada
    mensagem_1 = pix_json

    # Dados da requisição
    payload = {
        "api_key": API_KEY,  # Inclui a API Key para autenticação
        "number": f"55{numero}",  # Número no formato internacional, exemplo: 5511999999999
        "message": mensagem_1.strip()  # Mensagem formatada
    }


    # Enviar requisição POST
    requests.post(url, json=payload, headers=headers)

def zap_contrato(numero, url_contrato):
    url = f"{BASE_URL}/actions/sendMessage"

    # Mensagem personalizada
    mensagem_1 = f"""Aqui esta seu contrato para assinatura digital:

📜 *Contrato:* {url_contrato}

    """

    # Dados da requisição
    payload = {
        "api_key": API_KEY,  # Inclui a API Key para autenticação
        "number": f"55{numero}",  # Número no formato internacional, exemplo: 5511999999999
        "message": mensagem_1.strip()  # Mensagem formatada
    }


    # Enviar requisição POST
    requests.post(url, json=payload, headers=headers)

def zap_bem_vindo_pdf(numero):
    caminho_pdf = "assets/image/Bem-vindos_à_Longano_Corretora_de_Seguros_pegj1.jpg"
    
    with open(caminho_pdf, "rb") as pdf_file:
        pdf_base64 = base64.b64encode(pdf_file.read()).decode("utf-8")

    url = f"{BASE_URL}/actions/sendImage"

    payload = {
    "api_key": API_KEY,
    "number": f"55{numero}",
    "image": f"data:application/jpg;base64,{pdf_base64}",
    "fileName": "Bem-vindos_à_Longano_Corretora_de_Seguros_pegj1.jpg",
    }

    requests.post(url, json=payload, headers=headers)

