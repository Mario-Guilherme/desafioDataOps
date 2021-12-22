from database import Database

from utils.service import DataService

if __name__ == "__main__":
    database = Database()
    service = DataService(database)
    service.create_file()
