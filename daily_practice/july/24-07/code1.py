# def check_even_odd(number):
#     return "Even Number" if number%2==0 else "Odd Number" 

# print(check_even_odd(int(input("Provide Integer Number : ")))) 


check_even_odd = lambda number: "Even Number" if number%2==0 else "Odd Number" 
print(check_even_odd(int(input("Provide Integer Number : "))))