lines = []

offset = 0

# appends another asterisk to lines each time it is called
def _print_pyramid(aster1):
    if aster1 > 0:
        lines.append('*')
        _print_pyramid(aster1 - 1)

# passes values to _print_pyramid
def print_pyramid(aster):
    global offset
    global lines
    lines.clear()
    if aster > 0:

        # converts array into string
        _print_pyramid(aster)
        line = ''.join(lines)

        #determines spaces to allocate and right aligns if necessary
        num = aster + offset
        if(offset == 0):
            print(line.ljust(num))
        else:
            print(line.rjust(num))
        offset += 1
        
        print_pyramid(aster - 2)

print_pyramid(int(input("Enter the width of your pyramid: ")))
