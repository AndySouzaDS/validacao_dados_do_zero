from datetime import datetime

def validar_tipos(nome_produto, 
                  quantidade_estoque,
                  preco_unitario, 
                  disponivel_venda, 
                  data_validade):
    
    # verificando se o nome do produto é str (retorna um bool)
     if not isinstance(nome_produto, str):
          return False
     
     # verificando se o quantidade_estoque é int (retorna um bool)
     if not isinstance(quantidade_estoque, int):
          return False
     
     # verificando se o preco_unitario é float (retorna um bool)
     if not isinstance(preco_unitario, float):
          return False
     
     # verificando se o disponivel_venda é bool (retorna um bool)
     if not isinstance(disponivel_venda, bool):
          return False
     
     # verificando se o data_validade é str (retorna um bool)
     if not isinstance(data_validade, datetime):
          return False
     
     # verificando se o nome do produto é str (retorna um bool)
     if not isinstance(nome_produto, str):
          return False