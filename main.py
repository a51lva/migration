import pandas as pd
import numpy as np

refNumberArray = ['250702', '250949']

rulesDataArray = []
migrationDataArray = []

workDataArray = []
migrationWorkDataArray = []

def loadCSVFile(filepath):
        data = []
        encodings = [None, 'utf-8', 'ISO-8859-1']  # None is default
        for encoding in encodings:
                try:
                        data = pd.read_csv(filepath, encoding=encoding, sep=';', header=None)
                except Exception:  # should really be more specific 
                        pass
        return (np.array(data))

def createResult(workDataArrayP, migrationWorkDataArrayP):
        if((len(workDataArrayP)) == (len(migrationWorkDataArrayP))):
                with open("result.csv","w") as output:
                    count = 0
                    for item in migrationWorkDataArrayP:
                            workItem = workDataArrayP[count]
                            output.write("\n" + str(item[1]) + ";" + str(item[2]) + ";" + str(item[3]) + ";" + str(item[4]) + ";" + str(workItem[1]) + ";" + str(item[5]) + ";" + str(item[6]) + ";" + str(item[7]) + ";" + str(item[8]) + ";" + str(workItem[3]) + ";" + str(workItem[4]) + ";" + str(item[11]) + ";"+ str(item[12]))
                            count +=  1
                return True
        else:
                return False

def createWorkArray(refNumber, dataArray, indexRefNumberComparisom = 0):
        workArray = []
        
        for item in dataArray:
            itemRefNumber = str(item[indexRefNumberComparisom])
            if((itemRefNumber.find(refNumber, 0, len(itemRefNumber)) != -1) and (str(item[2]) != 'Not Migrate')):
                    workArray.append(item)
        
        return workArray

def processListOfRefNumber(refNumberArray, migrationDataArray, rulesDataArray):
        for refItem in refNumberArray:
           migrationWorkDataArray = createWorkArray(refItem, migrationDataArray, 1)
           workDataArray = createWorkArray(refItem, rulesDataArray)
           
           if(len(migrationWorkDataArray) > 0):
                if(createResult(workDataArray , migrationWorkDataArray)):
                    print(refItem + ' OK')
                else:
                    print(refItem + ' KO - The number are different')
           else:
                   print(refItem + ' KO - Cant find on migrated document')

def main():
    print('hello python')
    
    migrationDataArray = loadCSVFile('migrated_document.csv')
    rulesDataArray = loadCSVFile('TA_rules_DEF.csv')
      
    print(len(rulesDataArray))    
    print(len(migrationDataArray))

    processListOfRefNumber(refNumberArray , migrationDataArray , rulesDataArray)


if __name__ == "__main__":
    main()