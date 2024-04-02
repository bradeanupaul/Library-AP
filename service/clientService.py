from domain.clients import Client
from repository.genericRepository import Repository


class ClientService:
    def __init__(self, clientRepository: Repository, assignmentRepository: Repository):
        self.__clientRepository = clientRepository
        self.__assignmentRepository = assignmentRepository

    def searchClient(self, clientId):
        return self.__clientRepository.getEntityById(clientId)

    def getAllClients(self):
        return self.__clientRepository.getAllEntities()

    def addClient(self, clientId, clientName, clientCnp):
        client = Client(clientId, clientName, clientCnp)
        self.__clientRepository.addEntity(client)

    def modifyClient(self, clientId, newClientName, newClientCnp):
        newClient = Client(clientId, newClientName, newClientCnp)
        self.__clientRepository.modifyEntity(newClient)

    def deleteClient(self, clientId):
        assignments = self.__assignmentRepository.getAllEntities()
        for assignment in assignments:
            if assignment.getClientId() == clientId:
                self.__assignmentRepository.deleteEntity(assignment.getAssignmentId())
        self.__clientRepository.deleteEntity(clientId)

