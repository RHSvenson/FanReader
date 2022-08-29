# Snippeter er programmet ansvarlig for at inddele historien i "snippets" som så kan tilddeles forskellige karakterer
import re
import time



with open("examplestory.txt") as story_file:
    # Tildel en tæller til variablerne så vi dynamisk kan tildele dem i while løkken.
    story_file = story_file.read()
    variableCounter = 0
    charCounter = 0
    charCounterTotal = 0
    snippetDictionary = []


    # Vi starter med at skippe alt hvad der ikke er alfanumerisk, for at undgå titelformatering mm
    print("Starter scanning...")
    while re.search("\w| |\"", story_file[charCounterTotal]) == None:
        charCounterTotal += 1
    # Hovedløkke, denne danner en ny streng for hver "adskiller". Typisk et \n eller "
    # Så længe den totale mængde karakterer talt er under den totale mængde i tekst filen, fortsætter vi.
    print("Startloop færdig.")
    print(len(story_file))
    while charCounterTotal < len(story_file)-1:
            # Derefter starter vi med at lede efter alfanumeriske
            if re.search("\w|\ |\,|\.|\:|\;|'|\?|\!|-|—|\(|\)", story_file[charCounterTotal]) != None:
                # Som vi så tilføjer til snippetArray
                snippetDictionary += story_file[charCounterTotal]
                charCounterTotal += 1
            # Nye linjer og gåseøjne springes over.
            elif re.search("\n|\r", story_file[charCounterTotal]) != None:
                # Lav en intern overspringshandling indtil vi er tilbage til en alfanumerisk
                while re.search("\n|\r", story_file[charCounterTotal]) != None:
                    charCounterTotal += 1
                variableCounter += 1
            elif re.search("\"", story_file[charCounterTotal]) != None:
                # Spring selve gåseøjnene over, og overgå derefter til en ny variabel.
                # Bemærk at den tidligere elif for nye linjers while loop betyder at gåseøjne efter \n overspringes
                # så vi undgår for mange variableCounter switches.
                charCounterTotal += 1
            else:
                charCounterTotal += 1
                print("Fejl, ukendt karakter:", story_file[charCounterTotal])

    print(snippetDictionary)
    print(charCounterTotal)
            


