apples= int(input("How many apples? "))
children = int(input("How many children? "))

share = apples//children
reminder = apples%children

print()
print(f"Each child will get {share} apples.")
print(f"There will be {reminder} leftover apples.")