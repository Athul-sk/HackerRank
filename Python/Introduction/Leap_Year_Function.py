def is_leap(year):        # Creating a function is_leap  to check whether the entered year is a leap year or not
    leap = False          # Setting the default value of the boolean variable leap to False
    
    # Write your logic here
    if year%400 == 0 and year%100 ==0:    # It is a leap year if the year is divisible by 400 and 100 at the same time
        leap=True
    elif year%4==0 and year %100 != 0:    # It is a leap year if the year is divisible by 4 but not with 100 at the same time
        leap=True
    
    return leap

year = int(input())
print(is_leap(year))      # Calling the function
