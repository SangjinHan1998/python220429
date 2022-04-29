# insert Won,  exchange rate --> Dollar

won = input("Insert Won>>>")
dollar = input("Insert exchange rate>>>")

try:    
    # Code for which exceptions may occur
    print(int(won) / int(dollar))
except ValueError as err1: 
    # Code executed when an exception occurs
    # Direct corresponding error controllable code
    # Each Error can have nickname
    print("Exception occur", err1)   # err1 -> print exception message
except ZeroDivisionError as err2:
    print("Division zero is not able to execute", err2)
else:
    print("Execute Code when Exception don't occur")

finally:    # close file (resource return)
    print("Always execute Code Whether the exception occurs or not ")

