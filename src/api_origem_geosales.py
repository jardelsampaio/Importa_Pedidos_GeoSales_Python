import requests
import json
import re
from config import API_ORIGEM_URL, API_ORIGEM_TOKEN

def obter_pedidos():
    """Obtém pedidos e itens da API GeoSales ERP Integrator"""
    url = API_ORIGEM_URL
    headers = {
        "Content-Type": "application/json",
        "SSAUTH_TOKEN": API_ORIGEM_TOKEN
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Corrige vírgulas inválidas
        raw_text = response.text
        clean_text = re.sub(r",(\s*[}\]])", r"\1", raw_text)

        data = json.loads(clean_text)
        pedidos = data.get("PEDIDO", [])
        itens = data.get("ITEM_PEDIDO", [])

        # Agrupa os itens por cd_pedido_palm
        itens_por_pedido = {}
        for item in itens:
            chave = item.get("cd_pedido_palm")
            if chave:
                itens_por_pedido.setdefault(chave, []).append(item)

        # Insere os itens correspondentes dentro de cada pedido
        for pedido in pedidos:
            pedido_id = pedido.get("cd_pedido_palm")
            pedido["itens"] = itens_por_pedido.get(pedido_id, [])

        print(f"✅ {len(pedidos)} pedidos obtidos e agrupados com seus itens.")
        return pedidos

    except json.JSONDecodeError as e:
        print("❌ Erro ao decodificar JSON:", e)
        print("🔎 Resposta bruta da API:", response.text[:500])
        return []

    except requests.exceptions.RequestException as e:
        print("❌ Erro ao obter pedidos:", e)
        return []

# Teste rápido
if __name__ == "__main__":
    pedidos = obter_pedidos()
    print(json.dumps(pedidos, indent=4, ensure_ascii=False))
