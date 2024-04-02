from domain.entity import Entity


class Client(Entity):
    def __init__(self, entityId, entityName, entityCnp):
        super().__init__(entityId)
        self.__entityName = entityName
        self.__entityCnp = entityCnp

    def getClientName(self):
        return self.__entityName

    def getClientCnp(self):
        return self.__entityCnp

    def setClientName(self, Name):
        self.__entityName = Name

    def setClientCnp(self, Cnp):
        self.__entityCnp = Cnp

    def __str__(self):
        return f"Id-ul este: {self.getEntityId()}, Numele este: {self.getClientName()}, Cnp-ul este: {self.getClientCnp()}"