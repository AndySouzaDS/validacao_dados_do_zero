import pandas as pd
from pandas import DataFrame
from schema import InventarioSchema


# tipando como DataFrame - usar essa importacao: from pandas import DataFrame
#minha_tabela: DataFrame = pd.read_excel("data/inventario_mundo.xlsx")

# testando arquivo, sem uma coluna
minha_tabela: DataFrame = pd.read_excel("data/inventario_mundo_sem_coluna.xlsx")

# print(minha_tabela)

try:
    InventarioSchema.validate(minha_tabela)
    # print(minha_tabela)
    print("Excel, validado! Dados consistentes.")
except Exception as e:
    print(f"Erros no schema: {e}")