import pandas as pd
from database import Database


class CleanData:
    def __init__(self, data_base: Database) -> None:
        self.data_base = data_base

    def clean_year(self, df_date) -> pd.DataFrame:
        data_limite_final = df_date["ANO_INICIO_ATIVIDADE"] <= "2021"
        df_data_clean = df_date[data_limite_final].copy()
        return df_data_clean
