import pandas as pd
from pandas import DataFrame

# tipando como DataFrame
minha_tabela: DataFrame = pd.read_excel("data/inventario_mundo.xlsx")

print(minha_tabela)
