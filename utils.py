def ListOfCharsToString(string):

    listOfStrings = []
    for list in string:
        # initialization of string to ""
        new = ""
    
        # traverse in the string
        for x in list:
            new += x
    
        # return string
        listOfStrings.append(new)
    
    return listOfStrings

def strToListOfChars(string):
    lst = []
    for letter in string:
        lst.append(letter)
    return lst