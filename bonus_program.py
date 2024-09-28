sprice = int(input("Enter the car's selling price: "))

if sprice< 50000:
    bonus = sprice*0.01
else:
    bonus = sprice*0.015

if bonus < 200:
   bonus = 200

print(f"The bonus is {bonus:.2f}£")
