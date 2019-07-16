import pandas as pd
import numpy as np

class migrationModel:
    
    def loadCSVFile(self, filepath):
        data = []
        encodings = [None, 'utf-8', 'ISO-8859-1']  # None is default
        for encoding in encodings:
                try:
                        data = pd.read_csv(filepath, encoding=encoding, sep=';', header=None)
                except Exception:  # should really be more specific 
                        pass
        return (np.array(data))

    def createResult(self, workDataArrayP, migrationWorkDataArrayP):
            result = ''
            if((len(workDataArrayP)) == (len(migrationWorkDataArrayP))):
                    count = 0
                    for item in migrationWorkDataArrayP:
                            workItem = workDataArrayP[count]          

                            if( workItem[2] == item[5]):
                                    result = result + '\n' + ( str(workItem[0]).replace('nan','') + ";" + str(workItem[1]).replace('nan','') + ";" + str(workItem[2]).replace('nan','') + ";" + str(workItem[3]).replace('nan','') + ";" + str(workItem[4]).replace('nan','') + ";" + str(workItem[5]).replace('nan','') + ";" + str(workItem[6]).replace('nan','') + ";" + str(item[0]).replace('nan','') + ";" + str(item[1]).replace('nan','') + ";" + str(item[2]).replace('nan','') + ";" + str(item[3]).replace('nan','') + ";" + str(item[4]).replace('nan','') + ";"+ str(item[5]).replace('nan','') + ";"+ str(item[6]).replace('nan','') + ";"+ str(item[7]).replace('nan','') + ";"+ str(item[8]).replace('nan','') + ";"+ str(item[9]).replace('nan','') + ";"+ str(item[10]).replace('nan','') + ";"+ str(item[11]).replace('nan','') + ";"+ str(item[12]).replace('nan',''))
                            else:
                                    result = 'names are different'
                                    break
                            count +=  1
            return result

    def createWorkArray(self, refNumber, dataArray, indexRefNumberComparisom = 0):
            workArray = []
            
            for item in dataArray:
                itemRefNumber = str(item[indexRefNumberComparisom])
                if((itemRefNumber.find(refNumber, 0, len(itemRefNumber)) != -1) and (str(item[2]) != 'Not Migrate')):
                        workArray.append(item)
            
            return workArray

    def processListOfRefNumber(self, refNumberArray, migrationDataArray, rulesDataArray):
            with open("result/result.csv","w", encoding="utf-8") as output:
                    for refItem in refNumberArray:
                            migrationWorkDataArray = self.createWorkArray( refItem, migrationDataArray, 1 )
                            workDataArray = self.createWorkArray( refItem, rulesDataArray )
                            
                            if( len( migrationWorkDataArray ) > 0):
                                    result = self.createResult(workDataArray , migrationWorkDataArray)
                                    if( result != ''):
                                            if(result != 'names are different'):
                                                    output.write( result )
                                                    print(refItem + ' OK')
                                            else:
                                                print(refItem + ' - > KO - names are different')
                                    else:
                                            print(refItem + ' - > KO - the numbers are different')
                            else:
                                    print(refItem + ' - > KO - cant find on migrated document')