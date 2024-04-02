from domain.assignments import Assignment
from domain.exceptions.duplicateError import DuplicateError
from repository.genericRepository import Repository


class AssignmentService:
    def __init__(self, assignmentRepository: Repository, clientRepository: Repository, bookRepository: Repository):
        self.__assignmentRepository = assignmentRepository
        self.__clientRepository = clientRepository
        self.__bookRepository = bookRepository

    def searchAssignment(self, assignmentId):
        return self.__assignmentRepository.getEntityById(assignmentId)

    def getAllAssignments(self):
        return self.__assignmentRepository.getAllEntities()

    def addAssignment(self, assignmentId, clientId, bookId):
        if self.__clientRepository.getEntityById(clientId) is None:
            raise KeyError("Nu exista un client cu acest id.")
        if self.__bookRepository.getEntityById(bookId) is None:
            raise KeyError("Nu exista o carte cu acest id.")

        assignments = self.__assignmentRepository.getAllEntities()
        for assignment in assignments:
            if assignment.getAssignmentClient() == clientId and assignment.getAssignmentBook() == bookId:
                raise KeyError("Clientul are deja aceasta carte.")

        assignment = Assignment(assignmentId, clientId, bookId)
        return self.__assignmentRepository.addEntity(assignment)

    def modifyAssingment(self, assignmentId, newClientId, newBookId):
        newAssignment = Assignment(assignmentId, newClientId, newBookId)
        self.__assignmentRepository.addEntity(newAssignment)

    def deleteAssignment(self, assignmentId):
        self.__assignmentRepository.deleteEntity(assignmentId)


