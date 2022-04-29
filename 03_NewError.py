# New made Error
class PositiveNumError(Exception):
    def __init__(self):
        super().__init__("Can't input PositiveNumber")

try: 
    num = int(input("Insert negative number>>>"))
    if num >= 0:
        raise PositiveNumError
except PositiveNumError as e:
    print("Error occur!" , e)
