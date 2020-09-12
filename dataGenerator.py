import mendeleev
#chemical format should look like this compoundName:grams:amu
#tinkering variables
imprecisionAllowed = 0.1

#user input
x = vars(mendeleev)
file = open("amu_data.txt", "w+")
try:
	for atom in x:
		if(len(atom)<3):
			sym = str(atom)
			atom = x[atom]
			amu = atom.atomic_weight
			name = atom.name
			file.write(sym+":"+name+":"+str(amu)+"\n")
except Exception as e:
	print(e)
file.close()

		