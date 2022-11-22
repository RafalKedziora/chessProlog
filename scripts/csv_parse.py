def goodFormat(data):
    commaMode = True
    commaNum = 0
    newString = ""
    for x in data:
        if x == "(":
            newString += x
            commaMode = False
        elif x == ")":
            newString += x
            commaMode = True
        elif x == ",":
            if commaMode:
                commaNum += 1 
                newString += ";"
            else:
                newString += x
        elif x == "\n":
            pass
        else:
            newString += x
        if commaNum == 8:
            newString += "\n"
            commaNum = 0
    return newString
            
        

def main():
    with open("dopytona.txt", "r+") as file:
        data = file.read()

    newString = goodFormat(data)

    with open("nalejkurwiemiodu.csv", "w") as fileWriter:
        fileWriter.write(newString)
main()