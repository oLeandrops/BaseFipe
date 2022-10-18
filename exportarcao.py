import pandas as pd
from sqlalchemy import create_engine


engine = create_engine(
    'sqlite:///tabelaFipe.db', echo=True)

conexao_sa = engine.connect()

automoveis = pd.read_sql_table('carros',conexao_sa, index_col='id')
automoveis = automoveis.query('mesReferencia=="Mês de Referência Outubro/2022"')
automoveis.to_csv(f'BASE_MES/TabelaFipeOUT2022.csv')
automoveis.to_excel(f'BASE_MES/TabelaFipeOUT2022.xlsx')