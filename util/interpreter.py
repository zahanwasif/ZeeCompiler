import os
import lexer
import parser

def runFile(arg):
    filePath=os.getcwd()+"\\"+str(arg)
    print(filePath)
    s = []
    try:
        locFile=open(filePath)
        s.append(locFile.read(-1))
        locFile.close()
    except:
        pass
    return s
