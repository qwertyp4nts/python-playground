import sys
import csv
import re


def main():
    args = sys.argv[1:]
    if len(args) != 2:
        print("Usage: python dna.py data.csv sequence.txt")
        return 1
    with open(args[0], "r") as file:
        people = [line.split() for line in file]

    lineLength = len(people[0][0].split(","))
    
    # Split first row of array into 3d array, to get our DNA headers
    people[0][0] = people[0][0].split(",")
    
    with open(args[1], "r") as file2:
        personDNA = [line.split() for line in file2]
    
    buildstr = []
    sequence = personDNA[0][0]
    
    for i in range(1, lineLength, 1):
        keyword = people[0][0][i]
        loners = len(re.findall(f"((?<!{keyword})({keyword})(?!{keyword}))", sequence))
        
        allOccurences = len(re.findall(f"({people[0][0][i]})", sequence))
        
        # this is a bit of a hack. if theres only one occurence, add 1, so that we don't have to change the code below
        if allOccurences == 1:
            allOccurences += 1 
        
        # build a regex to see if the csv really contains the expected amount of 'keyword's in a row.
        # this is to ensure, there aren't other 'groups' of keywords in the csv (multiple groups are possible, we are just looking for the biggest one)
        regexStr = r'(%s){%d}' % (keyword, allOccurences - loners)
        if re.search(regexStr, sequence):
            buildstr.append(allOccurences - loners)
        else:  # if we are here, it means it has found multiple blocks. Iterate down from expected, and find the biggest block we can
            for i in range(allOccurences - loners - 1, 0, -1):
                regexStr2 = r'(%s){%d}' % (keyword, i)
                if re.search(regexStr2, sequence):
                    buildstr.append(i)
                    break
    
    separator = ''
    dnaStr = separator.join(str(buildstr))
    dnaStri = dnaStr.replace(" ", "").replace("[", "").replace("]", "")
    
    for person in range(1, len(people), 1):
        if re.search(f",{dnaStri}$", people[person][0]):
            target = people[person][0].split(",")
            print(target[0])
            return 0
        
    print("No match")
    return 0


main()