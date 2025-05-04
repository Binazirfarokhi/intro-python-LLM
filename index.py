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

name = input('Enter your name: ')
distance_km = input('Enter distance in km: ')
distance_mi = float(distance_km)/1.609
print(f'Hi {name.title()}! {distance_km}km is equivalent to {round(distance_mi,1)} miles.')
# list like array 
friends = ['binazir','reza','ali']
print(friends[0])
print(len(friends))
print(friends.count('eric'))