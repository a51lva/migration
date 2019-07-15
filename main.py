from model import migrationModel
import python_minifier

def main():
    print('hello python')
    
    refNumberArray = ['263625','263628','263629','263632','263633','263634','263637']
    
    mm = migrationModel()
    rulesDataArray = []
    migrationDataArray = []


    migrationDataArray = mm.loadCSVFile("data/csv/migrated_document.csv")
    rulesDataArray = mm.loadCSVFile('data/csv/lOTE_PRO_2.csv')
      
    print('Ta Rules Def size: ' + str(len(rulesDataArray)) )   
    print('Migrated Document size: ' + str(len(migrationDataArray)))

    mm.processListOfRefNumber(refNumberArray , migrationDataArray , rulesDataArray)

if __name__ == "__main__":
    with open('model.py') as f:
        print(python_minifier.minify(f.read()))