print("please run me on the browser by having me as a Python")
failed_subjects = "6"
print("number or use hammer  " + failed_subjects)
# data-types : string - intigers- float 2.5 - boolean - 
# you can not put numbers inside the 
print(type(1.45))
stringToNumber = 2
print("this str can conver a number to a string  : " + str(stringToNumber))
# we have int() : make it to the number 
# we have float () make it to the decimal 2.4 
# we have str() make it to the string 
# we vall these them cast : cast them to str or int or float 
# datatyoes and typecasting 
# basic arithmetic : reyazi 
a=3
b=2
print('addition', a+b)
print('division (float)' , a/b)
print('division (floor)' , a//b)
# exponent mishe tavan 
print('exponent: '            , a**b) 
msg = " we have a cool stuff here "
print(msg+msg)
print(msg,msg)
print(msg.upper())
print(msg.capitalize())
print(msg.title())
print(len(msg))
print(msg.count('w'))
# slicing : getting a part of string and give it to us
print(msg[5:12])
# print the mesage backward 
print(msg[::-1])
print(msg.replace('cool',"binazir"))
# string are mutable means you needanother place to store them and then use them


# name = input("what is your name ? ")
# print("HEllo " + name)
# convert miles to kilometers

# for using ` back tich in python you need to use f'' and that's it 

# name = input('Enter your name: ')
# distance_km = input('Enter distance in km: ')
# distance_mi = float(distance_km)/1.609
# print(f'Hi {name.title()}! {distance_km}km is equivalent to {round(distance_mi,1)} miles.')
# list like array 
friends = ['binazir','reza','ali']
print(friends[0])
print(len(friends))
print(friends.count('eric'))
# sorting arrays in Python : 
cars = [123,345,4546,667,5,64,2,78]
print(cars)
friends.extend(cars)
print(friends)
# del friends
# how to copy an array 
# new_array = friends.copy()
# print(new_array)
# or
# new_arraytwo = friends[:]
# print(new_arraytwo)
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
# new_day = input('Enter #of lemonades for new day: ')
# sales_w2.append(int(new_day))
sales.extend(sales_w1)
sales.extend(sales_w2)
# sales = sales_w1 + sales_w2
#sales.sort()
worst_day_prof = min(sales) * 1.5
best_day_prof = max(sales) * 1.5
print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')

# working with split and join 
msg = 'welcome to the world of Python which is easy to learn '
# split will create a list ( array) we are converting a string into a list
print(msg.split())
# shows empty spaces in the list
print(msg.split(' '))
# we can use join to seprate the str in the array or list which turn into line
csv='Eric, John,Micheal,Terry,Graham'
print('-'.join(csv))
# join and split are vice versa of each other 
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'

print(','.join(csv.split(';')).split(':'))
friends_list = ['Exercise: fill me with names']
print(friends_list)

# tuples
array=['jj','fgfgf','wwwe']
array_tuple=('tyty','hyhy','erwr')
# unorder and there is not duplicate { } it is faster that ( ) and []
# 
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']
