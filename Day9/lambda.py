'''
lambda(Anonymous Function):
    1. Lambda is a keyword. Which is used to create anonymous functions.
    2. For calling the lambda function, we can store the address of lambda inside a variable. By invoking the var_name, we can call the function.
'''
'''
var_name = lambda args: <exp>
var_name(args) ## Calling the lambda function
'''

## lambda args: <exp>
# result = lambda a,b: a+b ## Returns value
# print(result)
# print(result(1, 2))

# (lambda a,b: print(a+b))(int(input('First Num: ')), int(input('Sec Num: ')))


'''
lambda args: <exp_1> if <cond> else <exp_2>
'''

## WAP to find the square of a number if it is even.
# num = int(input('Enter a number: '))
# if num % 2 == 0:
#     print(num ** 2) ## num * num
    
# result = lambda num: print(num ** 2) if num%2 == 0 else None
# result(11)

# (lambda num: print(num ** 2) if num%2 == 0 else None)(int(input()))


## WAP to find the square of a number if it is even otherwise print cube of it.
# result = lambda num: print(num * num) if num%2==0 else print(num ** 3)
# result(int(input()))




## Check whether a num is positive or, negative or, zero.

# num = int(input())
# if num > 0:
#     print('POS')
# elif num < 0:
#     print('NEG')
# else:
#     print('ZERO')

# if num > 0:
#     print('POS')
# else:
#     if num < 0:
#         print('NEG')
#     else:
#         print('ZERO')

result = lambda num: print('POS') if num > 0 else print('NEG') if num < 0 else print('ZERO')
result(int(input()))
