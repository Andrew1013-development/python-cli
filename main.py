# dependencies
from datetime import date

# command pallete
# ver : print version
# printstr [string] : print string
# printvar [variable name] : print variable value
# definevar [variable name] [variable type] [variable name] : define a varaible with valur
# exit : exit cli

# variable types
# int, float : numbers
# string (default type)
# bool : True / False

#version shits
major = 0
minor = 0
rev = 0
branch = "a"
build = 2
flag = "C2"
flag_desc = "CONCEPTION 2"
compiled_date = date(2022,5,12)
version_string = f"v{major}.{minor}.{rev}{branch}{build}"

#variables
userin = ""
variables = {}

#main code
while userin != "exit" :
    userin = input()
    if userin == "ver" :
        print(f"Python CLI version {version_string}")
        print(f"Compiled on {compiled_date}")
        if flag != "" :
            print(f"Flags for program : {flag} ({flag_desc})")
    elif userin == "exit" :
        break
    elif "definevar" in userin :
        var_type,var_name,var_value = [s for s in userin.removeprefix("definevar ").split(" ")]
        #type determination
        if var_type == "int" :
            var_value = int(var_value)  
        elif var_type == "float" :
            var_value = float(var_value)
        elif var_type == "bool" :
            var_value = bool(var_value)
        variables[var_name] = var_value #assign variable and value
    elif "printstr" in userin :
        print([s for s in userin.split(" ")][1])
    elif "printvar" in userin :
        print(variables[[s for s in userin.split(" ")][1]])
    else :
        print("Error : Invaild command")
    print() #print empty line
