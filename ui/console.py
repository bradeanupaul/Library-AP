from domain.exceptions.duplicateError import DuplicateError
from service.clientService import ClientService
from service.bookService import BookService
from service.assignmentService import AssignmentService


class Console:
    def __init__(self, clientService: ClientService, bookService: BookService, assignmentService: AssignmentService):
        self.__clientService = clientService
        self.__bookService = bookService
        self.__assignmentService = assignmentService

    def addClient(self):
        try:
            clientId = input("Scrie id-ul clientului: ")
            clientName = input("Scrie numele clientului: ")
            clientCnp = input("Scrie cnp-ul clientului: ")
            self.__clientService.addClient(clientId, clientName, clientCnp)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modifyClient(self):
        try:
            clientId = input("Scrie id-ul clientului: ")
            newClientName = input("Scrie noul nume al clientului: ")
            newClientCnp = input("Scrie noul cnp al clientului: ")
            self.__clientService.modifyClient(clientId, newClientName, newClientCnp)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def deleteClient(self):
        try:
            clientId = input("Scrie id-ul clientului: ")
            self.__clientService.deleteClient(clientId)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def searchClient(self):
        try:
            clientId = input("Scrie id-ul clientului: ")
            print(self.__clientService.searchClient(clientId))
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def showAllClients(self):
        clients = self.__clientService.getAllClients()
        for client in clients:
            print(client)

    def addBook(self):
        try:
            bookId = input("Scrie id-ul cartii: ")
            bookTitle = input("Scrie titlul cartii: ")
            bookDescription = input("Scrie descrierea cartii: ")
            bookAuthor = input("Scrie autorul cartii: ")
            self.__bookService.addBook(bookId, bookTitle, bookDescription, bookAuthor)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modifyBook(self):
        try:
            bookId = input("Scrie id-ul cartii: ")
            newBookTitle = input("Scrie noul titlu al cartii: ")
            newBookDescription = input("Scrie noua descriere a cartii: ")
            newBookAuthor = input("Scrie noul autor al cartii: ")
            self.__bookService.modifyBook(bookId, newBookTitle, newBookDescription, newBookAuthor)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def deleteBook(self):
        try:
            bookId = input("Scrie id-ul cartii: ")
            self.__bookService.deleteBook(bookId)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def searchBook(self):
        try:
            bookId = input("scrie id-ul cartii: ")
            print(self.__bookService.searchBook(bookId))
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def showAllBooks(self):
        books = self.__bookService.getAllBooks()
        for book in books:
            print(book)

    def addAssignment(self):
        try:
            assignmentId = input("Scrie id-ul inchirierii: ")
            clientId = input("Scrie id-ul clientului: ")
            bookId = input("Scrie id-ul cartii: ")
            self.__assignmentService.addAssignment(assignmentId, clientId, bookId)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modifyAssignment(self):
        try:
            assignmentId = input("Scrie id-ul inscrierii: ")
            newClientId = input("Scrie noul id al clientului: ")
            newBookId = input("Scrie id al cartii: ")
            self.__assignmentService.modifyAssingment(assignmentId, newClientId, newBookId)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def deleteAssignment(self):
        try:
            assignmentId = input("Scrie id-ul inscrierii: ")
            self.__assignmentService.deleteAssignment(assignmentId)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def searchAssignment(self):
        try:
            assignmentId = input("Scrie id-ul inscrierii: ")
            print(self.__assignmentService.searchAssignment(assignmentId))
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def showAllAssignments(self):
        assignments = self.__assignmentService.getAllAssignments()
        for assignment in assignments:
            print(assignment)

    def printMenu(self):
        print("1. Adauga client.")
        print("2. Modifica client.")
        print("3. Sterge client.")
        print("4. Cauta client.")
        print("c. Afiseaza toti clientii.")
        print("5. Adauga carte.")
        print("6. Modifica carte.")
        print("7. Sterge carte.")
        print("8. Cauta carte.")
        print("b. Afiseaza toate cartile.")
        print("9. Adauga inscriere.")
        print("10. Modifica inscriere.")
        print("11. Sterge inscriere.")
        print("12. Cauta inscriere.")
        print("i. Afiseaza toate inscrierile.")
        print("13. Afiseaza cele mai inchiriate carti.")
        print("14. Afiseaza clientii cu cartile inchiriate.")
        print("15. Afiseaza primi 20% dintre cei mai activi clienti.")
        print("d. DTOs.")
        print("x. Iesire.")

    def menu(self):
        while True:
            self.printMenu()
            option = input("Scrie optiunea: ")
            if option == "1":
                self.addClient()
            elif option == "2":
                self.modifyClient()
            elif option == "3":
                self.deleteClient()
            elif option == "4":
                self.searchClient()
            elif option == "c":
                self.showAllClients()
            elif option == "5":
                self.addBook()
            elif option == "6":
                self.modifyBook()
            elif option == "7":
                self.deleteBook()
            elif option == "8":
                self.searchBook()
            elif option == "b":
                self.showAllBooks()
            elif option == "9":
                self.addAssignment()
            elif option == "10":
                self.modifyAssignment()
            elif option == "11":
                self.deleteAssignment()
            elif option == "12":
                self.searchAssignment()
            elif option == "i":
                self.showAllAssignments()
            elif option == "13":
                print("In lucru.")
            elif option == "14":
                print("In lucru.")
            elif option == "15":
                print("In lucru.")
            elif option == "d":
                print("In lucru.")
            elif option == "x":
                break
            else:
                print("Optiune gresita.")
