import pandas as pd
from database import Database


class CleanData:
    def __init__(self, data_base: Database) -> None:
        self.data_base = data_base
