#Question 1

a=int(input("Enter input:"))
b=int(input("Enter input:"))
c=int(input("Enter input:"))
x = y =0
if(a==0):
    print("Error")
else:
    discriminant = b ** 2 - 4 * a * c
    if(discriminant<0):
        print("Error")
    else:
          x=((-b+(discriminant ** 0.5)) / 2 * a)
          y=((-b-(discriminant ** 0.5)) / 2 * a)
print(x)
print(y)




#Question 2
sentence=input("Enter a string").lower()
x=sentence.split(" ")
y=[]
for i in x:
    if y.count(i)==0:
        y.append(i)
        print(i.title(),"-", sentence.count(i))



#Question 3
import re
a=input("Enter a string:")
count1 = count2 = 0
for count in a:
    if count.isdigit():
        count1+=1
    if count.isalpha():
        count2+=1
print("Digits -", count1)
print("Letters -",count2)

#Question 4
import re
a=(input("Enter a string:"))
if int(len(a)<6 or len(a)<=12):
    if (re.search("[A-Z]",a) and re.search("[a-z]",a) and re.search("[0-9]",a) and re.search("[@#$]",a)):
        print("It is a valid password")
    else:
        print("It is an invalid password")
else:
    print("The password you entered is wrong")


#Question 5
sentence = input("Enter a string: ")
target_word = input("Enter the searchable word:")
words = sentence.split()#to split the sentence
positions = []#declare position
index = 0
for word in words:
    if word == target_word:
        positions.append(index)#to add the position
    index += 1
if positions:
    print(positions)
else:
    print(False)


