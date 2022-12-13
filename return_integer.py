# get non-negative integer helper function:
def get_int():
    while True:
        count = input("Enter quantity: ")
        try:
            val = int(count)    
            if val >= 0:
                break
            else:
                print("Quantity can't be negative")
        except ValueError:
            print("Quantity must be a whole number")
    return val
