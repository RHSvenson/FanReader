# Snippeter er programmet ansvarlig for at inddele historien i "snippets" som så kan tilddeles forskellige karakterer
import re



with open("examplestory.txt") as story_file:
    # Tildel en tæller til variablerne så vi dynamisk kan tildele dem i while løkken.
    story_file = story_file.read()
    variableCounter = 0
    charCounter = 0
    charCounterTotal = 0
    snippetArray = {}
    # Vi starter med at skippe alt hvad der ikke er alfanumerisk, for at undgå titelformatering mm
    while story_file[charCounterTotal] != "\w":
        charCounterTotal += 1
    # Hovedløkke, denne danner en ny streng for hver "adskiller". Typisk et \n eller "
    # Så længe den totale mængde karakterer talt er under den totale mængde i tekst filen, fortsætter vi.
    while charCounterTotal < len(story_file.read()):
            # Derefter starter vi med at lede efter alfanumeriske
            if story_file[charCounterTotal] == "\D":
                # Som vi så tilføjer til snippetArray
                snippetDictionary[variableCounter] += story_file[charCounterTotal]
                charCounterTotal += 1
            # Nye linjer og gåseøjne springes over.
            elif story_file[charCounterTotal] == "\n":
                # Lav en intern overspringshandling indtil vi er tilbage til en alfanumerisk, derefter opdater variableCounter.
                while story_file[charCounterTotal] != "\w":
                    charCounterTotal +=1
                variableCounter =+ 1
            elif story_file[charCounterTotal] == "\"":
                # Spring selve gåseøjnene over, og overgå derefter til en ny variabel.
                # Bemærk at den tidligere elif for nye linjers while loop betyder at gåseøjne efter \n overspringes
                # så vi undgår for mange variableCounter switches.
                charCounterTotal += 1
                variableCounter += 1


