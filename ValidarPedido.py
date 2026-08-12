import json

def lambda_handler(event, context):
    # Simula a validação do pedido recebido
    itens = event.get('itens', [])
    
    if not itens:
        return {"status": "FALHA", "motivo": "Pedido vazio."}
        
    return {
        "status": "SUCESSO",
        "cliente": event.get('cliente', 'Cliente VIP'),
        "pedido_id": event.get('pedido_id', '12345'),
        "itens": itens,
        "total": event.get('total', 0.0)
    }
