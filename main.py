# dependencies
from datetime import date
# command pallete
# ver : print version
# print [string] : print string
# exit : exit cli

#version shits
major = 0
minor = 0
rev = 0
branch = "a"
build = 1
flag = "CONCEPTION"
compiled_date = date(2022,5,11)
version_string = f"{major}.{minor}.{rev}{branch}{build}"

#main code
userin = ""
while userin != "exit" :
    userin = input()
    if userin == "ver" :
        print(f"Python CLI version {version_string}")
        print(f"Compiled on {compiled_date}")
        if flag != "" :
            print(f"Flags for program : {flag}")
    elif userin == "exit" :
        break
    elif "print" in userin :
        print([s for s in userin.split(" ")][1])
    else :
        print("Error : Invaild command")
    print() #print empty line