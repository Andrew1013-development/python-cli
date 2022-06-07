# dependencies
from datetime import date
from termcolor import cprint as printc
from datetime import datetime
from time import localtime
from platform import python_version
from platform import release
from platform import system
from platform import platform
import os
import sys

# command pallete
# ver : print version
# printstr [string] : print string 
# printvar [variable name] : print variable value (if no variable name is specified, printvar will print all variables available)
# definevar [variable type] [varianle type] [variable value] : define a varaible with value of selected type
# assignvar [variable name] [variable type] [new variable value] : assign a given variable a new value of selected type
# clearvar [variable name] : clear variable's value (reset value to blank)
# exit : exit cli

# variable types
# integer, float : numbers
# string (default type)
# boolean : True / False

#version thingies
major = 0
minor = 0
rev = 0
branch = "a"
build = 5
flag = "C5"
flag_desc = "CONCEPTION 5"
compiled_date = date(2022,6,7)
compile_tag = "0607"
version_string = f"v{major}.{minor}.{rev}{branch}{build}"
python_version = python_version()
os_release = system() + " " + release()
os_version = platform().replace("-"," ",2)

#variables
userin = ""
variables = {}

#main code
while userin != "exit" :
    try :
        userin = input("> ")
        if userin == "ver" :
            print(f"Python CLI version {version_string}")
            print(f"Compiled on {compiled_date} with compilation tag {compile_tag}")
            if flag != "" :
                print(f"Flags for program : {flag} ({flag_desc})")
            print(f"Ran on Python version {python_version}")
            print(f"Operating system : {os_release}")
            print(f"OS Version : {os_version}")
        elif userin == "exit" :
            print("Exiting...")
            break
        elif "definevar" in userin :
            var_type,var_name,var_value = [s for s in userin.removeprefix("definevar ").split(" ")]
            #type determination
            if var_type == "integer" :
                var_value = int(var_value)  
            elif var_type == "float" :
                var_value = float(var_value)
            elif var_type == "boolean" :
                var_value = bool(var_value)
            variables[var_name] = var_value #assign variable and value
        elif "assignvar" in userin :
            var_name,var_type,var_value = [s for s in userin.removeprefix("definevar ").split(" ")]
            #type determination
            if var_type == "integer" :
                var_value = int(var_value)  
            elif var_type == "float" :
                var_value = float(var_value)
            elif var_type == "boolean" :
                var_value = bool(var_value)
            try :
                variables[var_name] = var_value #assign variable and value
            except KeyError :
                print(f"Variable {var_name} does not exist!")
        elif "clearvar" in userin :
            var_name = [s for s in userin.split(" ")][1]
            del variables[var_name]
        elif "printstr" in userin :
            printstr_input = [s for s in userin.removeprefix("printstr ").split(" ")]
            string = " ".join(printstr_input)
        elif "printvar" in userin :
            if userin == "printvar" :
                if variables == {} :
                    print("There's no varaibles")
                else :
                    print("currently available variables :")
                    for key in variables :  
                        print(f"{key} <- {variables[key]} (type : {type(variables[key])})")
            else :
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
        else :
            print("Error : Invaild command")
        print() #print empty line
    except KeyboardInterrupt :
        print("\nExiting from Ctrl-C trigger...")
        break