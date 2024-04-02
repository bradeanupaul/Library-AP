from domain.entity import Entity


class Assignment(Entity):
    def __init__(self, assignmentId, assignmentClient, assignmentBook):
        super().__init__(assignmentId)
        self.__assignmentClient = assignmentClient
        self.__assignmentBook = assignmentBook

    def getAssignmentClient(self):
        return self.__assignmentClient

    def getAssignmentBook(self):
        return self.__assignmentBook

    def setAssignmentClient(self, Client):
        self.__assignmentClient = Client

    def setAssignmentBook(self, Book):
        self.__assignmentBook = Book

    def __str__(self):
        return f"Id-ul este: {self.getEntityId()}, Clientul este: {self.getAssignmentClient()}, Cartea este: {self.getAssignmentBook()}"