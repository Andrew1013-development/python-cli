# dependencies
import pip
from os import path
import sys
import psutil #module needs to be installed
from datetime import date
from datetime import datetime
from time import sleep
from time import time
from timeit import timeit #module needs to be installed
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
# readtxt [file_name] : read text files and displaying the contents (line-by-line for now)
# writetxt [file_name] [string]: write a string to text, will create file if file does not exist 
# cwd : print current directory CLI is in
# credit : showing credits (will be available on the first Release Candidate (rc) build or the final / third Beta (b) build)

# variable types
# integer, float : numbers
# string (default type)
# boolean : True / False
# auto : dynamically determined (not available with assignvar)

#version thingies
major = 0
minor = 0
rev = 0
branch = "a"
build = 8
flag = "C8"
flag_desc = "CONCEPTION 8"
compiled_date = date(2022,6,9).strftime("%d/%m/%Y")
compile_tag = "0609"
version_string = f"v{major}.{minor}.{rev}{branch}{build}-{compile_tag}"
python_version = f"{python_implementation()} {python_version()}"
python_compiler = python_compiler()
os_release = system() + " " + release()
os_version = platform().replace("-"," ",2)

#variables
pre_userin = ""
userin = ""
variables = {}
log = []
error = False
work_dir = path.dirname(path.realpath(__file__))

#main code
while userin != "exit" :
    try :
        error = False
        userin = input("> ")
        if userin == "ver" :
            print(f"Python CLI version {version_string}")
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
            elif var_type == "auto" :
                var_value = eval(var_value)
            else :
                print("Invaild variable type")
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
            elif var_type == "auto" :
                var_value = eval(var_value)
            try :
                variables[var_name] = var_value #assign variable and value
            except KeyError :
                print(f"Variable {var_name} does not exist.")
                error = True
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
                    print("There's no varaibles.")
                    error = True
                else :
                    print("currently available variables :")
                    for key in variables :  
                        print(f"{key} <- {variables[key]} (type : {type(variables[key])})")
            else :
                var_name = [s for s in userin.split(" ")][1]
                if var_name in variables.keys() :
                    print(variables[var_name])
                else :
                    print(f"Variable {var_name} does not exist.")
                    error = True
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
        elif "readtxt" in userin :
            filename = userin.removeprefix("readtxt ")
            if ".txt" not in filename :
                filename += ".txt"
            filepath = path.join(work_dir,filename)
            try :
                with open(filepath,"r") as file_read :
                    strings = file_read.readlines()
                    file_read.close()
                    for ele in strings :
                        print(ele)
            except FileNotFoundError :
                print(f"{filepath} does not exist.")
                error = True
        elif "writetxt" in userin :
            filename,string = [s for s in userin.removeprefix("writetxt ").split(" ")]
            if ".txt" not in filename :
                filename += ".txt"
            filepath = path.join(work_dir,filename)
            with open(filepath,"w") as file_write :
                file_write.write(string)
                file_write.close()
                print("String written to file successfully.")
        elif userin == "cwd" :
            print(work_dir)
        elif userin == "log" :
            print("Commands log :")
            for i in range(0,len(log)) :
                print(f"{i+1} {log[i]}")
        else :
            print("Error : Invaild command")
            error = True
        if error == False :
            log.append(userin)
        print() #print empty line
    except KeyboardInterrupt :
        print("\nExiting from Ctrl-C trigger...")
        break