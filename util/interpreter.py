import os
import sys

def runFile(arg):
    s = []
    path = os.getcwd()+"\\"
    for i in arg:
        filePath=path+str(i)
        try:
            locFile=open(filePath)
            s.append(locFile.read(-1))
            locFile.close()
        except Exception:
            print("ERROR!!!")
            print(f"File '{i}' does not found on the path '{path}'")
            sys.exit()
    return s
