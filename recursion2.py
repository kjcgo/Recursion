spaces = 0

# prints each line of asterisks using recursion
def _print_pyramid(x):
    if x > 0:
        print("*", end = '')
        _print_pyramid(x - 1)

# repeatedtly calls _print_pyramid
def print_pyramid(x):
    
    global spaces
    if x > 0:
        
        # adds spaces for formatting
        for y in range(spaces):
            print(" ", end = '')

        #modify spaces and x 
        spaces += 1
        _print_pyramid(x)
        print()
        print_pyramid(x-2)


# ====== Not submitted ======
num = int(input("Enter a number: "))

print_pyramid(num)

