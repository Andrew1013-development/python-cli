#requirements : Python 3.9+ 
#tested on Python 3.10.4 and Python 3.11.0a7

# dependencies
from datetime import date
from datetime import datetime   
#from termcolor import cprint as printc
import time

# command pallete
# ver : print version
# printstr [string] : print string
# printvar [variable name] : print variable value
# definevar [variable name] [variable type] [variable value] : define a varaible with value of selected type
# assignvar [variable name] [value type] [new variable value] : assign a given variable a new value of selected type
# printc [string] [color] : print string with colors
# date : print current date
# time : print current time
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
build = 4
flag = "C4"
flag_desc = "CONCEPTION 4"
compiled_date = date(2022,5,17)
compile_tag = "0517"
version_string = f"v{major}.{minor}.{rev}{branch}{build}"

#variables
userin = ""
variables = {}

#main code
while userin != "exit" :
    userin = input()
    if userin == "ver" :
        print(f"Python CLI version {version_string}")
        print(f"Compiled on {compiled_date} with compilation tag {compile_tag}")
        if flag != "" :
            print(f"Flags for program : {flag} ({flag_desc})")
    elif userin == "exit" :
        break
    elif userin == "date" :
        print(datetime.now().strftime("%H:%M:%S"))
    elif userin == "time" :
        print(time.strftime("%H:%M:%S", time.localtime()))
    elif "definevar" in userin :
        var_name,var_type,var_value = [s for s in userin.removeprefix("definevar ").split(" ")]
        #type determination
        if var_type == "int" :
            var_value = int(var_value)  
        elif var_type == "float" :
            var_value = float(var_value)
        elif var_type == "bool" :
            var_value = bool(var_value)
        variables[var_name] = var_value #assign variable and value
    elif "assignvar" in userin :
        var_type,var_name,var_value = [s for s in userin.removeprefix("definevar ").split(" ")]
        #type determination
        if var_type == "int" :
            var_value = int(var_value)  
        elif var_type == "float" :
            var_value = float(var_value)
        elif var_type == "bool" :
            var_value = bool(var_value)
        try :
            variables[var_name] = var_value #assign variable and value
        except KeyError :
            print(f"No variable name : {var_name}")
    elif "printstr" in userin :
        print([s for s in userin.split(" ")][1])
    elif "printvar" in userin :
        print(variables[[s for s in userin.split(" ")][1]])
    else :
        print("Error : Invaild command")
    '''
    elif "printc" in userin :
        string,color = [s for s in userin.removeprefix("printc ").split(" ")]
        printc(string,color)
    '''
    
    print() #print empty line
