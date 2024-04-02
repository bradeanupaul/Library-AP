class Entity:
    def __init__(self, entityId):
        self.__entityId = entityId

    def getEntityId(self):
        return self.__entityId

    def setEntity(self, entityId):
        self.__entityId = entityId