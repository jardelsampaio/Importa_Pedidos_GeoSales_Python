from api_origem_geosales import obter_pedidos
from api_destino_erp import enviar_pedidos

def main():
    pedidos = obter_pedidos()
    if pedidos and len(pedidos) > 0:
        print(f"🚀 Enviando {len(pedidos)} pedidos ao ERP...")
        enviar_pedidos({"PEDIDO": pedidos})  # <-- empacota no dicionário
    else:
        print("⚠️ Nenhum pedido encontrado para enviar.")

if __name__ == "__main__":
    main()
