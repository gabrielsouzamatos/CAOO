from Model import Model


class Controller:

    def __init__(self):
        self.model = Model()

    def receberRegistro(self, nome, senha):
        return self.model.computarRegistro(nome, senha)

    def receberLogin(self, nome, senha):
        return self.model.computarLogin(nome, senha)

    def receberObra(self, nome, nomeObra, comentario, genero, nota, status, tipo):
        return self.model.addObra(nome, nomeObra, comentario, genero, nota, status, tipo)

    def puxarObra(self, usuario):
        return self.model.getObraUser(usuario)

    def contarObra(self, usuario):
        return self.model.countObrasUser(usuario)

    def deletarObra(self, id):
        return self.model.deleteObra(id)

    def PuxarObraId(self, id):
        return self.model.getObraId(id)

    def atualizarObraId(self, id, nomeObra, comentario, genero, nota, status, tipo):
        return self.model.updateObra(id, nomeObra, comentario, genero, nota, status, tipo)
