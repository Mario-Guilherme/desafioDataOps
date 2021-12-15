from database import Database

import pandas as pd

from typing import Dict

from datetime import datetime

from utils.clean_data import CleanData


class DataService:
    def __init__(self, database: Database) -> None:
        self.database = database

    def porcent_situation_cadastral(self) -> float:
        print("Criando a porcentagem da empresas ativas")
        actives = self.database.count_situacao_cadastral_ativa()
        all = self.database.count_all_situacao_cadastral()
        return round(actives / all, 4)

    def transform_to_dataframe(self) -> pd.DataFrame:
        print("Criando dataframe dos restaurantes")
        list_restaurant = list(self.database.query_restaurante())
        df_restaurnt = pd.DataFrame(list_restaurant)
        return df_restaurnt

    def transform_to_datetime(self) -> pd.DataFrame:
        print("Convertando string em data")
        df_date = self.transform_to_dataframe()
        df_date["DATA_DE_INICIO_ATIVIDADE"] = df_date["DATA_DE_INICIO_ATIVIDADE"].apply(
            lambda x: datetime.strptime(str(x), "%Y%m%d")
        )
        return df_date

    def create_column_year(self) -> pd.DataFrame:
        print("Criando coluna de anos")
        df_date = self.transform_to_datetime()
        df_date["ANO_INICIO_ATIVIDADE"] = df_date["DATA_DE_INICIO_ATIVIDADE"].apply(
            lambda x: x.strftime("%Y")
        )
        return df_date

    def group_by_year(self) -> Dict[str, int]:
        print("Criando colunas do ano de inicio da atividade")
        df_date = self.create_column_year()
        df_date_clean = CleanData().clean_year(df_date=df_date)
        df_groupy_date = df_date_clean.groupby(["ANO_INICIO_ATIVIDADE"])[
            ["CNAE_FISCAL_PRINCIPAL"]
        ].count()
        dict_date = df_groupy_date.to_dict()["CNAE_FISCAL_PRINCIPAL"]
        return dict_date

    def create_dataframe_answer(self) -> pd.DataFrame:
        print("Criando dataframe da resposta")
        porcent_cadastral = self.porcent_situation_cadastral()
        restaurant_year = self.group_by_year()
        df_awnser = pd.DataFrame(
            {
                "Empresas Ativas": porcent_cadastral,
                "Empresas abertas por ano": restaurant_year,
            }
        )
        return df_awnser

    def create_csv(self) -> None:
        print("Criando Csv")
        df_anwser = self.create_dataframe_answer()
        df_anwser.to_csv("resposta.csv", index=False)

    def create_excel(self) -> None:
        print("Criando Excel")
        df_anwser = self.create_dataframe_answer()
        df_anwser.to_csv("resposta.xlsx", sheet_name="anwser")
