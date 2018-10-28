import fileinput

familyTree = {
    "Test": "test"
}
spouses = {
    "Test": "test"

}
testCases = [
    "W A B AB",
    "W B C BC",
    "W C D DC",
    "W D E DE",
    "W E F EF",
    "W F G FG",
    "W AB BC ABC",
    "W DE EF DEF",
    "W EF FG EFG"

]
# for line in fileinput.input():
for x in testCases:
    # split the command into a list of strings

    command = x.split()

    # if the command has three parts, marriage without kid, print all of statements
    if len(command) == 3:
        pass
        # is x a blank of y?
        if command[0] == 'X' or command[0] == 'x':
            pass
        # print all of relation
        if command[0] == 'W' or command[0] == 'w':
            pass
        # marriage statement
        if command[0] == 'E' or command[0] == 'e':
            if command[1] in familyTree:
                pass  # person already exists
            else:
                # create new person
                familyTree[command[1]] = 'no parent'
                spouses[command[1]] = command[2]
            if command[2] in familyTree:
                pass  # person already exists
            else:
                # create new person
                familyTree[command[2]] = 'no parent'
                spouses[command[2]] = command[1]
                pass

    # if the command has four parts, marriage with kids, print true or false for relation
    if len(command) == 4:
        pass
        # is x a blank of y?
        if command[0] == 'X' or command[0] == 'x':
            pass
        # print all of relation
        if command[0] == 'W' or command[0] == 'w':
            pass
        # marriage statement
        if command[0] == 'E' or command[0] == 'e':
            pass
    pass

