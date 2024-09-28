try:
  sum = 0
  number= int(input("Enter an integer: "))
 
  if number>0:
   for number in range(number,0,-1):
      print(number, end=" ")
      sum = sum+ number
   print() 
   print(f"The sum is {sum}")
  else:
      print("Nothing to be printed")   
except ValueError:
  print("Nothing to be printed")


