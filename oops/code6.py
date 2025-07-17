"""class Bookshelf: 

    def __init__(self, *books):
        self.books = books 

    def __str__(self):
        return (f"Bookshelf with {len(self.books)} books ") 
    
class Book: 

    def __init__(self, name): 
        self.name = name 

    def __str__(self):
        return f"Book: {self.name}"
    

book1 = Book("1984")
book2 = Book("Pride and Prejudice")

bookshelf = Bookshelf(book1, book2)
    

print(bookshelf)  # Output: Bookshelf with 2 books

print(book1)
 # Output: Book: Pride and Prejudice



print(bookshelf.books[1])  # Output: Book: 1984 
""" 
















class Keyboard:
    def __init__(self, key_layout):
        self.layout = key_layout
        print(f"Keyboard with {self.layout} layout created.")

    def type_key(self, key_char):
        return f"Typing '{key_char}' on the {self.layout} keyboard."

class Monitor:
    def __init__(self, size):
        self.size = size
        print(f"Monitor of {self.size} inches created.")

    def display(self, content):
        return f"Displaying '{content}' on the {self.size}-inch monitor."



class Computer:
    def __init__(self, brand, cpu_model, keyboard_layout, monitor_size):
        self.brand = brand
        self.cpu = cpu_model
        print(f"\nBuilding a {self.brand} computer...")

        # --- COMPOSITION happens here ---
        # The Computer "has-a" Keyboard and "has-a" Monitor
        self.keyboard = Keyboard(keyboard_layout) # Creating a Keyboard object and assigning it
        self.monitor = Monitor(monitor_size)     # Creating a Monitor object and assigning it
        # ---------------------------------

    def boot_up(self):
        print(f"{self.brand} computer is booting up...")
        # The Computer uses its parts to perform actions
        display_message = self.monitor.display("Welcome!")
        print(display_message)
        return f"{self.brand} computer ready."

    def user_input(self, text):
        # The Computer delegates tasks to its parts
        for char in text:
            print(self.keyboard.type_key(char))

# --- Using the Computer ---

# Create a computer object
my_desktop = Computer("Dell", "i7", "QWERTY", 24)

# Use the computer's functionalities
print(my_desktop.boot_up())
my_desktop.user_input("Hello World")

# You can also access the components directly if needed
print(f"My keyboard layout is: {my_desktop.keyboard.layout}")
print(f"My monitor size is: {my_desktop.monitor.size} inches")

"""
output :-

Building a Dell computer...
Keyboard with QWERTY layout created.
Monitor of 24 inches created.
Dell computer is booting up...
Displaying 'Welcome!' on the 24-inch monitor.
Dell computer ready.
Typing 'H' on the QWERTY keyboard.
Typing 'e' on the QWERTY keyboard.
Typing 'l' on the QWERTY keyboard.
Typing 'l' on the QWERTY keyboard.
Typing 'o' on the QWERTY keyboard.
Typing ' ' on the QWERTY keyboard.
Typing 'W' on the QWERTY keyboard.
Typing 'o' on the QWERTY keyboard.
Typing 'r' on the QWERTY keyboard.
Typing 'l' on the QWERTY keyboard.
Typing 'd' on the QWERTY keyboard.
My keyboard layout is: QWERTY
My monitor size is: 24 inches
"""