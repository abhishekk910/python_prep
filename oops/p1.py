class Book:

    def __init__(self, title, author, pages=100):
        self.title = title
        self.author = author
        self.__pages = pages 

    def get_info(self):
        print(f"The book {self.title} by {self.author}. has {self.__pages} pages")
    
    def get_pages(self):
        print(f"Number of pages : {self.__pages}")

    def set_pages(self, pages):
        self.__pages += pages 

    

book_object1 = Book(author="Joe A", title="Python Book")
book_object1.get_info()

book_object1.get_pages()

book_object1.set_pages("100")
book_object1.get_pages()




