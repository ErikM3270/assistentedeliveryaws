# Assistente de Delivery com AWS Step Functions e Bedrock

Projeto prático do Bootcamp da DIO. O objetivo deste projeto é criar um fluxo de orquestração de pedidos de delivery utilizando a AWS.

# Arquitetura e Serviços Utilizados
- **AWS Step Functions:** Orquestração do fluxo de estados (Validação, Pagamento, IA, Notificação).
- **AWS Lambda:** Execução dos códigos de cada etapa (Python/Boto3).
- **Amazon Bedrock:** Geração de mensagens personalizadas utilizando IA Generativa (Anthropic Claude) para avisar o cliente sobre o status da entrega.

# Como o fluxo funciona
1. Recebe o payload do pedido.
2. A Lambda `ValidarPedido` checa se o pedido tem itens.
3. Se válido, vai para a Lambda `ProcessarPagamento`.
4. Se aprovado, a Lambda `AssistenteBedrock` cria uma mensagem amigável via IA.
5. O fluxo é finalizado com sucesso.

## JSON  (Payload)
json
{
  "cliente": "João Silva",
  "pedido_id": "998877",
  "itens": ["1x Pizza de Calabresa", "1x Guaraná 2L"],
  "total": 65.90
}
