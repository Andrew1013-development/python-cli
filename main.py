# dependencies
import pip
from os import path
from os import remove
from os import system as os_sys
from os import name
import sys
import psutil #module needs to be installed
from datetime import date
from datetime import datetime
from time import sleep
from time import time
from timeit import timeit #module needs to be installed
from termcolor import cprint as printc #module needs to be installed
from platform import python_version
from platform import python_compiler
from platform import python_implementation
from platform import release
from platform import system as pt_sys
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
# log [view / export]: show log of commands executed / export log to log.txt
# readtxt [file_name] : read text files and displaying the contents (line-by-line for now)
# writetxt [file_name] [string]: write a string to text, will create file if file does not exist 
# deltxt [file_name] : delete a text file
# cwd : print current directory CLI is in
# credit : showing credits (will be available on the first Release Candidate (rc) build or the final / third Beta (b) build)
# help : show command pallete

# variable types
# integer, float : numbers
# string (default type)
# boolean : True / False
# auto : dynamically determined (not available with assignvar)

#version thingies
major = 0
minor = 0
rev = 0
branch = "rc"
build = 1
flag = f"R{build}"
flag_desc = f"READY {build}"
base_version = "v0.0.0b4-0619"
compiled_date = date(2022,6,23).strftime("%d/%m/%Y")
compile_tag = "0623"
version_string = f"v{major}.{minor}.{rev}{branch}{build}-{compile_tag}"
python_version = f"{python_implementation()} {python_version()}"
python_compiler = python_compiler()
os_release = pt_sys() + " " + release()
os_version = platform().replace("-"," ",2)
#variables
pre_userin = ""
userin = ""
variables = {}
log = []
error = False
work_dir = path.dirname(path.realpath(__file__))

#functions

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
            if "Windows 10" in os_release :
                os_build = os_version[11:]
                for i in range(0,2) :
                    current_dot_position = os_build.index(".")
                    os_build = os_build[current_dot_position + 1:]
                os_build = os_build[:5]
                if int(os_build) >= 21996 :
                    os_release = "Windows 11"
                else :
                    os_release = "Windows 10"
            print(f"Operating system : {os_release}")
            print(f"OS Version : {os_release} {os_version[11:]}")
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
            elif var_type == "string" :
                pass
            elif var_type == "auto" :
                var_type = type(var_value).__name__
                if var_type == "int" :
                    var_value = int(var_value)  
                elif var_type == "float" :
                    var_value = float(var_value)
                elif var_type == "bool" :
                    var_value = bool(var_value)
                else :
                    var_value = str(var_value)
            else :
                print("Invaild variable type")
                error = True
            if error != True :
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
            elif var_type == "string" :
                pass
            elif var_type == "auto" :
                var_type = type(var_value).__name__
                if var_type == "int" :
                    var_value = int(var_value)  
                elif var_type == "float" :
                    var_value = float(var_value)
                elif var_type == "bool" :
                    var_value = bool(var_value)
                else :
                    var_value = str(var_value)
            else :
                print("Invaild variable type")
            try :
                variables[var_name] = var_value #assign variable and value
            except KeyError :
                print(f"Variable {var_name} does not exist.")
                error = True
                break
        elif "clearvar" in userin :             
            if userin == "clearvar" :
                variables = {}
            else :
                var_name = userin.removeprefix("clearvar ")
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
        elif "printc" in userin :
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
        elif "deltxt" in userin :
            filename = userin.removeprefix("deltxt ")
            if ".txt" not in userin :
                filename += ".txt"
            filepath = path.join(work_dir,filename)
            if path.exists(filepath) :
                remove(filepath)
                print(f"{filepath} deleted.")
            else :
                print(f"{filepath} does not exist.")
                error = True
        elif userin == "cwd" :
            print(work_dir)
        elif "log" in userin :
            argument = userin.removeprefix("log ")
            if argument == "view" :
                print("Commands log :")
                for i in range(0,len(log)) :
                    print(f"{i+1} {log[i]}")
            elif argument == "export" :
                filepath = path.join(work_dir,"log.txt")
                with open(filepath,"w") as file_log :
                    for i in range(0,len(log)) :
                        file_log.write(f"{i+1} {log[i]}\n")
                    file_log.close()
            else :
                print("Invaild argument.")
                error = True
        elif userin == "credit" :
            print("pCLI relies on the work of 1 person :")
            print("Lead Developer : Andrew1013")
            print()
            print("and these open-source dependencies and programs :")
            print("Program : Python 3.10.x -> Python 3.11.x")
            print("Dependencies : termcolor, psutil, timeit, built-in dependencies in Python")
            print("IDE : Visual Studio Code")
        elif userin == "help" :
            print("ver : print version of pCLI")
            print("credit : showing credits")
            print("help : show command pallete")
            print("cwd : print current directory CLI is in")
            print("time : display current day and time")
            print("exit : exit cli")
            print("log [view / export]: show log of commands executed / export log to log.txt")
            input("[Press Enter to continue]\n")
            print("printstr [string] : print string ")
            print("printvar [variable name] : print variable value (if no variable name is specified, printvar will print all variables available)")
            print("definevar [variable type] [varianle type] [variable value] : define a varaible with value of selected type")
            print("assignvar [variable name] [variable type] [new variable value] : assign a given variable a new value of selected type")
            print("clearvar [variable name] : clear variable's value (reset value to blank)")
            input("[Press Enter to continue]\n")
            print("readtxt [file_name] : read text files and displaying the contents (line-by-line for now)")
            print("writetxt [file_name] [string]: write a string to text, will create file if file does not exist")
            print("deltxt [file_name] : delete a text file")
            input("[Press Enter to continue]\n")
            print("clear : clear terminal screen")
        elif userin == "clear" :
            if name == "nt" :
                os_sys("cls")
            else :
                os_sys("clear")
        else :
            print("Error : Invaild command")
            error = True
        if error == False :
            log.append(userin)
        print() #print empty line
    except KeyboardInterrupt :
        print("\nExiting from Ctrl-C trigger...")
        break