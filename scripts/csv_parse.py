import os
import sys
import pandas as pd

comma_mode = True
def choose_sign(sign):
    global comma_mode
    match sign:
        case "(":
            comma_mode = False
            return sign
        case ")":
            comma_mode = True
            return sign
        case ",":
            if comma_mode:
                return sign
            else:
                return ";"
        case "\n":
            return ''
        case _:
            return sign

def string_builder(data):
    formatted_data = ""
    comma_num = 0
    for x in data:
        new_char = choose_sign(x)
        formatted_data += new_char
        if(new_char == ","):
            comma_num += 1
            if(comma_num == 8):
                formatted_data += "\n"
                comma_num = 0
    return formatted_data
            
        

def main():
    csv_type_data = string_builder(sys.argv[1])
    
    with open("results.csv", "w") as fileWriter:
        fileWriter.write(csv_type_data)

    read = pd.read_csv('results.csv')
    read.to_excel('results.xlsx', header=False, index=False)
    os.remove('results.csv')
main()