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
    "E ABCDEF EFG ABCDEFG",
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
    "W child EF",
    "X A Spouse B",  # should be yes
    "X AA Spouse BB",  # should be yes
    "X EFG Spouse A",  # should be no
    "X E Ancestor EFG",  # should be yes
    "X EFG Ancestor EF",  # should be no
    "X ABCDEF Cousin EFG",   # should be yes
    "X AB Sibling BC",  # should be yes
    "X AB Child A",  # should be yes
    "X B Child BC",  # should be no
    "W unrelated A",
    "W unrelated B",
    "W unrelated ABCDEFG",
    "X B unrelated A"

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
        if familyTree[name] != "no parent":
            parentsA = familyTree[name].split()
            for iname in familyTree:
                if iname not in sibs:
                    if iname != name:
                        parentsB = familyTree[iname].split()
                        for jname in parentsB:
                            if jname in parentsA:
                                if iname not in sibs:
                                    sibs.append(iname)
            return sibs


def get_ancestors(name):
    if name in familyTree:
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
                    if parent[0] not in stack:
                        stack.append(parent[0])
                    if parent[1] not in stack:
                        stack.append(parent[1])
                if len(stack) == 0:
                    break
                current = stack.pop()
            return ancs


def get_cousins(name):
    cous = []
    listA = []
    stack = []
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
                    if parent[0] not in stack and parent[0] not in listA:
                        stack.append(parent[0])
                    if parent[1] not in stack and parent[1] not in listA:
                        stack.append(parent[1])

                if len(stack) == 0:
                    break

                current = stack.pop()
               # while current in listA:
                #    if len(stack) == 0:
                 #       break
                  #  current = stack.pop()

            listA.sort()
        # ListTemp = []
        for iname in familyTree:
            # print(i)
            listB = []
            if iname != name:
                if familyTree[iname] != 'no parent':
                    parent = familyTree[iname].split()
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
                            if parent[0] not in stackB and parent[0] not in listB:
                                stackB.append(parent[0])
                            if parent[1] not in stackB and parent[1] not in listB:
                                stackB.append(parent[1])
                        if len(stackB) == 0:
                            break
                        current = stackB.pop()
                        # while current in listB:
                          #  if len(stackB) == 0:
                           #     break
                            #current = stackB.pop()
                    listB.sort()

            if name not in listB and iname not in listA:
                for jname in listA:

                    if jname in listB:
                        if iname not in cous:
                            cous.append(iname)
                for kname in listB:

                    if kname in listA:
                        if iname not in cous:
                            cous.append(iname)
        return cous


def get_unrelated(name):
    relation = []
    related = 0
    unrelation = []
    for i in familyTree:
        relation.append(i)
    for j in relation:
        related=0;
        temp = get_ancestors(name)
        if temp != None:
            if j in temp:
                related = 1
        temp = get_siblings(name)
        if temp != None:
            if j in get_siblings(name):
                related = 1
        if j in get_children(name):
            related = 1
        if j in get_cousins(name):
            related = 1
        temp = get_ancestors(j)
        if temp != None:
            if name in temp:
                related = 1
        temp = get_ancestors(j)
        if temp != None:
            if name in get_siblings(j):
                related = 1
        if name in get_children(j):
            related = 1
        if name in get_cousins(j):
            related = 1

        if related == 0:
            unrelation.append(j)

    return unrelation


for x in fileinput.input():
# for x in testCases:

    # split the command into a list of strings
    # print(x)
    command = x.split()
    # print(command)
    # if command is None: break
    if command[0] != 'E':
        print(x)
    # print(command)

    # if the command has three parts, marriage without kid, print all of statements
    if len(command) == 3:
        pass
        # is x a blank of y?
        if command[0] == 'X' or command[0] == 'x':
            # Should never be passed in this context
            pass
        # print all of relation
        if command[0] == 'W' or command[0] == 'w':
            if command[2] in familyTree:
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
                    unrelated = get_unrelated(command[2])
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
            if command[2] == 'Unrelated' or command[2] == 'unrelated':
                answer = "Yes"
            else:
                answer = "No"

            if command[1] in familyTree and command[3] in familyTree:
                if command[2] == 'Ancestor' or command[2] == 'ancestor':
                    ancestors = get_ancestors(command[3])
                    if ancestors != None:
                        if command[1] in ancestors:
                            answer = "Yes"
                if command[2] == 'Spouse' or command[2] == 'spouse':
                    if command[1] in spouses[command[3]]:
                        answer = "Yes"
                if command[2] == 'Cousin' or command[2] == 'cousin':
                    if command[3] in familyTree:
                        cousins = get_cousins(command[3])
                        if command[1] in cousins:
                            answer = "Yes"
                if command[2] == 'Sibling' or command[2] == 'sibling':
                    siblings = get_siblings(command[3])
                    if siblings != None:
                        if command[1] in siblings:
                            answer = "Yes"
                if command[2] == 'Child' or command[2] == 'child':
                    kids = get_children(command[3])
                    if command[1] in kids:
                        answer = "Yes"
                if command[2] == 'Unrelated' or command[2] == 'unrelated':
                    unrelated = get_unrelated(command[3])
                    if command[1] in unrelated:
                        answer = "Yes"
                    else:
                        answer = "No"
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


