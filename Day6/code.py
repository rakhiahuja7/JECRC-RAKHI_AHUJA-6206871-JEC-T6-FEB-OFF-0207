## inbuilt functions for string manipulation
# s="python"
# print("lower:", s.lower()) # it will convert the string to lower case

# print("upper:", s.upper()) # it will convert the string to upper case

# print("capitalize:", s.capitalize()) # it will convert the first character of the string to upper case and the rest to lower case

# print("title:", s.title()) # it will convert the first character of each word in the string to upper case and the rest to lower case

# print("strip:", s.strip("p")) # it will remove the specified character from the beginning and end of the string

# print("rstrip:", s.rstrip("n")) # it will remove the specified character from the end of the string

# print("lstrip:", s.lstrip("p")) # it will remove the specified character from the beginning of the string

# print("replace:", s.replace("p", "P")) # it will replace the specified character with another character

# print("index:", s.index("t")) # it will return the index of the specified character

# print("find:", s.find("r")) # it will return the index of the specified character if found, otherwise -1

# print("split:", s.split("t")) # it will split the string into a list of substrings based on the specified character

# list_s = s.split("t")
# print(list_s) 
# print("join:", "-".join(list_s)) # it will join the elements of a list into a string with the specified separator

# print("join:", " ".join(["python", "is", "awesome"])) # it will join the elements of a list into a string with the specified separator 

# print("startswith:", s.startswith("p")) # it will return True if the string starts with the specified character, otherwise False

# print("endswith:", s.endswith("n")) # it will return True if the string ends with the specified character, otherwise False 

# print("isdigit:", s.isdigit()) # it will return True if all characters in the string are digits, otherwise False

# print("isalpha:", s.isalpha()) # it will return True if all characters in the string are alphabetic, otherwise False

# print("isalnum:", s.isalnum()) # it will return True if all characters in the string are alphanumeric, otherwise False

# # s="1r2t3y4h5o6n@"

# # print("isdigit:", s.isdigit()) # it will return True if all characters in the string are digits, otherwise False

# # print("isalpha:", s.isalpha()) # it will return True if all characters in the string are alphabetic, otherwise False

# print("isalnum:", s.isalnum()) # it will return True if all characters in the string are alphanumeric, otherwise False

# print("isupper:", s.isupper()) # it will return True if all characters in the string are uppercase, otherwise False

# print("islower:", s.islower()) # it will return True if all characters in the string are lowercase, otherwise False

# inbuilt functions for list manipulation
# l=[1,2,3,4,5]

# l.append(6)# it will add the specified element to the end of the list
# print("append", l)
# l.insert(0, 0) # it will insert the specified element at the specified index in the list
# print("insert:", l) 
# l.remove(3) # it will remove the first occurrence of the specified element from the list
# print("remove:", l)
# l.pop()  # it will remove and return the last element of the list
# print("pop:", l)
# print("pop:", l.pop(0)) # it will remove and return the element at the specified index in the list
# print("list:", l)
# print("index:", l.index(4)) # it will return the index of the first occurrence
# l.extend([7,8,9]) # it will extend the list by appending all the elements from the specified iterable
# print("extend:", l)

## sort() and reverse()

## sort() -- sort in ascending order and return none i.e no new collection will be returned


# l = [12, 1, 3 ,45, 6]
# # print(l.sort())
# print(l)

# l.sort(reverse = True)
# print(l)
## if reverse is true then descending order , if false then ascending


# l = [1, 3, 4 ,2, 5,4]
# l.reverse()   ## reverse will always reverse the list not sort it 
# print(l)

# print(l.index(2))# will give indexof value
# # print(l.index(10)) ## error

# print(l.count(4))
# print(l.count(12)) # will not return error  instead gave count = 0

# clear will remove all the items in the list 

# l.clear()
# print(l)



## functions for tuple data types
'''
1.index
2. count
'''
# tpl = (1,2, 2, 3, 5)
# print(tpl.count(2))
# print(tpl.index(3))

# same as index and count in list



## Functions for set data type
'''
add
remove
discard
pop : randomly 
clear
union
intersection
difference 


'''

# s= {1, 2, True, False, 0, 3+9j}
# print(s)

# ## add() add element in set randomly + no effect is element is already present
# s.add(100)
# print(s)

