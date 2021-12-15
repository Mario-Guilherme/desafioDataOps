from database import Database

import pandas as pd

from typing import Dict

from datetime import datetime

from utils.clean_data import CleanData


class DataService:
    def __init__(self, database: Database) -> None:
        self.database = database
