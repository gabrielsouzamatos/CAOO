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

    def puxarObra(self, position):
        return self.model.get_all_obras(position)
