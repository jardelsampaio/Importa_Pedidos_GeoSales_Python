import requests
import json
from requests.auth import HTTPBasicAuth
from config import API_DESTINO_URL, API_DESTINO_USER, API_DESTINO_PASS

def enviar_pedidos(pedidos):
    """
    Envia os pedidos (em formato JSON) para a API de destino Datasul.
    """
    headers = {
        "Content-Type": "application/json"
    }

    try:
        print(f"➡️ Enviando {len(pedidos['PEDIDO'])} pedidos para o endpoint Datasul...")

        response = requests.post(
            API_DESTINO_URL,
            auth=HTTPBasicAuth(API_DESTINO_USER, API_DESTINO_PASS),
            headers=headers,
            data=json.dumps(pedidos)
        )

        print(f"📡 Status: {response.status_code}")
        print(f"Resposta: {response.text}")

        response.raise_for_status()
        print("✅ Pedidos enviados com sucesso!")
        return True

    except requests.exceptions.RequestException as e:
        print("❌ Erro ao enviar pedidos:", e)
        return False
