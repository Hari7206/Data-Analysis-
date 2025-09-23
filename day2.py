
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
    print("tu fail hai")'''


#odd even
userage  = int(input("Enter your age: "))
if userage % 2 == 0:
    print("age is even")
else:
    print("age is odd")
