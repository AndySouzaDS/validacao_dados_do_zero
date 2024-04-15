import pandas as pd
from pandas import DataFrame
from schema import InventarioSchema
import streamlit as st
import sqlite3

def main():
    st.title("Esse é meu projeto de Python do Zero")

    arquivo = st.file_uploader("Selecione o arquivo de Excel, para validação!", type=["xlsx"])
    if arquivo is not None:
        data_frame = pd.read_excel(arquivo)

        try:
            InventarioSchema.validate(data_frame)
            st.success("Excel, validado! Dados consistentes.")

            if st.button("Salvar no Banco"):
                # Criando uma conexão com o banco de dados SQLite
                con = sqlite3.connect("inventario.db")
                # declarando que o arquivo que será enviado será o data_frame
                    # inventario.db - banco de dados; 
                    # inventario - nome do arquivo (tabela), que será salvo, caso a
                        # a tabela exista, será sobreescrita
                data_frame.to_sql("inventario", con, if_exists='replace', index=False)
                st.success("Dados salvos com sucesso no banco de dados!")
                con.close()

        except Exception as e:
            st.error(f"Erros no schema: {e}")

if __name__ == "__main__":
    main()
