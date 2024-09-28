try:

 number=int(input("Enter a weekday number: "))
   
 if not 1 <= number <= 7:
    raise ValueError
 print("OK")

except:
    print("Please enter an integer between 1 and 7")
