import requests
import base64


# Configuração da API
API_KEY = "bdd44f38-1974-45f6-bf77-5cb0218056ec"
URL_UPLOAD = f"https://app.clicksign.com/api/v1/documents?access_token={API_KEY}"

def upload_contrato(caminho_pdf):

    with open(caminho_pdf, "rb") as pdf_file:
        pdf_base64 = base64.b64encode(pdf_file.read()).decode("utf-8")
    
    # Dados para envio
    data = {
        "document": {
            "path": f"/{caminho_pdf}",
            "content_base64": f"data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{pdf_base64}",  # Envia o arquivo em Base64
            "deadline_at": None,
            "auto_close": True,
            "locale": "pt-BR",
            "remind_interval": "1"
        }
    }

    headers = {"Content-Type": "application/json"}  # Sem Authorization

    # Faz upload do contrato
    response = requests.post(URL_UPLOAD, json=data, headers=headers)
    
    if response.status_code == 201:
        print("✅ Contrato enviado com sucesso!")
        return response.json()["document"]["key"]  # Retorna a chave do documento
    else:
        print("❌ Erro ao enviar contrato:", response.text)
        return None
    



def criar_signatario(nome, email, cpf, cel):
    URL_SIGNATARIO = f"https://app.clicksign.com/api/v1/signers?access_token={API_KEY}"

    data = {
        "signer": {
            "email": email,
            "phone_number": cel,
            "auths": [
            "email"
            ],
            "name": nome,
            "documentation": cpf,
            "birthday": "1983-03-31",
            "has_documentation": True,
            "selfie_enabled": False,
            "handwritten_enabled": False,
            "location_required_enabled": False,
            "official_document_enabled": False,
            "liveness_enabled": False,
            "facial_biometrics_enabled": False
        }
    }
    headers = {
    "Authorization": f"Bearer {API_KEY}",  # Token no formato correto
    "Content-Type": "application/json",
    "Accept": "application/json"
    }

    response = requests.post(URL_SIGNATARIO, json=data, headers=headers)
    
    if response.status_code == 201:
        return response.json()["signer"]["key"]  # Retorna a chave do signatário
    else:
        print("Erro ao criar signatário:", response.text)
        return None


def adicionar_signatario_ao_contrato(documento_key, signatario_key):
    URL_ADD_SIGNATARIO = f"https://app.clicksign.com/api/v1/lists?access_token={API_KEY}"

    data = {
        "list": {
            "document_key": documento_key,
            "signer_key": signatario_key,
            "sign_as": "sign",
            "message": "teste"
        }
    }
    headers = {
    "Authorization": f"Bearer {API_KEY}",  # Token no formato correto
    "Content-Type": "application/json"
    }

    response = requests.post(URL_ADD_SIGNATARIO, json=data, headers=headers)
    
    if response.status_code == 201:
        
        return response.json()["list"]
    else:
        print("Erro ao adicionar signatário:", response.text)
        return False



def enviar_contrato_para_assinatura(email):

    URL_ENVIAR_CONTRATO = f"https://app.clicksign.com/api/v1/notifications?access_token={API_KEY}"

    data = {
        "request_signature_key": email,
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.post(URL_ENVIAR_CONTRATO, json=data, headers=headers)
    
    if response.status_code == 202:
        print("Contrato enviado para assinatura com sucesso!")
        return True
    else:
        print("Erro ao enviar contrato:", response.text)
        return False

caminho_pdf = "assets/document/Contrato_de_Adesão_Assistência_Funeral1.docx"
# Passo 1: Enviar o contrato e pegar a chave do documento
documento_key = upload_contrato(caminho_pdf)

if documento_key:
    # Passo 2: Criar o signatário
    signatario_key = criar_signatario("teste teste", "leandrofelixf@outlook.com", "45444248875", "11968920238")

    if signatario_key:
        # Passo 3: Vincular signatário ao contrato
        key_sms= adicionar_signatario_ao_contrato(documento_key, signatario_key)
        if key_sms:
            email = key_sms["request_signature_key"]
            url = key_sms["url"]
            enviar_contrato_para_assinatura(email)