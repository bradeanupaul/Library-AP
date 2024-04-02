from domain.books import Book
from repository.genericRepository import Repository


class BookService:
    def __init__(self, bookRepository: Repository, assignmentRepository: Repository):
        self.__bookRepository = bookRepository
        self.__assignmentRepository = assignmentRepository

    def searchBook(self, bookId):
        return self.__bookRepository.getEntityById(bookId)

    def getAllBooks(self):
        return self.__bookRepository.getAllEntities()

    def addBook(self, bookId, bookTitle, bookDescription, bookAuthor):
        book = Book(bookId, bookTitle, bookDescription, bookAuthor)
        self.__bookRepository.addEntity(book)

    def modifyBook(self, bookId, newBookTitle, newBookDescription, newBookAuthor):
        book = Book(bookId, newBookTitle, newBookDescription, newBookAuthor)
        self.__bookRepository.modifyEntity(book)

    def deleteBook(self, bookId):
        assignments = self.__assignmentRepository.getAllEntities()
        for assignment in assignments:
            if assignment.getBookId() == bookId:
                self.__assignmentRepository.deleteEntity(assignment.getAssignmentId())
        self.__bookRepository.deleteEntity(bookId)
