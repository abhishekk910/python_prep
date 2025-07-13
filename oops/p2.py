class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        # Using a double underscore makes a variable "private" in Python
        # It's a convention, not a strict rule, but it signals to
        # other developers not to access it directly.
        self.__balance = balance

    # Getter method to access the balance
    def get_balance(self):
        return self.__balance

    # Method to deposit money (controlled access)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit of ${amount} successful. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient amount to withdraw")
        else: 
            self.__balance -= amount 
            print(f"Withdrawal amount ${amount} successful. New balance: ${self.__balance}")
        

my_account = Account(owner="Alice")
print(f"Initial balance: ${my_account.get_balance()}")

my_account.deposit(500)
my_account.withdraw(100)  