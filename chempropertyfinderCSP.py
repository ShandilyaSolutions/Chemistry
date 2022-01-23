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
  final_data ["Chem Spider ID "] = ChemSpiID
  #final_data["Image"] = chem_data.image
  final_data ["SMILE Structure"] = cs.get_details(ChemSpiID)['smiles']
  final_data ["Image URL"] = chem_data.image_url
  return json.dumps(final_data)
 
def findDesiredCompound(chem_data):
  output={}
  c=0
  for i in chem_data:
    output[c]=i.common_name
    c+=1
  output['no_of_results'] = c
  print("Found ",output["no_of_results"]," matches :")
  for j in range (0,output["no_of_results"],1):
    print (j," : ",output[j])
  print("Please select your choice by typing the no corresponding to the compound name")
  #ch=int(input("Here  : "))
  return output#[ch]

def nametoID(name):                                                   #COMPLETE THIS TO COMPLETE THE CODE
  # #It takes a name and returns its ChemSpiID
  # lst=list(cs.search(name))
  # common_names=[]
  # i=0
  # for item in lst:

  return name.

def tester(data):
  dic = findDesiredCompound(data)
  keys = dic.values()
  for i in keys:
    result = list(cs.search(i))
    print(i," : ",len(result))
  return None




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
  tester(chem_data)
#   l = len(chem_data)
#   if (l == 1):
#     CSid = nametoId(chem_data.common_name)
#   else:
#     search = findDesiredCompound(chem_data)
#     CSid = nametoID(search)

#   output = getDataFromID(CSid)

# print (output)
