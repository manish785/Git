print('Hello World')

#variable in python
age=20
price=15.6
first_name='manish'
is_online=True
print(age)

#taking input in python
#name=input("what is your name? ")
#print('Hello'+' '+name)

#Type conversion
#birth_year=input('Enter your birth year: ')
#age=2020-int(birth_year)
#print(age)

#add two number in python 
#first=int(input("First: "))
#second=int(input("second: "))
#sum=first+second
#print(sum)

#type conversion -str to int and vice versa

#first=int(input("First: "))
#second=float(input("second: "))
#sum=first+second
#print(sum)

#string 
course='Python for beginners'
print(course.find('Python'))

#in operator
print('Python' in course)

#and operator and or operator in python
price=5
print(price>10 and price<30)
print(price>10 or price<30)

#if else condtion
temperature=10
if temperature > 30:
    print("It's hot day")
elif temperature>20:
    print("It's mid hot day")
elif temperature>10:
    print("It's bit cold day")
else:
    print('very cold')

#loops 
i=1
while i<=5:
    print(i * '*')
    i=i+1


#list
names=['manish','ravi','rohit','nitish']
names[0]='sunny'
print(names[0])
print(names[0:3]) #this will print elements from 0th index to 2nd index elements
print(names)

#list methods
numbers=[1,2,3,4,5]
numbers.append(6)
print(numbers)

numbers.insert(0,-1)  #this method insert value at a particular place
print(numbers)

numbers.remove(3) #this remove the particular value

#numbers.clear() #this method removes the all elements

print(1 in numbers) # the 'in' operator use to find the particular value exist or not 
print(len(numbers)) # it gives the length of list

#for loop
numbers1=[1,2,3,4,5]
for item in numbers1:
    print(item)

#range
#numbers2=range(5,10,2)
for number in range(5):
    print(number)

#tuples- it is immutable data type
numbers3=(1,2,3)
print(numbers3.count(3))
print(numbers3.index(3))

































