import math
# print("hello world!")
# # This is a comment.
# '''comment'''
# 'comment'

# int_example = 5
# float_example = 5.55
# string_example = "hello"

# x=5
# x="this is a string"

# result = 5.5//4
# print(result)

# result = 5.5%4
# print(result)

# squared = 5**2
# print(squared)

# squared = math.pow(6,2)
# print(squared)

# if squared == 25:
#     print("Correct")
# else:
#     print("Something went wrong")

# x=10
# y=100
# if x >= 10 or y<90:
#     print("one statement is true")

# grade = 90
# if grade >=90:
#     letter = "A"
# elif grade >= 90:
#     letter = "B"
# elif grade >=80:
#     letter = "C"
# else:
#     letter = "D"

# first_name='Luke'
# last_name='Franco'
# full_name = first_name + ' ' +last_name
# repeat = first_name*5
# print(full_name) 
# print(repeat)

# first_two = first_name[0:2]
# print(first_two)

# if 'L' in first_name:
#     print("L in first name")
# alist =  [7, 9, 4, 2, 7, 7, 5, 3, 5, 1, 7, 8, 6, 7]
# min = 5 
# max = 7
# new_list= [var for var in alist if var<min or var>max]
# print(new_list)
# words = ["Hello", "hi", "brown", "what", "hi", "brown"]

# strings = ["a", "b", "c", "a", "c"]
# dictionary = {}
# # dictionary[strings[0]] = 0
# dictionary[strings[0]] = [var + 1 for var in range(0,len(strings))]

# print(dictionary)
# strang = "Hello my name is joe baseball"

# new_list = [var for var in strang if var==' ']
# print(len(new_list))

lst = [5,4,3,2,1]

new_list = lst
i = 0
min = lst[0]
pos = 0
for x in lst:
    if x <= min:
        min = x
        pos = i
    i=i+1
new_list[pos] = new_list[0]
new_list[0] = min
print(new_list)