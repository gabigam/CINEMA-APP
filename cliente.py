class Cliente:
    def __init__(self):
        self.__clientes = [] # []

    def adicionarCliente(self, dados):
        self.__clientes.append(dados)

    def removerCliente(self, dados):
        self.__clientes.remove(dados)

    def getClientes(self):
        return self.__clientes

    def getClienteID(self, id):
        return self.__clientes[id]


cliente_geral = Cliente()