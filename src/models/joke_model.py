import random
from .db import db
from .abstract_model import AbstractModel


class JokeModel(AbstractModel):
    # Define que a Coleção do Banco se chamara jokes.
    # Uma coleção é o equivalente a uma tabela no Mysql
    _collection = db["jokes"]

    # Nosso construtor receberá um dicionário (JSON)
    # para instanciar um objeto
    def __init__(self, json_data):
        super().__init__(json_data)
    
    @classmethod
    def get_random(cls):
        data = cls.find()
        if not data:
            return
        return random.choice(data)
    
    def to_dict(self):
        return {
            "_id": str(self.data["_id"]),
            "joke": self.data["joke"],
        }
