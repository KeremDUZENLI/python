from fileCheck import *
from fileCompare import *
from listConvert import *


# PATH
mypath1 = input("First  Path:   ")
mypath2 = input("Second Path:   ")

# DATABASE
dataBase1 = []
dataBase2 = []

# BASIC LIST
basicList1 = []
basicList2 = []

# ---------------------------------------------------------------

# FILECHECK
FileCheck(mypath1, dataBase1)
FileCheck(mypath2, dataBase2)

# LISTCONVERTER
ListConvert(dataBase1, basicList1)
ListConvert(dataBase2, basicList2)

# FINAL
FileCompare(basicList1, basicList2)
