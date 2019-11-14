import DNADict
inputCode = str(input("Input Sequence \n"))
canCalculateBool = False
RNACode = []
proteinCode = []
def canCalculate(code):
    global canCalculateBool
    if len(code) % 3 != 0:
        print("Sequence cannot be calculated")
        canCalculateBool = False
    else:
        print("Sequence can be calculated")
        canCalculateBool = True

def checkStart(code):
    if "TAC" in code or "tac" in code or "AUG" in code or "aur" in code:
        print("Has Start")
    else:
        print("No Start Codon")
    
def translateRNA(code):
    global RNACode
    for x in range(0, len(code)):
        if code[x] == "A" or code[x] == "a":
            RNACode.append("U")
        elif code[x] == "T" or code[x] == "t":
            RNACode.append("A")
        elif code[x] == "C" or code[x] == "c":
            RNACode.append("G")
        elif code[x] == "G" or code[x] == "g":
            RNACode.append("C")
    return RNACode
            
def transcriptionProtein():
	global RNACode
	global proteinCode
	for j in range(0, len(RNACode)):
		temp = ""
		if j%3 == 0:
			for k in range(0,3):
				temp = temp + RNACode[j+k]
			print(DNADict.codonDict[temp], end = " ")

def keepRNA():
    global RNACode
    global inputCode
    if "U" in inputCode or "u" in inputCode:
        print("Input is already RNA, keeping code")
        for i in range(0, len(inputCode)):
            RNACode.append(inputCode[i])
    else:
        translateRNA(inputCode)

def main():
    global RNACode
    global canCalculateBool
    global inputCode
    canCalculate(inputCode)
    if canCalculateBool == True:
        checkStart(inputCode)
        keepRNA()
        print(RNACode)
        transcriptionProtein()
    elif canCalculateBool == False:
        continueInput = input("Input cannot be translated into codons. Continue with translation into RNA? Y/n")
        if continueInput == "Y" or continueInput == "y":
            checkStart(inputCode)
            keepRNA()
            print(RNACode)

main()


    