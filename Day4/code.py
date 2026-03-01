'''
Problem 1:
Calculate electricity bill based on units
 0-100 -> 5/unit
 101-300 -> 7/unit
 above 300 -> 10/unit
 if bill > 5000 -> 5% discount
 '''
units = int(input('Enter units:'))
bill = None
if units > 0:
    if units <= 100 :
       bill = units*5
    elif  101 <= units <=300 :
       bill = units * 7
      
    else :
       bill = units * 10

    if bill > 5000:
        bill = bill * 0.95
    print(f'Bill Amount after Discount:{bill}')       
else:
    print('Enter valid units!')   


'''
Loan Approval System

"Problem:
Loan approved if :
salary > 25, 000
CIBIL score > 700
if salary > 50, 000 & CIBIL > 750 -> instant approval

otherwise -> rejected
'''

salary = int(input('Enter Salary:'))
CIBIL_score = int(input('Enter CIBIL score: '))

if salary > 25000 and CIBIL_score > 700:
    if(salary > 50000 and CIBIL_score > 750):
        print('Instant Approval')
    else:
        print('Loan Approved')  

else:
    print('Rejected') 



'''
WAP to check whether a year is leap year or not
'''
year = int(input('Enter the year:'))

if year% 4 == 0:
    if year%100 != 0 or year%400 == 0:
        print('Leap Year')
else:
    print('Not a leap year') 



'''
WAP to take a charcter from the user and convert it into lowercase if it is an uppercase or vice-versa.

'''
character = ord(input('Enetr an alphabet:'))


if  65 <= (character) <= 90 :
    print('It is uppercase letter')
    print(chr(character + 32))
elif 97 <= (character) <= 122:
    print('It is lowercase letter')
    print(chr(character - 32))
else:
    print(chr(character))

# second method more human readable

charcter = input('Enter a charcter:')

# way 2

if 'A' <= charcter <= 'Z':
    print(chr(ord(charcter)+ 32))
elif 'a' <= charcter <= 'z':
     print(chr(ord(charcter) - 32))  
else:
    print(charcter)       


## Achieve the desired output for the below given input:
## INPUT:RAhul@123Gh
## OUTPUT: raHUL@123gH

## you can't use inbulit functions 

string = input('Enter the input:')
result = ''

for i in string:
    if 'A' <= i <= 'Z':
       result += (chr(ord(i)+ 32))
    elif 'a' <= i <= 'z':
        result += (chr(ord(i) - 32))  
    else:
        result += i    
print(result)  

'''
## input: [10, 2.2, 5, 'Hello', [100, 200], 99.9] //find out the maximum number 
## 99.9
'''

list1 = eval(input('Enter a list:'))
first = list1[0]

for i in list1:
    if type(i) in [int, float]:
        if i > first:
            first = i
print(first)   


'''
input : {'a':1, 'b':2, 'c':3, 'd':4}
output: {1:'a', 2:'b', 3:'c', 4:'d'}

'''

coll = {'a':1, 'b':2, 'c':3, 'd':4}
new_coll = {}

for i in coll:       ## here i will store the key of the collection 
    new_coll[coll[i]] = i   ## here coll[i] will store the value of coll and we made that the key for new_coll and i which was originally the key for coll as value of new_coll
print(new_coll)    




'''
input : ('Hello', 'Hi', 20, 40.2, 9.6j, [1, 2], 'PYTHON', 'JECRC', (1, 2, 3))
output: {'Hello':'l', 'Hi':'Hi', 'PYTHON':'PN', 'JECRC': 'C', (1, 2, 3) : 2}

'''
coll = eval(input('Enter a collection:'))
new_coll = {}

for i in coll:
    if type(i) in [str, tuple]:
        if len(i)%2 == 0:
            new_coll[i] = i[0] + i[-1]
        else:
            new_coll[i] = i[len(i) // 2]
print(new_coll)  




#break statement

## homogeneous or heterogeneous collection
coll = [1, 3, 3.6 ,4, 5, 'Hello']
i, flag = coll[0], True  ## flag = True means we are assuming it is homogenous collection at start

for j in coll:
    if type(i) != type(j):
        flag = False
        break
if flag:
    print('Homogeneous collection!')
else:
    print('Heterogeneous Collection!')           

## PASS 
if True:
    ## I don't have a statement block  but if we keep it empty it will give an error so we use pass 
    pass

 

for i in range(10):
    pass

print('Good Morning!') 
