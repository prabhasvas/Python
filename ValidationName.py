import re

isValid = True
errorMessage = ""

def containsNumber(name):
    return any(char.isdigit() for char in name)

def validateSingleQuotes(subStr):
    print("current substring: ", subStr)
    count = 0
    singleQuotesFlag = False
    for char in subStr:
        count = count + 1

        if (char == "'" and count ==1):
            singleQuotesFlag = True
        elif (char != "'" and singleQuotesFlag == True):
            singleQuotesFlag = False
        elif(char == "'" and singleQuotesFlag == False):
            return False
    return True

def printResult():
    if (isValid == True):
        print("Congrats, Valid Name!", errorMessage)
    else:
        print("Sorry, Name Validation Failed!", errorMessage)

def stringValidation(name):
    names = name.split()

    for subString in names:
        if (subString.startswith("-") or subString.endswith("-")):
            errorMessage = "hyphen at beginning or end of a sub-string.."
            isValid = False
            break
        if (subString.startswith("'")):
            errorMessage = "Sub-string starts with single-quotes.."
            isValid = False
            break

        if "'" in subString:
            status = validateSingleQuotes(subString[1:])
            if (status == False):
                errorMessage = "Single-quotes is at incorrect index position.."
                isValid = False
                break



name = input("Enter a name: ")

# Check for presence of any Number. If number present, display "Validation Failed" message and exit
hasNum = containsNumber(name)
if (hasNum == True):
    print("Sorry, Name Validation Failed. It contains Number!")
    exit(0)

# Check for presence of special characters which are not allowed. If number present, display "Validation Failed" message and exit
if re.match("^[a-zA-Z']*$", name):
    isValid = True
else:
    errorMessage = "Contains unallowed characters.."
    isValid = False

#String validation - Check for incorrect positioning of hyphen and single-quotes
isValid = stringValidation(name)

printResult()





