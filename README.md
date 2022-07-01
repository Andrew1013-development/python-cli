# python-cli
Bare-bones Command Line Interface (CLI) written in Python

## Commmand Pallete
```
# command pallete
# ver : print version
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
# credit : showing credits (will be available on the first Release Candidate (rc) build or the final / third Beta (b) build)
# help : show command pallete
```

## Versioning System
v{major}.{minor}.{revision}{branch}{build}-{compiled_date}
example : v0.0.0a1-0511
note : 
- [date] format : month-day (wil be changed into year-month-day before 2023)

## Latest version (of each branches)
- Release : v0.0.0p1-0701
- Release Candidate : v0.0.0rc2-0629
- Beta : v0.0.0b4-0619
- Alpha : v0.0.0a10-0613

## Versions about to be deprecated (of each branches)
- Release : N/A
- Release Candidate : N/A
- Beta : N/A
- Alpha : v0.0.0a1-0511 (date of deprecation : 11/8/2022)
