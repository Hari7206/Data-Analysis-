
marketvalue = float(input("Enter the market real value: "))
discountvalue = float(input("Enter how much discount you want: "))

discount_percent = (discountvalue / marketvalue) * 100

print("Your discount % is:", discount_percent)

finalprice = marketvalue - discount_percent

print("Your discount % is:", finalprice)

