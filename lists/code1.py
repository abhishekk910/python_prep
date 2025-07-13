# my_list = [0] * 26
# print(my_list, id(my_list))
# my_list = [1, 2, 3, 4, 5]
# print(my_list, id(my_list))


# nums = list(range(1,7))

# for num in nums:
#     if num%2==0:
#         print(num)


# [print(num) for num in nums if num%2 == 0]

# word_list = ['hello', 'world', 'zen', 'python']
# upper_words = [word.upper() for word in word_list]
# print(upper_words)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# res = []
# for sublist in matrix:
#     for num in sublist:
#         res.append(num)
# print(res)

# flat = [num for sub_list in matrix for num in sub_list]
# print(flat)

# lambda argument(s) : expression 

# add = lambda x,y : x+y 
# print(add(1,2))