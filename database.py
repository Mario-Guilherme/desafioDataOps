from utils.singleton import Singleton

from config import DevelopmentConfig

from pymongo import MongoClient, errors


class Database(metaclass=Singleton):
    def __init__(self) -> None:

        try:
            self.__client = MongoClient(
                DevelopmentConfig.DATABASE_URI,
                serverSelectionTimeoutMS=DevelopmentConfig.TIME_OUT,
            )
        except errors.ServerSelectionTimeoutError as err:
            raise ("pymongo ERROR:", err)

    def __get_database_estabelecimento(self):
        return self.__client["Recebimento"]

    def insert_estabelecimento(self, data) -> None:
        self.__get_database_processed_images()["recebimento"].insert_one(data)

    def query_situacao_cadastral_ativa(self):
        return self.__get_database_estabelecimento()["recebimento"].find(
            {"SITUACAO_CADASTRAL": "02"}
        )
