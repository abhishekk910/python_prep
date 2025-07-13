def named(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))

args = (1,2,3)
details = {"name": "Abhi", "age": 26}
#named(*args, name="Abhi", age=25)
named(args, details, **details)