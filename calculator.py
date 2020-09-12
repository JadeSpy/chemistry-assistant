#User input
input_data = '''
pt:34.48
n:15.19
c:17.38
h:2.65
'''
#Tweaking
allowedUncertainty = 0.2 #The allowed difference between each number generated and the closest integer to it required for the answer to be validated.
outputAsRounded = False #Want nice clean numbers?





#Load DATA
names = []
symbols = []
humanReadableSymbols = []
masses = []
with open("amu_data.txt") as f:
	line = f.readline()
	while line:
		contents = line.split(":")
		symbols.append(contents[0].lower())
		humanReadableSymbols.append(contents[0])
		names.append(contents[1].lower())
		masses.append(float(contents[2]))
		line = f.readline()
converted_data_symbols = []
converted_data_amounts = []
converted_data_masses = []
input_data = input_data.split("\n")
for line in input_data:
	if(line==""):
		continue
	line = line.lower()
	lineData = line.split(":")
	identifier = lineData[0]
	if(identifier in names):
		index = names.index(identifier)
		identifier = symbols[index]
	else:
		if(not identifier in symbols):
			print("Couldn't find an atom with the identifier:", identifier)
			exit()
	converted_data_symbols.append(identifier)
	index = symbols.index(identifier)
	converted_data_masses.append(masses[index])
	try:
		converted_data_amounts.append(float(lineData[1]))
	except:
		print("One of the weights you entered wasn't a number.")
		exit()
smallestMole = 192459081259128
for i in range(len(converted_data_amounts)):
	amount = converted_data_amounts[i]
	moles = amount/converted_data_masses[i]
	converted_data_amounts[i]=moles
	if(moles<smallestMole):
		smallestMole = moles
#FINDING FORMUMLA
ratio = 1/smallestMole
import math
for i in range(1,100000):
	potentialFormula = []
	for moles in converted_data_amounts:
		potentialFormula.append(ratio*moles*i)
	valid = True
	for atoms in potentialFormula:
		decimal = atoms-math.floor(atoms)
		if(decimal>allowedUncertainty and decimal < 1-allowedUncertainty):
			valid = False
	if(valid==True):
		outputEquation = ""
		for i in range(len(converted_data_symbols)):
			if(outputAsRounded):
				if(outputEquation==""):
					outputEquation+=humanReadableSymbols[symbols.index(converted_data_symbols[i])]+str(round(potentialFormula[i]))
				else:
					outputEquation+=" + "+humanReadableSymbols[symbols.index(converted_data_symbols[i])]+str(round(potentialFormula[i]))
			else:
				if(outputEquation==""):
					outputEquation+=humanReadableSymbols[symbols.index(converted_data_symbols[i])]+str(potentialFormula[i])
				else:
					outputEquation+=" + "+humanReadableSymbols[symbols.index(converted_data_symbols[i])]+str(potentialFormula[i])

		break
print(outputEquation)




