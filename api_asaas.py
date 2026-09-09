import flet as ft
import requests
import time

#forma de pagamento formagtado
tipo_pag = {"Boleto": "BOLETO", 
            "Cartão de Crédito": "CREDIT_CARD",
            "Cartão de Débito": "DEBIT_CARD",
            "Pix": "PIX"
            }

#plano formatado

plano_abrev = {
    "Seguro de Vida Individual Básico": "S.V Ind. Básico",
    "Seguro de Vida Básico Familiar": "S.V Básico Familiar",
    "Seguro de Vida Essencial Familiar": "S.V Essencial Familiar",
    "Seguro de Vida Multi Familiar": "S.V Multi Familiar"
}
# valor do plano
plano_valor = {
    "Seguro de Vida Individual Básico": 29.90,
    "Seguro de Vida Básico Familiar": 49.90,
    "Seguro de Vida Essencial Familiar": 79.90,
    "Seguro de Vida Multi Familiar": 120.00
}

# função data vencimento dias util:
from datetime import datetime, timedelta
import holidays

def calcular_vencimento(dias=30):
    # Lista de feriados no Brasil
    feriados = holidays.Brazil()
    
    # Data inicial (hoje)
    data_vencimento = datetime.today().date() + timedelta(days=dias)

    # Ajusta para o próximo dia útil
    while data_vencimento.weekday() in (5, 6) or data_vencimento in feriados:
        data_vencimento += timedelta(days=1)
    
    return data_vencimento.strftime("%Y-%m-%d")

vencimento = calcular_vencimento()

#data formato Y-M-D
def data_YMD():
    import datetime
    return datetime.date.today().strftime("%Y-%m-%d")

# data atual
def data_atual():
    import datetime
    return datetime.date.today().strftime("%d/%m/%Y")

# hora atual
def hora_atual():
    import datetime
    return datetime.datetime.now().strftime("%H:%M")


# Sua API Key do Asaas
API_KEY = "SUA_API_KEY_ASAAS"
BASE_URL = "https://api.asaas.com/v3"  # Ambiente real

HEADERS = {
    "accept": "application/json",
    "content-Type": "application/json",
    "access_token": API_KEY
}


def cadastrar_cliente(nome, email, cpf, telefone, endereco, cep, numero, complemento, grupo):
    url = f"{BASE_URL}/customers"
    payload = {
        "name": nome,
        "email": email,
        "cpfCnpj": cpf,
        "mobilePhone": telefone,
        "postalCode": cep,
        "address": endereco,
        "addressNumber": numero,
        "complement": complemento,
        "groupName": grupo
    }

    response = requests.post(url, json=payload, headers=HEADERS)

    if response.status_code == 200:
        return response.json()["id"]  # Retorna o ID do cliente
    else:
        print("Erro ao cadastrar cliente:", response.json())
        return None

def gerar_cobranca(cliente_id, valor,pagamento):
    url = f"{BASE_URL}/payments"
    payload = {
        "customer": cliente_id,
        "billingType": tipo_pag[pagamento],  # Pode ser PIX, BOLETO, etc.
        "value": valor,
        "dueDate": vencimento  # Data de vencimento
    }

    response = requests.post(url, json=payload, headers=HEADERS)

    if response.status_code == 200:
        print(response.json())
        return response.json()  # Retorna a cobrança criada
    else:
        print("Erro ao gerar cobrança:", response.json())
        return None

def nf(cliente_id, valor, data_YMDAY):
    url = f"{BASE_URL}/invoices"

    payload = {
        "taxes": {
        "iss": 2,
        "retainIss": None
        },
        "customer": cliente_id,
        "serviceDescription": "Nota fiscal da Fatura",
        "observations": "Referente  ao Plano",
        "value": valor,
        "effectiveDate": data_YMDAY,
        "deductions": 5,
        "municipalServiceCode": "06130",
        "municipalServiceName": "Corretagem de seguros"
    }

    response = requests.post(url, json=payload, headers=HEADERS)
    print(response.json())
    return response.json()

def boleto(cobranca):

    url = f"{BASE_URL}/payments/{cobranca}/identificationField"

    response = requests.get(url, headers=HEADERS)

    print(response.json())
    return response.json()

def pix(cobranca_id):

    url = f"{BASE_URL}/payments/{cobranca_id}/pixQrCode"

    response = requests.get(url, headers=HEADERS)

    return response.json()

def verificar_pagamento_ate_confirmar(cobranca_id, page):
    # Criando um alerta de carregamento
    loading_indicator = ft.AlertDialog(
        modal=True,  # Impede interação com o fundo
        title=ft.Text("Aguardando pagamento..."),
        content=ft.ProgressRing(width=50, height=50),
    )
    
    page.dialog = loading_indicator  # Adiciona o diálogo na página
    loading_indicator.open = True  # Abre o diálogo
    page.update()  # Atualiza a interface para exibir o diálogo
    
    while True:
        # Verifica o status da cobrança
        response = requests.get(f"{BASE_URL}/payments/{cobranca_id}", headers=HEADERS)
        
        if response.status_code == 200:
            status = response.json().get("status")
            if status == "RECEIVED":
                loading_indicator.open = False  # Fecha o alerta de carregamento
                page.update()
                return "aprovado"
            if status == "CONFIRMED":
                loading_indicator.open = False  # Fecha o alerta de carregamento
                page.update()
                return "confirmado"
            else:
                time.sleep(5)  # Aguarda 5 segundos antes de verificar novamente
        else:
            break
