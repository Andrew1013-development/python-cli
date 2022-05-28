# dependencies
from datetime import date
from termcolor import cprint as printc
from datetime import datetime
from time import localtime
import os
import sys


# command pallete
# ver : print version
# printstr [string] : print string
# printvar [variable name] : print variable value
# definevar [variable name] [variable type] [variable value] : define a varaible with value of selected type
# assignvar [variable name] [value type] [new variable value] : assign a given variable a new value of selected type
# exit : exit cli

# variable types
# int, float : numbers
# string (default type)
# bool : True / False

#version thingies
major = 0
minor = 0
rev = 0
branch = "b"
build = 1
flag = "T1"
flag_desc = "TESTING 1"
compiled_date = date(2022,5,28)
compile_tag = "0528"
version_string = f"v{major}.{minor}.{rev}{branch}{build}"

#variables
pre_userin = ""
userin = ""
variables = {}
disabled_commands = []

#main code
while userin != "exit" :
    try :   
        pre_userin = userin
        userin = input("> ")
        if userin == "ver" :
            print(f"Python CLI version {version_string}, based on v0.0.0a4")
            print(f"Compiled on {compiled_date} with compilation tag {compile_tag}")
            if flag != "" :
                print(f"Flags for program : {flag} ({flag_desc})")
        #needs fixing
        elif userin == "bug" :
            print("bug reporting coming soon!")
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
                print(f"Variable {var_name} does not exist!")
        elif "printstr" in userin :
            printstr_input = [s for s in userin.removeprefix("printstr ").split(" ")]
            string = " ".join(printstr_input)
            print(string)
        elif "printvar" in userin :
            var_name = [s for s in userin.split(" ")][1]
            if var_name in variables.keys() :
                print(variables[var_name])
            else :
                print(f"Variable {var_name} does not exist!")
        elif "printc " in userin :
            printc_input = [s for s in userin.removeprefix("printc ").split(" ")]
            color = printc_input[len(printc_input)-1]
            printc_input.remove(color)
            string = " ".join(printc_input)
            printc(string, color)
        elif userin == "exit" :
            print("Exiting...")
            break
        else :
            print("Error : Invaild command")
        print() #print empty line
    except KeyboardInterrupt :
        print("\nExiting from Ctrl-C trigger...")
        break