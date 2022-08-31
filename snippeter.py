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
    stringCache = ""

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
                stringCache += story_file[charCounterTotal]
                # Som vi så tilføjer til snippetArray
                charCounterTotal += 1
            # Nye linjer og gåseøjne springes over.
            elif re.search("\n|\r\\^M", story_file[charCounterTotal]) != None:
                # Lav en intern overspringshandling indtil vi er tilbage til en alfanumerisk
                while re.search("\n|\r|\^M", story_file[charCounterTotal]) != None:
                    charCounterTotal += 1
                # Generer snippets, tildel værdi 0 for højtlæser snippet
                globals()[f"snippet{variableCounter}"] = (0,str(stringCache))
                variableCounter += 1
                snippetDictionary.append([f"snippet{variableCounter}"])
                stringCache = ""
            elif re.search("\"", story_file[charCounterTotal]) != None:
                # Spring selve gåseøjnene over, og overgå derefter til en ny variabel.
                # Bemærk at den tidligere elif for nye linjers while loop betyder at gåseøjne efter \n overspringes
                # så vi undgår for mange variableCounter switches.
                charCounterTotal += 1
                # Tildel værdi 1 for dialog snippet
                globals()[f"snippet{variableCounter}"] = (1,str(stringCache))
                variableCounter += 1
                snippetDictionary.append([f"snippet{variableCounter}"])
                stringCache = ""
            else:
                charCounterTotal += 1
                print("Fejl, ukendt karakter:", story_file[charCounterTotal])

    print(snippetDictionary)
    print(charCounterTotal)
    i = 0
    while i != 698:
        print({i}, globals()[f"snippet{i}"])
        i += 1
            


