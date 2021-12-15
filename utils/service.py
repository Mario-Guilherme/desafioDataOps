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
