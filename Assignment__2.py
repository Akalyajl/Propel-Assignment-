#1.Print the list of numbers which are divisible by 5 and multiple of 8 between 2000 and 2500

list=[]
for i in range(2000,2500):
    if i%5==0 and i%8==0:
        x=list.append(i)
print(list)

#2.Write a Python program to create the table (from 1 to 10) of a number getting input from the user

n=int(input("Enter a num:"))
z=int(input("Enter a num:"))
for i in range(1,n+1):
    table=z*i
    print(z,"*",i,"=",table)

#3.sort the list in ascending order and print first element

list =[6,7,10,1,3,2,5,4,9,8]
list.sort()
print(list)
print(list[0])


#4.Python program to find second largest number in a list

n=int(input("Enter num:"))
l=[]
for i in range(n):
    l.sort()
    l.append(i)
print(l[-2])



#5.Python program to print odd numbers & even numbers separately in al list of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a=[]
b=[]
for i in list:
    if i%2==0:
        x=a.append(i)
    elif i%2==1:
        y=b.append(i)
print(a)
print(b)

#6.Program for Reversing a list

list=[]
n=int(input("Enter a num:"))
for i in range(1,n+1):
    list.append(i)
print(list[::-1])



#7.Program to print all odd numbers from 1-50

list=[]
a=int(input("Enter a num:"))
b=int(input("Enter a num:"))
for i in range(a,b+1):
    if i%2==1:
        x=list.append(i)
print(list)

#8.Program to count Even and odd numbers in a list

m=int(input("Enter a list:"))
n=int(input("Enter a list:"))
a=[]
b=[]
for i in range(m,n+1):
    if i%2==0:
        x=a.append(i)
        even_count=len(a)
    elif i%2==1:
        y=b.append(i)
        odd_count=len(b)
print(even_count)
print(odd_count)



#9.Write a python program to remove zeros from an IP address("216.08.094.196")

import re
a="216.08.094.196"
z=re.sub('\.[0]*','.',a)
print(z)


#10.Write a Python program that matches a string that has an 'a' followed by anything, ending 's'

import re
string=input("Enter string:")
x=re.findall("a+\S+s",string)
print(x)

#11.Replace all occurences of 6 with 'six' and 10 with 'ten' for the given string 'They ate 6 apples and 10 banana'

a="They ate 6 apples and 10 banana"
b=a.replace("6","six")
c=b.replace("10","ten")
print(c)

#12.Write a program to check whether a person is eligible for voting or not. (accept age from user)

age=int(input("Enter the age:"))
if(age>=18):
    print("The person is eligible for voting")
else:
    print("The person is not eligible for voting")

"""13.Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
    Unit                                                       Price  
First 100 units                                               no charge
Next 100 units                                              Rs 5 per unit
After 200 units                                             Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)"""


a=int(input("Enter num of unit:"))
if a<=100 and a>=0:
    print("Current bill is zero rupees")
elif a>100 and a<=200:
    b=100*5
    print("Current bill is",b,"rupees")
elif a>200:
    c=200*10
    print("Current bill is",c,"rupees")
else:
    print("invalid")

"""14 Write a program to accept percentage from the user and display the grade according to the following criteria:

         Marks                                    Grade
	     > 90                                       A
         > 80 and <= 90                             B
         >= 60 and <= 80                            C
         below 60
"""


a=int(input("Enter marks:"))
if a>90:
    print("Grade A")
elif a>80 and a<=90:
    print("Grade B")
elif a>=60 and a<=80:
    print("Grade C")
elif a<60:
    print("Grade D")
else:
    print("Invalid!!Enter correct marks!")






