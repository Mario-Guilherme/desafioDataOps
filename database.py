import pymongo
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

    def count_situacao_cadastral_ativa(self):
        return self.__get_database_estabelecimento()["recebimento"].count_documents(
            {"SITUACAO_CADASTRAL": "02"}
        )

    def count_all_situacao_cadastral(self):
        return self.__get_database_estabelecimento()["recebimento"].count_documents({})

    def query_restaurante(self):
        exclude_data = {
            "_id": False,
            "CNPJ_BASICO": False,
            "CNPJ_ORDEM": False,
            "CNPJ_DV": False,
            "IDENTIFICADOR_MATRIZ": False,
            "NOME_FANTASIA": False,
            "SITUACAO_CADASTRAL": False,
            "DATA_SITUACAO_CADASTRAL": False,
            "MOTIVO_SITUACAO_CADASTRAL": False,
            "NOME_DA_CIDADE_NO_EXTERIOR": False,
            "PAIS": False,
            "CNAE_FISCAL_SECUNDARIA": False,
            "TIPO_DE_LOGRADOURO": False,
            "LOGRADOURO": False,
            "NUMERO": False,
            "COMPLEMENTO": False,
            "BAIRRO": False,
            "CEP": False,
            "UF": False,
            "MUNICIPIO": False,
            "DDD_1": False,
            "TELEFONE_1": False,
            "DDD_2": False,
            "TELEFONE_2": False,
            "DDD_DO_FAX": False,
            "FAX": False,
            "CORREIO_ELETRONICO": False,
            "SITUACAO_ESPECIAL": False,
            "DATA_DA_SITUACAO_ESPECIAL": False,
        }

        return self.__get_database_estabelecimento()["recebimento"].find(
            {"CNAE_FISCAL_PRINCIPAL": {"$regex": "^561"}}, projection=exclude_data
        )
