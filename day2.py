
'''marketvalue = float(input("Enter the market real value: "))
discountvalue = float(input("Enter how much discount you want: "))

discount_percent = (discountvalue / marketvalue) * 100

print("Your discount % is:", discount_percent)

finalprice = marketvalue - discount_percent

print("Your discount % is:", finalprice)




usermarks = int(input("Enter your marks: "))

if usermarks > 90:
    print("Marks is A")
elif usermarks >= 80:
    print("Marks is A+")
    
elif usermarks >= 70:
    print("Marks is B+")
elif usermarks >= 60:
    print("Marks is B")
elif usermarks >= 50:
    print("Marks is B+")
else:
    print("tu fail hai")


#odd even
userage  = int(input("Enter your age: "))
if userage % 2 == 0:
    print("age is even")
else:
    print("age is odd")

#driving eligibility
print("Can i drive \n")
userage =  int(input("Enter your age: "))
if userage >= 18:
    print("You can drive")
else:
    print("Pehle bda hoja")


#pass or fail
print("Is am i pass or fail \n")
userage =  int(input("Enter your marks: "))
if userage >= 40:
    print("You are pass well done")
else:
    print("Sorry Bhai tu fail hai")

#for loop
for i in range(1, 11, 3):
    print(i)


#for table
userinput =  int(input("Enter your number you want to create table: "))
for i in range(1 , 1):
    print(i*userinput)

#while
i = 1;
while(i<=10):
    print(i*2)
    i= i+1;'''

i = 1;
total = 0;
while (i <= 10):
  total = total +i 
  i = i+1
print(total)
