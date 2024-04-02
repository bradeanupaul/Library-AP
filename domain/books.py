from domain.entity import Entity


class Book(Entity):
    def __init__(self, entityId, entityTitle, entityDescription, entityAuthor):
        super().__init__(entityId)
        self.__entityTitle = entityTitle
        self.__entityDescription = entityDescription
        self.__entityAuthor = entityAuthor

    def getBookTitle(self):
        return self.__bookTitle

    def getBookDescription(self):
        return self.__entityDescription

    def getBookAuthor(self):
        return self.__entityAuthor

    def setBookTitle(self, entityTitle):
        self.__entityTitle = entityTitle

    def setBookDescription(self, entityDescription):
        self.__entityDescription = entityDescription

    def setBookAuthor(self, entityAuthor):
        self.__entityDescription = entityAuthor

    def __str__(self):
        return f"Id-ul este: {self.getEntityId()}, Titlul este {self.__entityTitle()}, Descrierea este: {self.__entityDescription()}, Autorul este: {self.__entityAuthor()}"