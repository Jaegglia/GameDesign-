#august
#im gonna start with a for loop
last=9
for line in range (1,last):
    for number in range(line):
        print("*",end='')
    for space in range((last-1)-line):
        print(" ", end= '')
    for number in range (line,(last+1)):
        print("*",end='')
    for space in range (line-1):
        print(" ", end='')
    for space in range (line-1):
        print(" ", end='')
    for number in range(last-line):
        print("*",end='')
    for space in range(line,(last-1)):
        print(" ",end='')
    for number in range(line):
        print("*",end='')
    print()
