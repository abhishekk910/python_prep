def multiply(args):
    print(args, type(args))
    total = 1
    for arg in args:
        print(arg)
        total *= arg 

    return total 


def add(args):
    print("addition")
    total = 0
    for i in args:
        total += i 
    return total

def apply(operator, *args):
    if operator == "*":
        return multiply(args)
    elif operator == "+":
        return add(args)
    else:
        return "No valid operator to apply"
    

print(apply("*", 1,2,3,4)) 
print(apply("+", 1,2,3,4,4))
print(apply("/", 1,2,3,4,4))