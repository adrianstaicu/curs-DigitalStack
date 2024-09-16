#dictionar = {} asa se defineste, are key-valoare

dictionar = {1:"Ana", "2": 'Mere', "3":'pere', 4:"prune", 1:"Antonia"}
#print(type(dictionar))
#print(dictionar)
#print(dictionar["2"])
#print(dictionar["22"])
#print(dictionar.get("22", "Nu gaste nimic"))
#dictionar["22"]="valoare nou" #adaugare valoare

dictionar.update({"22":"Valoare noua", "33":'Alta valoare'})

print(dictionar)
print(dictionar.keys()) # vedem toate keyle
print(dictionar.values()) # vedem toate valorile cheilor
print(dictionar.items())