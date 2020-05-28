import os
import lexer
import parser


def runFile():

    files=os.listdir(os.getcwd()+"/test_cases")
    s=[]
    for fil in files:
        # string=str(os.getcwd()+"/test_cases/")+str(fil)
        try:
            filePath=os.getcwd()+"/test_cases/"+str(fil)
            # print (filePath)
            locFile=open(filePath)
            s.append(locFile.read(-1))
            locFile.close()
        except:
            pass
    return s

