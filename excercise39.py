counties = {
            'nairobi' :"NRB" ,
            'Thika':"Tka" ,
            'Githurai':"GRI" ,
            'Kakamega':"KKGA",
            'Webuye':"WBE",
            'Kisumu':"KSM"
             }

#adding towns to the different counties we have
towns ={
        'NRB':"Westlands",
        'Tka':"Gatundu",
        'GRI':"Kimbo",
        'KSM':"Lwangni"
        }

#adding more towns
towns['NRB'] = 'Kibera'
towns['Tka'] = 'Ruiru'
towns['KKGA'] = 'Miciku'
towns['WBE'] = 'kalaye'

#printing out some counties
print('-' * 10)
print("Nairobi has: " , towns["NRB"])
print("Thika has: " , towns["Tka"])

#printing again
print("Nairobi's abbrevation is" , counties['nairobi'])
print("Thika's abbreviation is" ,counties['Thika'])

print("-" *10)
print("Nairobi has:" , towns[counties['nairobi']] )
print("Thika has:"  , towns[counties['Thika']] )

print("-" * 10)
new_dic = {} #created an empty dict to be able to use the counties dict twice?
new_dic = counties.copy()
for county, abbrev in new_dic.items():
    print("%s is abbreviated %s" %(county , abbrev))

#print every town in counties
print("-" * 10)
for abbreviation , town in towns.items():
    print("%s has the town %s" %(abbreviation , town))


#both at the same time
print("-" * 10)
for counties , abbreviation in counties.items():
    print("%r county is abbreviated %r and has towns %r" %(counties , abbreviation
    , towns[abbreviation]))

#created an empty dict to be able to use the counties dict for the third time why?
second_dict = {}
second_dict = new_dic.copy()

print("-" * 10)
county = second_dict.get('Macha' )

if  not county:
    print("sorry there is no Macha")

town = towns.get("Mch" , "Doesnt Exist")
print("the town for the county 'Mch' is: %s" %town)
