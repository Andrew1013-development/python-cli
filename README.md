# python-cli
Command Line Interface (CLI) written in Python

## Commmand Pallete
```
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
```

## Versioning System
- versioning scheme (as of now) : v{major}.{minor}.{revision}{branch}{build}-{compiled_date}(-{note})
  - {compiled_date} format : month-day (wil be changed into year-month-day before 2023)
  - branch meanings :
    - a : Alpha
    - b : Beta
    - rc : Release Candidate
    - p (or no branch indicator) : Release
    - m : Miscellaneous (v0.0.0)
  - note : "-{note}" part is only for Miscellaneous builds
  
## Latest version (of each branches)
- Release : v0.0.0p3-0703
- Release Candidate : v0.0.0rc2-0629
- Beta : v0.0.0b4-0619
- Alpha : v0.0.0a10-0613
- Miscellaneous : v0.0.0m1-0608-wyanh_14

## Versions about to be deprecated (of each branches)
- Release : N/A
- Release Candidate : N/A
- Beta : N/A
- Alpha : v0.0.0a1-0511 (timeframe of deprecation : 5 to 10 months)
- Miscellaneous : v0.0.0m1-0608-wyanh_14 (timeframe of deprecation : 3 to 6 months)