# value = 2
# s.add(value) ## it adds the value but set will remove it if it's already present so that's why it throws no error
# print(s)

# # s.add([12, 13]) ## throws error as mutable collection is getting added
# # print(s)

# s.add((12, 13))
# print(s)

#  remove() -- remove an element from set, it must be present. if not it throws an error 
# s.remove(3+9j)
# print(s)

# s.remove(True)
# print(s)

# s.remove(10)  //throws keyerror
# print(s)

## discard() -- similar to remove but it does not raise an exception when an element is missing from the set
# s.discard(1)
# print(s)

# s.discard(10) ## no error 
# print(s)


## pop() - randomly pop out values from set
# print(s)
# s.pop()
# print(s)
# s.pop()
# print(s)


## clear() -- discard all the element and return an empty set


## union - concate the sets, return a new set
# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# # s3 = s1.union(s2)
# # print(s3)

# # s = s1.union(s2, s3)
# # print(s)

# # s4 = {5, 6, 7}
# # s5 = s1.union(s2, s, s3, s4)
# # print(s5)


# # s1.union({1, 2, 3}, {5, 6, 7}, {7, 8, 9})
# # print(s1)

# ## intersection - wil return the common elements
# # print(s1.intersection(s2))  ## {2,3}

# ## difference -- all the uncommon elements in set 1

# # print(s1.difference(s2)) ## {1}

# ## symmetric_difference - return a set with elements in either the set or other but not both  (remove intersect elements)

# # print(s1.symmetric_difference(s2))  ## {1, 4}

# # Functions for dictionary data type
# ## clear -- will remove all the elements

# ## update() -- will update values, pass a dictionary inside of it 

# # user['password'] = '123' 
# # print(user)

# # user.update({'password' : '12345678'})
# # print(user)

# # user.update({'password' : '*****', 'is_logged_in' : True})
# # print(user)

# ## keys -- will return all the keys
# print(user.keys())

# ## values -- will return all values

# print(user.values())

# ## items -- will return a list of key value pairs

# print(user.items()) 

# '''
# dict_keys(['username', 'password', 'location'])
# dict_values(['user123', '*****', 'IN'])
# dict_items([('username', 'user123'), ('password', '*****'), ('location', 'IN')])

# '''

## packing
'''
... def func_name(*args):
...     statement
...     block
... func_name(val1, val2, val3,.....,valn)
'''

## create a function whichcan take n no of int or float numbers and returns only their addition

# def add_nums(*args):
#     print(args, type(args))
#     sum = 0
#     for i in args:
#         sum += i 
#     print(f'Addition:{sum}')

# add_nums()

# add_nums(1,2, 3, 4, 5, 6, 7, 8)

'''
output:
() <class 'tuple'>
Addition:0
(1, 2, 3, 4, 5, 6, 7, 8) <class 'tuple'>
Addition:36
'''


# def add_nums(*args):
#     args = list(args)
#     print(args, type(args))
#     sum = 0
#     for i in args:
#         sum += i 
#     print(f'Addition:{sum}')

# add_nums()

# add_nums(1,2, 3, 4, 5, 6, 7, 8)

'''
output:
[] <class 'list'>
Addition:0
[1, 2, 3, 4, 5, 6, 7, 8] <class 'list'>
Addition:36
'''
# #create a function which will take n no of input and return the addition only of int and float separately
# def add_sum(*args):
#     # args=list(args)
#     sum=0
#     # sum_float=0.0
#     for i in args:
#         if type(i)==int or type(i)==float:
#             sum+=i
#         # elif type(i)==float:
#         #     sum_float+=i
#     print('Addition of int and float:',sum)
#     # print('Addition of float:',sum_float)
# add_sum(1, 2, 3, 4, 5, 6, 7, 8,"hello",'a', 1.5, 2.5, 3.5)

# output:
# Addition of int and float: 43.5

#create a function which will return a lisr of prime numbers.please make sure that user can pass n no of input and function will return prime numbers from that input
# def isprime(i):
#     if i < 2:
#         return False
#     for j in range(2, int(i**0.5)+1):
#         if i % j == 0:
#             return False
#     return True
# def prime_nums(*args):
#     prime=[]
#     for i in args:
#             if isprime(i):
#                 prime.append(i)
#     print('Prime numbers:',prime)

# prime_nums(*eval(input('Enter numbers: ')))
