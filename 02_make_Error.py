# Let's force an error by using the "raise" syntax


# initial Error
try: 
    num = int(input("Insert negative number>>>"))
    if num >= 0:
        raise ValueError("Can't insert positive number ")
except ValueError as e:
    print("Error occur!" , e)
