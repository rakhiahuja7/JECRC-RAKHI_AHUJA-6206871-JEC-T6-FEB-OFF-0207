
'''
  control statement : it is a type of statement which controls the flow of the execution of a program
'''
## Conditional statements: Based upon one condition, the flow of the exexution of a program will be decided
'''
1. if statement(simple if)
2. if else statement,
3. elif statement,
4. nested if statement
'''

## WAP to check whether the username & password is correct or not. if correct print login successful completed. If not, do nothing
## if 
user = {
    'username': 'user123',
    'password': '****'
}
un = input('Enter username: ')
pwd = input('Enter Password: ')

## if the condition is true then only if block will get executed 
if un == user['username'] and pwd == user['password'] :
    print('Login Successfully Completed')
else:
    print('Incorrect username or password')    

print('Program got ended!')

'''
syntax of if --->

 if <condition> :
    statement block (True statement Block - TSB)

______________________________________________

syntax of if else --->


if <condition> :
    statement block (tsb)
else:
    statement block (false statement block - FSB)       

''' 



## elif statement
## when we have multiple conditions and for those multiple conditions we have multiple sattements then we go for elif 
## for elif there should be atleast one if condition


## WAP in python to take a character from the user and check whether it is a vowel or consonant or digit or special character
'''
1. Take a charcter from the user.
2. Apply the condition one by one
'''

str(input('Enter a character:'))  
if chr in 'aeiouAEIOU':
    print('Vowel!')
elif chr in '0123456789':
    print('digit !')
elif (chr >= 'a' and chr<= 'z' ) or (chr >= 'A' and chr <= 'Z')  :
    print('Consonant!')
else:
    print('Special Character!')    
