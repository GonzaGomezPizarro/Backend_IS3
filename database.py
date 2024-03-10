from pymongo import MongoClient, ASCENDING
from pymongo.errors import OperationFailure

class MongoDB:
    def __init__(self, host, port, username, password, database_name):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database_name = database_name

        # Configura la conexión a MongoDB con autenticación
        self.client = MongoClient(host, port, username=username, password=password)
        self.db = self.client[database_name]

        # Agrega un índice único al campo 'username' si no existe
        try:
            self.db.users.create_index([('username', ASCENDING)], unique=True)
        except OperationFailure as e:
            print(f"Error al crear el índice único: {e}")

    def insert_user(self, user):
        result = self.db.users.insert_one(user)
        return str(result.inserted_id)

    def get_user(self, username):
        return self.db.users.find_one({"username": username})

    def get_users(self):
        return list(self.db.users.find())

# Configuración de autenticación
mongo = MongoDB("localhost", 27017, "root", "CONTRASENA", "usuarios")
