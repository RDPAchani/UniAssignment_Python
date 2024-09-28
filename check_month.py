try:

 month=input("Enter a month number: ")
 month= int(month) 

 while(1 > month > 12): 

    print(f"{month} is not a valid month number")
    month=input("Enter a month number: ")
 print("OK")

except ValueError:
    print(f"'{month}' is not a valid month number")