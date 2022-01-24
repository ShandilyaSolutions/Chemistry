import os
from chemspipy import ChemSpider
import json

api_key = os.environ['KEY']

cs = ChemSpider(api_key)

#class chemspipy.objects.Compound

def fromChemSpiderID(ChemSpiID):
  data = cs.get_compound(ChemSpiID)
  return data

def fromNameOfChemical(name):
  data = cs.search(name)
  return data

def getDataFromID(chem_data):
  final_data = {}
  final_data ["Common Name "] = chem_data.common_name
  final_data ["IUPAC Name "] = None
  final_data ["Molecular Formula "] = chem_data.molecular_formula
  final_data ["Molecular Weight "] = chem_data.molecular_weight
  final_data ["Chem Spider ID "] = chem_data.record_id
  #final_data["Image"] = chem_data.image
  # final_data ["SMILE Structure"] = cs.get_details(chem_data.record_id)['smiles']
  final_data ["SMILE Structure"] = chem_data.smiles
  final_data ["Image URL"] = chem_data.image_url
  return json.dumps(final_data)
 
def findDesiredCompound(chem_data):
    for i in range(1, len(chem_data)+1):
        print(i, ":", chem_data[i-1].common_name)
    x = int(input("Enter the index of compund: "))
    return chem_data[x-1]

# def nametoID(compound_object):                                                   #COMPLETE THIS TO COMPLETE THE CODE
#   return compound_object.record_id

# def tester(data):
#   dic = findDesiredCompound(data)
#   keys = dic.values()
#   for i in keys:
#     result = list(cs.search(i))
#     print(i," : ",len(result))
#   return None




print("""Available Choices  :
1. - Use ChemSpider ID
2. - Use Compound's Name""")
ch = int(input("Enter your choice here  : "))

if (ch==1):
  ChemSpiID = int(input("Enter the Chem Spider ID of the compound you are looking for :  "))
  chem_data = fromChemSpiderID(ChemSpiID)
  output = getDataFromID(chem_data)
elif (ch==2):
  name = input("Enter the name of the chemical compund here :  ")
  chem_data = fromNameOfChemical(name)
  chem_data = list(chem_data)
  # tester(chem_data)
  l = len(chem_data)
  if (l == 1):
    comp_obj = chem_data[0]
  else:
    comp_obj = findDesiredCompound(chem_data)

  output = getDataFromID(comp_obj)

print (output)
