import fileinput

familyTree = {
}
spouses = {
}
testCases = [
    "E AA BB",
    "E AAA BB",
    "E AAAA BB",
    "E AAAAA BB",
    "E AAAAAA BB",
    "E A B AB",
    "E A C AC",
    "E A D AD",
    "E A E AE",
    "E A F AF",
    "E A G AG",
    "E A H AH",
    "E B C BC",
    "E C D DC",
    "E D E DE",
    "E E F EF",
    "E F G FG",
    "E AB BC ABC",
    "E DE EF DEF",
    "E EF FG EFG",
    "E ABC DEF ABCDEF",
    "E ABCDEF EFG SBCDEFG",
    "E AC DC ACDC",
    "E EF AD EFAD",
    "E BC EFG BCEFG",
    "W Spouse A",
    "W Spouse BB",
    "W Spouse EFG",
    "W Ancestor EFG",
    "W cousin EFG",
    "W cousin ACDC",
    "W sibling AB",
    "W sibling FG",
    "W child A",
    "W child B",
    "W child EF"

]


def get_children(name):
    children = []
    if name in familyTree:
        for i in familyTree:
            if i != command[2]:
                parents = familyTree[i].split()
                if name in parents:
                    children.append(i)
        return children


def get_siblings(name):
    sibs = []
    if name in familyTree:
        parentsA = familyTree[name].split()
        for i in familyTree:
            if i != name:
                parentsB = familyTree[i].split()
                for j in parentsB:
                    if j in parentsA:
                        sibs.append(i)
        return sibs


def get_ancestors(name):
    ancs = ["temp"]
    ancs.clear()
    stack = ["temp"]
    stack.clear()
    # Person is not at top of the Family Tree
    if familyTree[name] != 'no parent':
        parent = familyTree[name].split()
        stack.append(parent[0])
        stack.append(parent[1])
        # focus on parent just popped off
        current = stack.pop()
        true = 1
        while true == 1:
            # put current in ancestors
            if current not in ancs:
                ancs.append(current)
            # Stops when reach the top of family tree
            if familyTree[current] != 'no parent':
                parent = familyTree[current].split()
                stack.append(parent[0])
                stack.append(parent[1])
            if len(stack) == 0:
                break
            current = stack.pop()
        return ancs


def get_cousins(name):
    cous = []
    listA = []
    stack = []
    listB = []
    stackB = []
    if name in familyTree:
        if familyTree[name] != 'no parent':
            parent = familyTree[name].split()
            stack.append(parent[0])
            stack.append(parent[1])
            current = stack.pop()
            true = 1
            while true == 1:
                if current not in listA:
                    listA.append(current)
                if familyTree[current] != 'no parent':
                    parent = familyTree[current].split()
                    stack.append(parent[0])
                    stack.append(parent[1])
                if len(stack) == 0:
                    break
                current = stack.pop()
            listA.sort()
        ListTemp = []
        for i in familyTree:
            # print(i)
            listB = []
            if i != command[2]:
                if familyTree[i] != 'no parent':
                    parent = familyTree[i].split()
                    stackB.append(parent[0])
                    stackB.append(parent[1])
                    current = stackB.pop()
                    true = 1
                    # print("--------------")
                    while true == 1:
                        if current not in listB:
                            listB.append(current)
                        if familyTree[current] != 'no parent':
                            parent = familyTree[current].split()
                            stackB.append(parent[0])
                            stackB.append(parent[1])
                        if len(stackB) == 0:
                            break
                        current = stackB.pop()
                    listB.sort()

            if name not in listB and i not in listA:
                for j in listA:

                    if j in listB:
                        if i not in cous:
                            cous.append(i)
                for k in listB:

                    if k in listA:
                        if i not in cous:
                            cous.append(i)
        return cous


def get_related(name):
    relation = []
    for i in get_ancestors(name):
        relation.append(i)


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
                ancestors = get_ancestors(command[2])
                ancestors.sort()
                for j in range(0, len(ancestors)):
                    print(ancestors[j])
            if command[1] == 'Spouse' or command[1] == 'spouse':
                if command[2] in spouses:
                    temp = spouses[command[2]].split()
                    temp.sort()
                    for i in range(0, len(temp)):
                        print(temp[i])
            if command[1] == 'Cousin' or command[1] == 'cousin':
                cousins = get_cousins(command[2])
                cousins.sort()
                for i in cousins:
                    print(i)
            if command[1] == 'Sibling' or command[1] == 'sibling':
                siblings = get_siblings(command[2])
                siblings.sort()
                for i in siblings:
                    print(i)
            if command[1] == 'Child' or command[1] == 'child':
                kids = get_children(command[2])
                kids.sort()
                for i in kids:
                    print(i)
            if command[1] == 'Unrelated' or command[1] == 'unrelated':
                unrelated = []
                if command[2] in familyTree:
                    pass
                unrelated.sort()
                for i in unrelated:
                    print(i)

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
            # _________________________End of marriage add_______________________________________________________
    # if the command has four parts, marriage with kids, print true or false for relation
    if len(command) == 4:
        pass

        # is x a blank of y?
        if command[0] == 'X' or command[0] == 'x':
            answer = "No"
            if command[2] == 'Ancestor' or command[2] == 'ancestor':
                ancestors = get_ancestors(command[3])
                if command[1] in ancestors:
                    answer = "Yes"
            if command[2] == 'Spouse' or command[2] == 'spouse':
                if command[1] in spouses[command[3]]:
                    answer = "Yes"
            if command[2] == 'Cousin' or command[2] == 'cousin':
                cousins = get_cousins(command[3])
                if command[1] in cousins:
                    answer = "Yes"
            if command[2] == 'Sibling' or command[2] == 'sibling':
                siblings = get_siblings(command[3])
                if command[1] in siblings:
                    answer = "Yes"
            if command[2] == 'Child' or command[2] == 'child':
                kids = get_children(command[3])
                if command[1] in kids:
                    answer = "Yes"
            if command[2] == 'Unrelated' or command[2] == 'unrelated':
                pass
            print(answer)

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
