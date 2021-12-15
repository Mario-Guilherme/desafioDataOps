from database import Database

import pandas as pd

from typing import Dict

from datetime import datetime

from utils.clean_data import CleanData


class DataService:
    def __init__(self, database: Database) -> None:
        self.database = database

    def porcent_situation_cadastral(self) -> float:
        actives = self.database.query_situacao_cadastral_ativa()
        all = self.database.query_all_situacao_cadastral()
        return round(actives / all, 4)

    def transform_to_dataframe(self) -> pd.DataFrame:
        list_restaurant = list(self.database.query_restaurante())
        df_restaurnt = pd.DataFrame(list_restaurant)
        return df_restaurnt

    def transform_to_datetime(self) -> pd.DataFrame:
        df_date = self.transform_to_dataframe()
        df_date["DATA_DE_INICIO_ATIVIDADE"] = df_date["DATA_DE_INICIO_ATIVIDADE"].apply(
            lambda x: datetime.strptime(str(x), "%Y%m%d")
        )
        return df_date
