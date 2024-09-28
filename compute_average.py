try:

 value= float(input("Enter first number: "))
 number= 0
 sum=0
 while(value!=0):
    sum=sum+value
    value=float(input("Enter next number: "))
    number= number+1

 average= sum/number
 print(f"The average is {average:.2f}")

except ZeroDivisionError:
  print("Nothing to be calculated")
