import pandas as pd


class CleanData:
    def __init__(self) -> None:
        pass

    @staticmethod
    def clean_year(df_date) -> pd.DataFrame:
        data_limite_final = df_date["ANO_INICIO_ATIVIDADE"] <= "2021"
        df_data_clean = df_date[data_limite_final].copy()
        return df_data_clean
