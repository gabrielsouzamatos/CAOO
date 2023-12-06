import pymongo
from pymongo import MongoClient


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
        maxIdResult = self.collectionObras.find_one(sort=[("_id", -1)])
        result = self.collectionObras.find_one({"Nome": nomeObra})

        if maxIdResult is None:
            newId = 1
        else:
            newId = maxIdResult["_id"] + 1

        if result == None:
            self.collectionObras.insert_one({"_id": newId, "Usuario": nome, "Nome": nomeObra, "Comentario": comentario,
                                            "Genero": genero, "Nota": nota, "Status": status, "Tipo": tipo})
            return True
        return False

    def getObraUser(self, usuario):
        result = []
        for x in self.collectionObras.find({"Usuario": usuario}, {"_id": 1, "Nome": 1, "Comentario": 1, "Nota": 1}):
            obra_id = x.get("_id", "")
            nome = x.get("Nome", "")
            comentario = x.get("Comentario", "")
            nota = x.get("Nota", "")

            result.append(
                {"_id": obra_id, "Nome": nome, "Comentario": comentario, "Nota": nota}
            )

        return result

    def countObrasUser(self, usuario):
        count = self.collectionObras.count_documents({"Usuario": usuario})
        return count

    def deleteObra(self, id):
        self.collectionObras.delete_one({"_id": id})

    def getObraId(self, id):
        obraData = self.collectionObras.find_one({"_id": id})
        return obraData

    def updateObra(self, id, nomeObra, comentario, genero, nota, status, tipo):
        result = self.collectionObras.update_one({"_id": id}, {"$set": {
            "Nome": nomeObra,
            "Comentario": comentario,
            "Genero": genero,
            "Nota": nota,
            "Status": status,
            "Tipo": tipo
        }})

        if result.modified_count == 1:
            return True
        return False
