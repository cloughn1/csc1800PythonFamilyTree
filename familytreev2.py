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
    "W child EF",
    "X A spouse B",
    "X AB spouse BC",
    "X A child B",
    "X A parent AB",
    "X A ancestor ABC",
    "X F unrelated XYZ",
    "X F unrelated A",
    "X F unrelated FG"
]

def getlistfrompeople (relation, persontwo) :
    ancestors = []
    children = []
    cousins = []
    related = []
    unrelated = []
    if relation == 'Ancestor' or relation == 'ancestor':
        ancestors = ["temp"]
        ancestors.clear()
        stack = ["temp"]
        stack.clear()
        if familyTree[persontwo] != 'no parent':
            parent = familyTree[persontwo].split()
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
        return ancestors
    if relation == 'Spouse' or relation == 'spouse':
        temp = spouses[persontwo].split()
        temp.sort()
        return temp
    if relation == 'Cousin' or relation == 'cousin':
        cousins = []
        listA = []
        stack = []
        listB = []
        stackB = []
        if persontwo in familyTree:
            if familyTree[persontwo] != 'no parent':
                parent = familyTree[persontwo].split()
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
                if i != persontwo:
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

                if persontwo not in listB and i not in listA:
                    for j in listA:

                        if j in listB:
                            if i not in cousins:
                                cousins.append(i)
                    for k in listB:

                        if k in listA:
                            if i not in cousins:
                                cousins.append(i)
            cousins.sort()
        return cousins
    if relation == 'Sibling' or relation == 'sibling':
        siblings = []
        if persontwo in familyTree:
            parentsA = familyTree[persontwo].split()
            for i in familyTree:
                if i != persontwo:
                    parentsB = familyTree[i].split()
                    for j in parentsB:
                        if j in parentsA:
                            siblings.append(i)
        siblings.sort()
        return siblings
    if relation == 'Child' or relation == 'child':
        kids = []
        if persontwo in familyTree:
            for i in familyTree:
                if i != persontwo:
                    parents = familyTree[i].split()
                    if persontwo in parents:
                        kids.append(i)
        kids.sort()
        return kids
    if relation == 'Unrelated' or relation == 'unrelated':
        ancestors.append(getlistfrompeople('ancestors', persontwo))
        children.append(getlistfrompeople('child', persontwo))
        cousins.append(getlistfrompeople('cousin', persontwo))
        related = ancestors + children + cousins
        related = list(related)
        everyone = list(familyTree.keys())
        unrelated = difflist(everyone, related)
        return unrelated

def difflist(listone, listtwo):
    difflist = []
    for i in listone:
        if i not in listtwo:
            difflist.append(i)
    return difflist


def ispersoninlist (person, relation, persontwo) :
    if relation == 'Ancestor' or relation == 'ancestor':
        ancestors = getlistfrompeople('ancestors', persontwo)
        if ancestors is None:
            return False
        if person in ancestors:
            return True
        return False
    if relation == 'Spouse' or relation == 'spouse':
        spouses = getlistfrompeople('spouses', persontwo)
        if spouses is None:
            return False
        if person in spouses:
            return True
        return False
    if relation == 'Cousin' or relation == 'cousin':
        cousins = getlistfrompeople('cousin', persontwo)
        if cousins is None:
            return False
        if person in cousins:
            return True
        return False
    if relation == 'Sibling' or relation == 'sibling':
        siblings = getlistfrompeople('siblings', persontwo)
        if siblings is None:
            return False
        if person in siblings:
            return True
        return False
    if relation == 'Child' or relation == 'child':
        children = getlistfrompeople('child', persontwo)
        if children is None:
            return False
        if person in children:
            return True
        return False
    if relation == 'Unrelated' or relation == 'unrelated':
        unrelated = getlistfrompeople('unrelated', persontwo)
        if unrelated is None:
            return False
        if person in unrelated:
            return True
        return False


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
            relationlist = getlistfrompeople(command[1], command[2])
            for i in relationlist:
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
            # ________________________________End of marriage add_________________________________________________________________
    # if the command has four parts, marriage with kids, print true or false for relation
    if len(command) == 4:
        pass

        # is x a blank of y?
        if command[0] == 'X' or command[0] == 'x':
            if (ispersoninlist(command[1], command[2], command[3])):
                print('Yes')
            else:
                print('No')

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
