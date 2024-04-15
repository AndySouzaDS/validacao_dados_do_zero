from datetime import datetime
from modulo_validador import validar_tipos

nome_produto: str = "Mesa de Escritório"
quantidade_estoque: int = 10
preco_unitario: float = 450.0
disponivel_venda: bool = True
data_validade: datetime = datetime(2024, 12, 31)

resultado = validar_tipos(nome_produto, 
                           quantidade_estoque, 
                           preco_unitario, 
                           disponivel_venda, 
                           data_validade)

print(resultado)