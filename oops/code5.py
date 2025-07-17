class Book:

    total_books_count = 0 

    def __init__(self, title, author):
        self.title = title 
        self.author = author 
        Book.total_books_count += 1 

    @classmethod
    def get_total_books_count(cls):
        return cls.total_books_count  
    
    @classmethod
    def create_classic_by_austen(cls, title):
        return cls(title, "Jane Austen")


    def display_info(self):
        print(self.title, self.author) 
print(Book.get_total_books_count())
book1 = Book("1984", "George Orwell")
print(Book.get_total_books_count())
book2 = Book.create_classic_by_austen("Pride and Prejudice")


print(Book.get_total_books_count()) 