from datetime import datetime

nome_produto: str = "Mesa de Escritório"
quantidade_estoque: int = 10
preco_unitario: float = 450.0
disponivel_venda: bool = True
data_validade: datetime = datetime(2024, 12, 31)

print(data_validade)
print(type(data_validade))