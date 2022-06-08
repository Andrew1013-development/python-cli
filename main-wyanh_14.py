# dependencies
import pip
import os
import sys
import psutil
from datetime import date
from datetime import datetime
from time import sleep
from time import time
from termcolor import cprint as printc
from platform import python_version
from platform import python_compiler
from platform import python_implementation
from platform import release
from platform import system
from platform import platform

# command pallete
# ver : print version
# printstr [string] : print string 
# printvar [variable name] : print variable value (if no variable name is specified, printvar will print all variables available)
# definevar [variable type] [varianle type] [variable value] : define a varaible with value of selected type
# assignvar [variable name] [variable type] [new variable value] : assign a given variable a new value of selected type
# clearvar [variable name] : clear variable's value (reset value to blank)
# exit : exit cli
# time : display current day and time
# log : show log of commands executed
# wyanh_14 : showing social details of wyanh_14 (obtained through sources, accurate as of 5/2022)

# variable types
# integer, float : numbers
# string (default type)
# boolean : True / False

#version thingies
major = 0
minor = 0
rev = 0
branch = "m"
build = 1
base_version = "v0.0.0a6-0607"
note = "wyanh_14"
flag = "M1"
flag_desc = "MISC 1"
compiled_date = date(2022,6,8).strftime("%d/%m/%Y")
compile_tag = "0608"
version_string = f"v{major}.{minor}.{rev}{branch}{build}-{compile_tag}-{note}"
python_version = python_implementation() + " " + python_version()
python_compiler = python_compiler()
os_release = system() + " " + release()
os_version = platform().replace("-"," ",2)

#variables
pre_userin = ""
userin = ""
variables = {}
log = []
error = False

#main code
while userin != "exit" :
    try :
        error = False
        userin = input("> ")
        if userin == "ver" :
            print(f"Python CLI version {version_string}, based on {base_version}")
            print(f"Compiled on {compiled_date} with compilation tag {compile_tag}")
            if flag != "" :
                print(f"Flags for program : {flag} ({flag_desc})")
            print(f"Running on {python_version} [{python_compiler}]")
            print()
            print("(OS version might be inaccurate with Windows 10 and Windows 11)")
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
            var_name,var_type,var_value = [s for s in userin.removeprefix("assignvar ").split(" ")]
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
            print(string)
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
        elif userin == "time" :
            today = date.today().strftime("%d/%m/%Y")
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Current day and time : {today} {now}")
        elif userin == "log" :
            print("Commands log :")
            for i in range(0,len(log)) :
                print(f"{i+1} {log[i]}")
        elif userin == note :
            print("(note: information is accurate as of May 2022)")
            print("full name : Phan Nguyễn Minh Anh, class : 8TC2, school : THCS Chánh Hưng")
            print("Facebook : Minhh Anhh (https://www.facebook.com/ig_winhahnn_14)")
            print("Instagram : wyanh_14 (https://www.instagram.com/wyanh_14/)")
            print("TikTok : unknown")
        else :
            print("Error : Invaild command")
            error = True
        if error == False :
            log.append(userin)
        print() #print empty line
    except KeyboardInterrupt :
        print("\nExiting from Ctrl-C trigger...")
        break