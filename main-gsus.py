# dependencies
from http.client import responses
import pip
from os import path
from os import remove
from os import system as os_sys
from os import name
from os import remove
import sys
import gc
import pdb
import requests #module needs to be installed
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
from PIL import ImageTk, Image
import tkinter #module needs to be installed
import cv2 #module needs to be installed

# command pallete
# ver : print version
# usrver : print version of pCLI's User mode (does include within the original ver command)
# printstr [string] : print string 
# printvar [variable name] : print variable value (if no variable name is specified, printvar will print all variables available)
# definevar [variable type] [varianle type] [variable value] : define a varaible with value of selected type
# assignvar [variable name] [variable type] [new variable value] : assign a given variable a new value of selected type
# clearvar [variable name] : clear variable's value (reset value to blank)
# exit : exit cli
# time : display current day and time
# log (view / export / clear): show log of commands executed / export log to log.txt / clear log
# readtxt [file_name] : read text files and displaying the contents (line-by-line for now)
# writetxt [file_name] [string]: write a string to text, will create file if file does not exist 
# deltxt [file_name] : delete a text file
# cwd : print current directory CLI is in
# mode : show what mode pCLI is in
# credit : showing credits
# help : show command pallete
# system : enables the execution of system commands
# sysver : print version of pCLI's System mode (does include within the original ver command)
# exitsys : exit system mode, terminating system commands execution
# hbdaygsus : download 3 pictures of gsus then automatically open them (with timeout of 3 seconds per item)

# variable types
# integer, float : numbers
# string (default type)
# boolean : True / False
# auto : dynamically determined

#pCLI version thingies
major = 0
minor = 0
rev = 0
branch = "m"
build = 3
flag = f"M{build}"
flag_desc = f"MISC {build}"
base_version = "v0.0.0p3-0703"
note = "gsus"
compiled_date = date(2022,7,12).strftime("%d/%m/%Y")
compile_tag = "0712"
version_string = f"v{major}.{minor}.{rev}{branch}{build}-{compile_tag}-{note}"
python_version = f"{python_implementation()} {python_version()}"
python_compiler = python_compiler()
os_release = pt_sys() + " " + release()
os_version = platform().replace("-"," ",2)

#User mode version thingies
usr_major = 1
usr_minor = 1
usr_version_string = f"v{usr_major}.{usr_minor}"
usr_compiled_date = date(2022,7,3).strftime("%d/%m/%Y")
usr_level = 2

#System mode version thingies
sys_major = 1
sys_minor = 1
sys_version_string = f"v{sys_major}.{sys_minor}"
sys_compiled_date = date(2022,7,3).strftime("%d/%m/%Y")
sys_level = 2

#variables
pre_userin = ""
userin = ""
systemin = ""
variables = {}
log = []
error = False
system_commands = False
user_commands = True
work_dir = path.dirname(path.realpath(__file__))
first_start = True

#functions

