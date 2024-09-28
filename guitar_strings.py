gigs = int(input("Number of gigs: "))
string_set = int(input("Gigs to be played with the same set of strings: "))
string_price = float(input("Price of a set of guitar strings: "))

number = (gigs+string_set-1)//string_set
cost = string_price*number
print(f"The guitarist needs {number} new sets of guitar strings")
print(f"The total cost is {cost:.2f} euros")