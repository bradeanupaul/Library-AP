from repository.genericRepository import Repository
from service.assignmentService import AssignmentService
from service.clientService import ClientService
from service.bookService import BookService
from ui.console import Console

def main():
    clientRepository = Repository()
    bookRepository = Repository()
    assignmentRepository = Repository()

    clientService = ClientService(clientRepository, assignmentRepository)
    bookService = BookService(bookRepository, assignmentRepository)
    assignmentService = AssignmentService(assignmentRepository, clientRepository, bookRepository)

    console = Console(clientService, bookService, assignmentService)

    console.menu()

main()