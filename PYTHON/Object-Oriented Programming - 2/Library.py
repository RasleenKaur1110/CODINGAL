class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = dict()

    def displayBooks(self):
        print(f"We have the following books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender Book database has been updated. You can take the book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")
    
    def addBook(self, book):
        self.booklist.add(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':

    books = Library({'One of us is lying', 'A good girls guide to murder', 'Nancy Drew diaries', 'The agathas', 'As good as dead'}, "Peace")

    while(True):
        print(f"Welcome to the {books.name} library. Enter your choice to continue.")
        print("1. Display Books")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")

        user_choice = input()
        if user_choice not in {'1', '2', '3', '4'}:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            books.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of your book that you want to lend: ")
            user = input("Enter your name")
            books.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book that you want to add: ")
            books.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book that you want to return: ")
            books.returnBook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice = input()
        if user_choice == "q":
            exit()
        else:
            continue