#main code
while userin != "exit" :
    if system_commands == False :
        if first_start == True :
            if name == "nt" :
                os_sys("cls")
            else :
                os_sys("clear")
            print("You are in User mode. System mode is available with 'system' command.")
            first_start = False
        else :
            pass
        try :
            userin = input("> ")
            if userin == "ver" :
                print(f"Python CLI version {version_string}, based on {base_version}")
                print(f"User mode version {usr_version_string}, System mode version {sys_version_string}")
                print(f"Compiled on {compiled_date} with compilation tag {compile_tag}")
                if flag != "" :
                    print(f"Flags for program : {flag} ({flag_desc}) / {note}")
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
            elif userin == "usrver" :
                print(f"Python CLI User mode version {usr_version_string}, level {usr_level}")
                print(f"Compiled on {sys_compiled_date}")
                print(f"Running on {python_version} [{python_compiler}]")
            elif userin == "exit" :
                print("Exiting...")
                gc.collect()
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
                            if type(variables[key]).__name__ == "int" :
                                var_type = "integer"
                            elif type(variables[key]).__name__ == "str" :
                                var_type = "string"
                            elif type(variables[key]).__name__ == "bool" :
                                var_type = "boolean"
                            else :
                                var_type = type(variables[key]).__name__
                            print(f"{key} <- {variables[key]} (type : {var_type}    )")
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
                if userin == "log" :
                    argument = "view"
                else :
                    argument = userin.removeprefix("log ")
                if argument == "view" :
                    if log == [] :
                        print("Log is empty.")
                    else :
                        print("Commands log :")
                        for i in range(0,len(log)) :
                            print(f"{i+1} {log[i]}")
                            if i / 6 >= 1:
                                input("[Press Enter to continue]\n")
                elif argument == "export" :
                    filepath = path.join(work_dir,"log.txt")
                    with open(filepath,"w") as file_log :
                        for i in range(0,len(log)) :
                            file_log.write(f"{i+1} {log[i]}\n")
                        file_log.close()
                elif argument == "log" :
                    log = []
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
                print("ver : print version of pCLI's User mode")
                print("credit : showing credits")
                print("help : show command pallete")
                print("cwd : print current directory CLI is in")
                print("time : display current day and time")
                print("exit : exit cli")
                print("mode : show what mode pCLI is in")
                print("log [view / export / clear]: show log of commands executed / export log to log.txt / clear log")
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
                print("download : download main-wyanh_14.py (pCLI version v0.0.0m1-0608-wyanh_14) into the working directory")
                print("Note : 'download' won't be supported until the update mechanism is implemented, use it at your own risk.")
                input("[Press Enter to continue]\n")
                print("system : enables the execution of system commands using System mode")
                print("Note : pCLI commands, including log, will not be executed in system mode.")
                print("exitsys : exit system mode, terminating system commands execution.")
                print("sysver : print version of pCLI's System mode")
                print("usrver : print version of pCLI's User mode")
                input("[Press Enter to continue]\n")
                print("hbdaygsus : download 3 pictures of gsus then automatically open them (with timeout of 3 seconds per picture)")
            elif userin == "clear" :
                if name == "nt" :
                    os_sys("cls")
                else :
                    os_sys("clear")
            elif userin == "download" :
                filepath = path.join(work_dir,"main-wyanh_14.py")
                url = "https://raw.githubusercontent.com/Andrew1013-development/python-cli/misc/main-wyanh_14.py"
                response = requests.get(url, stream=True)
                size = int(response.headers.get('content-length', 0))
                print("This is for testing purposes only, this command will not be documented.")
                print(f"Downloading pCLI version v0.0.0m1-0608-wyanh_14....")
                with open(filepath, 'wb') as file:
                    for data in response.iter_content(1024):
                        file.write(data)
                print("Download complete.")
            elif userin == "system" :
                system_commands = True
                print("Preparing to enter System mode....")
                print("Clearing User mode data....")
                pre_userin = ""
                userin = ""
                systemin = ""
                variables = {}
                log = []
                sleep(0.5)
                print("Entering System mode....")
                sleep(0.1)
            elif userin == "mode" :
                print("Current mode : User mode")
            elif userin == "hbdaygsus" :
                image_urls = [
                    "https://lh3.googleusercontent.com/dfx8gxaTVKzMvd_vi7XnlqBoLxDJj45MuWtIL7vG_B3LkpuSQeuLfayBuD8-B7coLatJ6rrUvGJJJZYc0_UZ6WzL2P7fpEgXoPgYeZpHJrI4S2WqiWS6z6mJObsppR9nzFSlkHeU1Unhfntoo080Uo6gjdRTHSsgUNvC2vVQqjqBbfxYlyWuffg6mn9pbBwc8IPAqlVu7J6y2QI4q4Bubj-BNgnJQNVYze_bILonlNC_WcB07t25mMkH_e61F52BYVaMdQ3f82nKW7EVfsRtdSYkedMYbEqQaucSpV2nVPXWpNWj6wL8eqyzN0_woO8JsY8OydYFi6-0ac4gy18nc4dYUEs36CsLNcoC9UAnpjZ48fykwerC-oPsjTA8m2M4Gl5nPuTFxowqMN8ljJpvh4MsFTjxQIkrVkW46WkxbeQONberchRzwPN1i5IdCPtdTVzcE-KUTA1bEpM2iWPXHJ5pdRqW3V2Cm5RVyNoxkRsVDxaHY8VOI4pt7YXQyjvMboVDtgDYWD5Xeabfo3oDnOBBN6hmvh_4GuItcXV8JzTmpGwKYUWWPNqwX_MtuT2KNvNXJxai-deLYgnOk06t_AZp0QsnU5id9_eqoBhMyLe38X63g0aHN9C0h98lelO8kAO9TSGKwM4giaJvLuVakzfxF1Ex5zMEdoNRlZlzJ9dDMoRCsT_155sIL5IjMtDJ_qZeimHthu2W5791mkkwJuwWIBlnx1iPFGNLwzeAKtgko-6Lv6PNFrxV6Gx-2yG_-jzt6wY4e4MhZPRhzYlCfMfUaa-IXBrCw6-GrQM4D8ln5yDGiM-RowV8hA6gLGNANO5FNZI=w1198-h898-no?authuser=0",
                    "https://lh3.googleusercontent.com/QzRHFk3XY4T4MUXoOLTCdMTMhrpkj89eEeLoKbf7_PfkMbjgxY1eI96cSpGLcsXMyJRgmIqAffJo_KLz0OhpkAxYGsh4oxF2v1nIRcb1Ln0Ok7Dwtui01MY2j2wvNEuRN39B_1QFTCOZZpBxhldR-PkFeyzHBkyePRIP9SEx1WXyPvTUQXRvZvLazgMP9hMCGOUnegLuxNmIRu1qoLiXpnLDwnlwNVMJ9YPM7d2b8vR4cGA-d9J401_cct3X3CgPWC9d5aM71ir0F3oX8sfFYCo5VpL6N1Ekhs9gif7knbzC60xm-fwiqhsIQ4qWZ7yAHG0TOoEWU73VDjR-qhYlb92CIkHxf9ci3Y8g157JHcpMOy4LRqJztSjz4DJCwt3hDjkvVyJ2_8b6FgfdOL_3eIaahkPvObL7H2lNGMK9NJHV_UlQ4IuWPo6yVDoUusTmqmFNbOo5sRhFdbc7jT-6aVpeCCpsYsjYPO5qZRNzbBBpJrb5g791OnqXYczUU07pulTyZKYgQ1IwFJ82igfnw-rw6elQEUSqhtsOcOfuSU-hf1OqKOU_8ScCnn3yC5LnPj3h_k4UsQGrCVTy0tO5lLUlV4fajHAccvW-a3f8FXSo-vJ74_gEAqMtMRpetVUMYh0PwDiZ4rFdHCOm-sP4Yf_i_ZtPTjdeDuZ3sfhn0D0lbZOzvci7NQ57V3wwg-syb7lcygP2jAq6NUQ4f1fUogwdmkyrg5-tPOt0N6sXOrlctux_pyujDvkIbKkAgm-VpBcGJvNZADeLpwgEMIL7QqyR0MwOmjvj3toIXJ-qGxoE6EpObyqN6mZtDU_fdskmmLZ1xBo=w1470-h828-no?authuser=0",
                    "https://lh3.googleusercontent.com/pOsBjhATiJb034CPF_MoepJB59d5lt_mgX7R0EIeNZht6n-CX9XI8L6OhMlDBoYnGtua_buUG9_oMeKJQjLqHorayNwJm06KmlcMVwgADYsqLojsynjyU3nBhWC_qhJZ3meVRsfIm8rFRNedDTnoDz5ONP_lSMrJzZzE8bJleb2BmeC05yHsNLpQ0T0E8yPeVynIBgjKDDCZMoIiBMvZPqvaVUs0HbsUFoFZm5gE2olHAx-AtGBZtpLOjmPT08Ytupho0FO2c8_XLRYgbKtDMFZydRYDo_uJ3EPMqREbgIb89877fOCW0B7sexnzkK23zwNLjcKrylCRigA-6EHDeoNnLwwehkqElRHSniVVYxtg34AwYpBDuxli9E1lFjfEm2JrU1sQl84MIakslMbfl703O2sGQkziYC5punoKvcwmCgR7qomricGYo_Zn5LCv_-lTGp6GxAJtKOiJiDC1lNpXb7Em3MXpnc-xI-fCx9TWcrwCBgPhMuER9TBRqj3OS5pl9r8UaaMT8LfCo3skXvZb8h2FQN18KyClSa9_CvREpTDMEYDEQvRDIAafToecIvgeq02HexlFHPJOm2dAQ6232Sz2jtMvol2aP-tpCkyF4y6Ohl1TSN80KS3oZpPOP_ODyD7mVMEGiqX0GRTxIqbYQpWbVcusrp2NI7EsADuNjB4Q8xHFKR2Nst6syyu3JYSYx5JqkUqlQbld6FXKw9ViSeEdfbJUXDGuqFjfmAiYY8njK99lUyI51jE1u7gG983fJc874bFR8z48dFY_ojC-zYy0Qp7fL6pdq4CPOQxo379fgHXDPKrZNaG_iLE1jehY42s=w1470-h828-no?authuser=0"
                ]
                print("Preparing to download photos...")
                sleep(0.5)         
                #photos
                count = 1
                for url in image_urls : 
                    #download code
                    response = requests.get(url,stream=True)
                    filepath = path.join(work_dir,f"gsus{count}.jpg")
                    with open(filepath,"wb") as gsus_pic :
                        print(f"Downloading picture {count}")
                        for block in response.iter_content(1024) :
                            if not block :
                                break
                            gsus_pic.write(block)
                    count += 1 
                    #window code
                    window = tkinter.Tk()
                    screen_width = window.winfo_screenwidth()
                    screen_height = window.winfo_screenheight()
                    frame = tkinter.Frame(window,width=screen_height,height=screen_width)
                    frame.pack()
                    frame.place(anchor='center',relx=0.5,rely=0.5)
                    image = ImageTk.PhotoImage(Image.open(filepath))
                    label = tkinter.Label(frame,image=image)
                    label.pack()
                    window.attributes('-topmost',1) #on top of all other windows
                    window.state("zoomed") #fullscreen
                    window.after(3000,window.destroy) #destroy window after 3 seconds
                    window.mainloop()
                    remove(filepath)
                print("Downloading pictures complete.")
                print("Command execution finished.")    
            else :
                print("Error : Invaild command")
                error = True
            if error == False :
                log.append(userin)
            print() #print empty line
        except KeyboardInterrupt :
            print("\nExiting from Ctrl-C trigger...")
            gc.collect()
            break
    else :
        if name == "nt" :
            os_sys("cls")
        else :
            os_sys("clear")
        print("You are in System mode, all pCLI commands will be disabled")
        print("Type 'exitsys' to exit System mode")
        
        #variables
        pre_systemin = ""
        systemin = "" 
        
        #main code
        while systemin != "exitsys" :
            systemin = input("> ")
            if systemin == "sysver" :
                print(f"Python CLI System mode version {sys_version_string}, level {sys_level}")
                print(f"Compiled on {sys_compiled_date}")
                print(f"Running on {python_version} [{python_compiler}]")
            elif systemin == "exitsys" :
                print("Exiting system mode...")
                print("Clearing System mode data...")
                system_commands = False
                first_start = True
                systemin = ""
                gc.collect()
                sleep(0.5)
                print("Entering User mode....")
                sleep(0.1)
                print()
                break
            elif systemin == "mode" :
                print("Current mode : System mode")
            else :            
                os_sys(systemin)
            print()