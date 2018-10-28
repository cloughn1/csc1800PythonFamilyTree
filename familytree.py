import fileinput

familyTree = {
    "Test": "test"
}
spouses = {
    "Test": "test"

}
testCases = [
    "E AA BB",
    "E AAA BB",
    "E AAAA BB",
    "E AAAAA BB",
    "E AAAAAA BB",
    "E A B AB",
    "E B C BC",
    "E C D DC",
    "E D E DE",
    "E E F EF",
    "E F G FG",
    "E AB BC ABC",
    "E DE EF DEF",
    "E EF FG EFG"

]
# for line in fileinput.input():
for x in testCases:
    # split the command into a list of strings

    command = x.split()
    print(command)
    print(len(command))
    # if the command has three parts, marriage without kid, print all of statements
    if len(command) == 3:
        pass
        # is x a blank of y?
        if command[0] == 'X' or command[0] == 'x':
            # Should never be passed in this context
            pass
        # print all of relation
        if command[0] == 'W' or command[0] == 'w':
            pass
            # ____________________End of return all_________________________________________________________________

        # marriage statement
        if command[0] == 'E' or command[0] == 'e':
            if command[1] in familyTree and command[1] in spouses:
                # person already exists
                temp = spouses[command[1]]
                temp = temp.split()
                inside = 0
                # temp is now the array of all spouses
                for i in temp:
                    if i == command[2]:
                        # if the spouse already exists, mark that
                        inside = 1
                if inside == 0:
                    # if the search failed to find the spouse, add them
                    temp = spouses[command[1]]+' '+command[2]
                    spouses[command[1]] = temp
            else:
                # create new person
                familyTree[command[1]] = 'no parent'
                spouses[command[1]] = command[2]
            if command[2] in familyTree and command[2] in spouses:
                # person already exists
                temp = spouses[command[1]]
                temp = temp.split()
                inside = 0
                for i in temp:
                    if i == command[1]:
                        # spouse exists
                        inside = 1
                if inside == 0:
                    # create spouse
                    temp = spouses[command[2]] + ' ' + command[1]
                    spouses[command[2]] = temp
            else:
                # create new person
                familyTree[command[2]] = 'no parent'
                spouses[command[2]] = command[1]
                pass
            # ________________________________End of marriage add_________________________________________________________________
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
            # Repetition of the spouses for only two people
            if command[1] in familyTree and command[1] in spouses:
                # person already exists
                temp = spouses[command[1]]
                temp = temp.split()
                inside = 0
                # temp is now the array of all spouses
                for i in temp:
                    if i == command[2]:
                        # if the spouse already exists, mark that
                        inside = 1
                if inside == 0:
                    # if the search failed to find the spouse, add them
                    temp = spouses[command[1]]+' '+command[2]
                    spouses[command[1]] = temp
            else:
                # create new person
                familyTree[command[1]] = 'no parent'
                spouses[command[1]] = command[2]
            if command[2] in familyTree and command[2] in spouses:
                # person already exists
                temp = spouses[command[1]]
                temp = temp.split()
                inside = 0
                for i in temp:
                    if i == command[1]:
                        # spouse exists
                        inside = 1
                if inside == 0:
                    # create spouse
                    temp = spouses[command[2]] + ' ' + command[1]
                    spouses[command[2]] = temp
            else:
                # create new person
                familyTree[command[2]] = 'no parent'
                spouses[command[2]] = command[1]
                pass
            # both parents are now created and in the trees
            familyTree[command[3]] = command[1]+' '+command[2]

    pass
print(familyTree)
print(spouses)
