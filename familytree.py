import fileinput

familyTree
for line in fileinput.input():
    # split the command into a list of strings
    x = line;
    command = x.split()

    # if the command has three parts, marriage without kid, print all of statements
    if len(command) == 3:
        pass
        # is x a blank of y?
        if command[0] == 'X' | command[0] == 'x':
            pass
        # print all of relation
        if command[0] == 'W' | command[0] == 'w':
            pass
        # marriage statement
        if command[0] == 'E' | command[0] == 'e':
            pass

    # if the command has four parts, marriage with kids, print true or false for relation
    if len(command) == 4:
        pass
        # is x a blank of y?
        if command[0] == 'X' | command[0] == 'x':
            pass
        # print all of relation
        if command[0] == 'W' | command[0] == 'w':
            pass
        # marriage statement
        if command[0] == 'E' | command[0] == 'e':
            pass
    pass

