import re
import os


def set_up(year):
    HEADER_TEXT = ["Prefix", "Last", "First", "Suffix",	"FilingType", "StateDst", "Year", "FilingDate", "DocID"]

    fileData = year + "FD"
    filename = os.path.abspath("Congress App Chall/Data/" + fileData + "/" + fileData + ".txt") #? might need changing to find Data properly when translated to exe in the Beta exes folder

    splitText = []

    with open(filename) as f:
        lines = f.readlines()

    for w in range(len(lines)):
        splitText.append(lines[w].split("\t"))

    stripText = []

    for a in range(len(splitText)):
        newList = []
        for r in range(len(splitText[a])):
            pieceOfText = splitText[a][r]
            newList.append(pieceOfText.strip())
        stripText.append(newList)

    # un-remove this when working with real data
    # stripText.remove(HEADER_TEXT)


    # for l in range(len(stripText)):
    #     print(stripText[l])
    #     print("\n")
    
    return stripText

def purchased_most(organized_FD, fileDataHere):

    # PMP = Purchased Most Person
    temp_PMP = 0
    new_PMP = 0
    length = (len(organized_FD))

    for p in range(len(organized_FD)):

        if p != length - 1:
            name1 = organized_FD[p][1], organized_FD[p][2]
            name2 = organized_FD[p + 1][1], organized_FD[p + 1][2]

            if name1 == name2:
                temp_PMP += 1
            else:
                if temp_PMP > new_PMP:
                    new_PMP = temp_PMP

                    temp_name = name1

                temp_PMP = 0
        
        else:
            name2 = organized_FD[p - 1][1], organized_FD[p - 1][2]

            if name1 == name2:
                temp_PMP += 1
            else:
                if temp_PMP > new_PMP:
                    new_PMP = temp_PMP
                    temp_PMP = 0
            
            if temp_PMP >  new_PMP:
                new_PMP = temp_PMP
            
            new_PMP -= 1

    temp_name = (temp_name[0] + ", " + temp_name[1])

    # index = find_index(organized_FD, temp_name)
    # temp_split_name = temp_name.split(",")
    # print(temp_split_name[1], temp_split_name[0], "purchased", new_PMP,"times in", fileDataHere, "and can be found", index, "lines from the top")  

    return temp_name, new_PMP

def find_index(organized_FD, person):

    indexSubCount = 0
    index = 0
    length = (len(organized_FD))

    name1 = person.split(",")

    for p in range(len(organized_FD)):

        person2 = organized_FD[p][1] + ", " + organized_FD[p][2]
        name2 = person2.split(",")

        if p < length:
            if p == 0:
                if name1 == name2:
                    index = p

            if p != 0:
                person3 = organized_FD[p - 1][1] + ", " + organized_FD[p - 1][2]
                name3 = person3.split(",")
                
                if name1 == name2:
                    index = p
                    
                    indexSubCount += 1

                elif name2 != name3 and name1 == name3:
                    indexSubCount = indexSubCount - 2
                    index = index - indexSubCount
    #                 print("index after sub",index)

    
    # print("index",index)
    # print("sub count",indexSubCount)
    
    return index

def how_much_one_purchase(organized_FD, fileYear, location_where, person):
    
    splitPerson = person.split(",")
    
    amount = 0
    index = 0

    for l in range(len(organized_FD)):
        person2 = organized_FD[l][1] + ", " + organized_FD[l][2]
        splitPerson2 = person2.split(",")

        if splitPerson == splitPerson2:
            amount += 1
            index = l
    
    # if organized_FD[index][0] != '':
    #     print(organized_FD[index][0], splitPerson[1], splitPerson[0], "purchased stocks", amount, "times in", fileYear, "and can be found", location_where, "lines from the top")
    # else:
    #     print(splitPerson[1], splitPerson[0], "purchased stocks", amount, "times in", fileYear, "and can be found", location_where, "lines from the top")

    return amount



# if __name__ == '__main__':
#     main()

# while True:
#     main()
