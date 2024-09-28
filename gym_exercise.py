days=int(input("Enter the number of days of gym visits per year: "))
price_daypass= float(input("Enter price for a day pass: "))
membership_fee= float(input("Enter yearly membership fee: "))

day_price = days*price_daypass
print()
if (membership_fee>day_price):
    print(f"Buying day passes is {(membership_fee-day_price):.2f} euros cheaper")

elif (day_price>membership_fee):
    print(f"Paying the yearly membership fee is {(day_price-membership_fee):.2f} euros cheaper")

else:
   print(f"There is no price difference")



