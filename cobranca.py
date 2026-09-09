import requests

ASAAS_API_KEY = "SUA_API_KEY_ASAAS"
ASAAS_BASE_URL = "https://sandbox.asaas.com/api/v3"

def criar_cliente(nome, email, telefone, cpf):
    """Cria um cliente no Asaas."""
    url = f"{ASAAS_BASE_URL}/customers"
    headers = {
        "Content-Type": "application/json",
        "access_token": ASAAS_API_KEY
    }
    payload = {
        "name": nome,
        "email": email,
        "phone": telefone,
        "cpfCnpj": cpf,
        "personType": "FISICA"  # ou "JURIDICA" para empresas
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200 or response.status_code == 201:
        return response.json()  # Retorna os dados do cliente criado
    else:
        print("Erro ao criar cliente:", response.text)
        return None

def criar_cobranca(cliente_id, valor, descricao):
    """Gera uma cobrança no Asaas."""
    url = f"{ASAAS_BASE_URL}/payments"
    headers = {
        "Content-Type": "application/json",
        "access_token": ASAAS_API_KEY
    }
    payload = {
        "customer": cliente_id,
        "billingType": "PIX",  # Ou "BOLETO", "CREDIT_CARD"
        "dueDate": "2025-01-30",  # Data de vencimento
        "value": valor,
        "description": descricao
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200 or response.status_code == 201:
        return response.json()  # Retorna os dados da cobrança
    else:
        print("Erro ao criar cobrança:", response.text)
        return None
