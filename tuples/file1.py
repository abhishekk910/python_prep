tuple1 = (1,2,3)
tuple2 = (4,5,6)

tuple3 = ()

for  i in range(len(tuple1)):
    tuple3 += (tuple1[i] + tuple2[i],)

print(tuple3)  # Output: (5, 7, 9)  