import pymongo
from pymongo import MongoClient
import uuid


class Model:

    def __init__(self):
        cluster = MongoClient(
            "mongodb+srv://gsmatos2014:xllnaSaLVssAXYvy@clustergabrielsm.yyg6p8a.mongodb.net/?retryWrites=true&w=majority")
        db = cluster["CaixaDeCartas"]
        self.collectionLogin = db["Login"]
        self.collectionObras = db["Obras"]

    def computarRegistro(self, nome, senha):
        result = self.collectionLogin.find_one({"Usuario": nome})

        if result == None:
            self.collectionLogin.insert_one({"Usuario": nome, "Senha": senha})
            return True
        return False

    def computarLogin(self, nome, senha):
        result = self.collectionLogin.find_one(
            {"Usuario": nome, "Senha": senha})

        if result == None:
            return False
        return True

    def addObra(self, nome, nomeObra, comentario, genero, nota, status, tipo):
        max_id_result = self.collectionObras.find_one(sort=[("_id", -1)])
        result = self.collectionObras.find_one({"Nome": nomeObra})

        if max_id_result is None:
            new_id = 1
        else:
            new_id = max_id_result["_id"] + 1

        if result == None:
            self.collectionObras.insert_one({"_id": new_id, "Usuario": nome, "Nome": nomeObra, "Comentario": comentario,
                                            "Genero": genero, "Nota": nota, "Status": status, "Tipo": tipo})
            return True
        return False

    def get_all_obras(self, position):
        result = []
        for x in self.collectionObras.find({}, {"_id": 0, "Nome": position, "Comentario": position, "Nota": position}):
            nome = x.get("Nome", "")
            comentario = x.get("Comentario", "")
            nota = x.get("Nota", "")

            result.append(
                f"Nome: {nome} Comentario: {comentario} Nota: {nota}")
        return result
