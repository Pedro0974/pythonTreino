

class Tarefa:

    def __init__(self, titulo, descricao, data_criacao, data_conclusao, status):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data_criacao = data_criacao
        self.__data_conclusao = data_conclusao
        self.__status = status

    @property
    def titulo(self):
        return self.__titulo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def data_criacao(self):
        return self.__data_criacao

    @property
    def data_conclusao(self):
        return self.__data_conclusao

    @property
    def status(self):
        return self.__status
