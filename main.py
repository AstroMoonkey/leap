# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
while year <= 2080:
  if year % 400 == 0:   #**unless** the year is also evenly divisible by 400`
    print(f"{year} is a leap year because it is evenly divisible by 400")
  elif year % 100 == 0:    # **except** every year that is evenly divisible by 100
    print(f"{year} is not a leap year because is evenly divisible by 100")
  elif year % 4 == 0:  # on every year that is evenly divisible by 4
    print(f"{year} is a leap year")
  else:
    print(f"{year} is not this is not a leap year")
    
  year = year + 1

