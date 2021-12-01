# Creating a Library class (oop mini-project)
class Library:
    # whoever initiates the library class will have these at their disposal
    def __init__(self, lst, name):
        self.booklist = lst
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f'Library {self.name} has the following books: ')
        for book in self.booklist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print('The book-database updated. Can take the book')
        else:
            print(f'The book has already been lent to {self.lendDict[book]}')

    def addBook(self, book):
        self.booklist.append(book)
        print('The book has been added to the book-database')
    
    def returnBook(self, book):
        self.lendDict.pop(book)
        print(f'The book has been removed from the lentDict')

# Initializing library object in the same file, so we have use name==main

if __name__ == '__main__':
    nik = Library(['hp', 'stormlight', 'python', 'algo', 'java'], "MyLibrary")

    while True:
        print('Wel. to {nik.name}, Enter choice to continue')
        print('1. displaybooks')
        print('2. lendbooks')
        print('3. addbooks')
        print('4. returnbooks')

        user_inp = int(input(">> "))

        if user_inp == 1:
            nik.displayBooks()
        elif user_inp == 2:
            name = input('Enter your name: ')
            book_name = input('Enter the book you want to lend: ')
            nik.lendBook(name, book_name)
        elif user_inp == 3:
            book_name = input('Entet the book you want to add to library: ')
            nik.addBook(book_name)
        elif user_inp == 4:
            book_name = input('Enter the book you want to return: ')
            nik.returnBook(book_name)
        else:
            print('not a valid option')
        
        print('press q to quit and c to continue')
        # user_inp2 = ''
        # while user_inp2 == 'q' or user_inp2 == 'c':
        #     user_inp2 = input()
        #     if user_inp2 == 'q':
        #         exit()
        #     elif user_inp2 == 'c':
        #         continue
        user_inp2 = input("+> ")
        if user_inp2 == 'q':
            exit()
        else:
            continue











