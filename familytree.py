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
    "E EF FG EFG",
    "W Ancestor EFG"

]
# for line in fileinput.input():
for x in testCases:
    # split the command into a list of strings

    command = x.split()
    print(command)

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
            if command[1] == 'Ancestor' or command[1] == 'ancestor':
                ancestors = ["temp"]
                ancestors.clear()
                stack = ["temp"]
                stack.clear()
                if familyTree[command[2]] != 'no parent':
                    parent = familyTree[command[2]].split()
                    stack.append(parent[0])
                    stack.append(parent[1])
                    current = stack.pop()
                    true = 1;
                    while true == 1:
                        if current not in ancestors:
                            ancestors.append(current)
                        if familyTree[current] != 'no parent':

                            parent = familyTree[current].split()
                            stack.append(parent[0])
                            stack.append(parent[1])
                        if len(stack) == 0:
                            break
                        current = stack.pop()
                    ancestors.sort()
                    for j in range(0, len(ancestors)):
                        print(ancestors[j])
            if command[1] == 'Spouse' or command[1] == 'spouse':
                pass
            if command[1] == 'Cousin' or command[1] == 'cousin':
                pass
            if command[1] == 'Sibling' or command[1] == 'sibling':
                pass
            if command[1] == 'Child' or command[1] == 'child':
                pass
            if command[1] == 'Unrelated' or command[1] == 'unrelated':
                pass

        # marriage statement
        if command[0] == 'E' or command[0] == 'e':
            if command[1] in familyTree:
                # person already exists
                if command[1] in spouses:

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
                    spouses[command[1]] = command[2]
            else:
                # create new person
                familyTree[command[1]] = 'no parent'
                spouses[command[1]] = command[2]
            if command[2] in familyTree:
                # person already exists
                if command[2] in spouses:

                    temp = spouses[command[2]]
                    temp = temp.split()
                    inside = 0
                    # temp is now the array of all spouses
                    for i in temp:
                        if i == command[2]:
                            # if the spouse already exists, mark that
                            inside = 1
                    if inside == 0:
                        # if the search failed to find the spouse, add them
                        temp = spouses[command[2]]+' '+command[1]
                        spouses[command[2]] = temp
                else:
                    spouses[command[2]] = command[1]
            else:
                # create new person
                familyTree[command[2]] = 'no parent'
                spouses[command[2]] = command[1]
            # ________________________________End of marriage add_________________________________________________________________
    # if the command has four parts, marriage with kids, print true or false for relation
    if len(command) == 4:
        pass

        # is x a blank of y?
        if command[0] == 'X' or command[0] == 'x':
            if command[2] == 'Ancestor' or command[2] == 'ancestor':
                pass
            if command[2] == 'Spouse' or command[2] == 'spouse':
                pass
            if command[2] == 'Cousin' or command[2] == 'cousin':
                pass
            if command[2] == 'Sibling' or command[2] == 'sibling':
                pass
            if command[2] == 'Child' or command[2] == 'child':
                pass
            if command[2] == 'Unrelated' or command[2] == 'unrelated':
                pass

        # print all of relation
        if command[0] == 'W' or command[0] == 'w':
            # should never occur
            pass

        # marriage statement
        if command[0] == 'E' or command[0] == 'e':
            # Repetition of the spouses for only two people
            if command[1] in familyTree:
                # person already exists
                if command[1] in spouses:

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
                    spouses[command[1]] = command[2]
            else:
                # create new person
                familyTree[command[1]] = 'no parent'
                spouses[command[1]] = command[2]
            if command[2] in familyTree:
                # person already exists
                if command[2] in spouses:

                    temp = spouses[command[2]]
                    temp = temp.split()
                    inside = 0
                    # temp is now the array of all spouses
                    for i in temp:
                        if i == command[2]:
                            # if the spouse already exists, mark that
                            inside = 1
                    if inside == 0:
                        # if the search failed to find the spouse, add them
                        temp = spouses[command[2]]+' '+command[1]
                        spouses[command[2]] = temp
                else:
                    spouses[command[2]] = command[1]
            else:
                # create new person
                familyTree[command[2]] = 'no parent'
                spouses[command[2]] = command[1]
            # both parents are now created and in the trees
            familyTree[command[3]] = command[1]+' '+command[2]

    pass
print(familyTree)
print(spouses)
