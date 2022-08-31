# Snippeter er programmet ansvarlig for at inddele historien i "snippets" som så kan tilddeles forskellige karakterer
import re
import time



with open("examplestory.txt") as story_file:
    # Omdan story_file til en en lang string.
    story_file = story_file.read()

    # Tæller til hvor mange gange vi har skiftet snippet
    variableCounter = 0

    # Tæller til hvor mange karakterer vi er igennem, til at iterere med
    charCounterTotal = 0

    # Faktisk ikke en dictionary, men en liste. Indeholder vores tuples.
    snippetDictionary = []

    # Midlertidig opbevaring til de sætninger vi bygger.
    stringCache = ""

    # Vi starter med at skippe alt hvad der ikke er alfanumerisk, for at undgå titelformatering mm
    print("Starter scanning...")

    # Så længe vi ikke har nogen alfanumerisk karakter, så springer vi bare over.
    while re.search("\w|\")", story_file[charCounterTotal]) == None:
        charCounterTotal += 1
    # Hovedløkke, denne danner en ny streng for hver "adskiller". Typisk et \n eller "
    # Så længe den totale mængde karakterer talt er under den totale mængde i tekst filen, fortsætter vi.
    print("Startloop færdig.")
    while charCounterTotal < len(story_file)-1:
            # Derefter starter vi med at lede efter alfanumeriske
            if re.search("\w|\ |\,|\.|\:|\;|'|\?|\!|-|—|\(|\)", story_file[charCounterTotal]) != None:
                # Hver gang vi finder en alfanumerisk, tilføjer vi den til slutningen af vores midlertidige string.
                stringCache += story_file[charCounterTotal]

                # Og øger tælleren med en.
                charCounterTotal += 1
            # Nye linjer og gåseøjne springes over.
            elif re.search("\n|\r\\^M|\ ", story_file[charCounterTotal]) != None:
                # Lav en intern overspringshandling indtil vi er tilbage til en alfanumerisk, ligesom i starten.
                while re.search("\n|\r|\^M|\ ", story_file[charCounterTotal]) != None:
                    charCounterTotal += 1

                # Lav dynamiske tuples og tilføj dem til den globale variabel liste
                globals()[f"snippet{variableCounter}"] = (0,str(stringCache))
                if stringCache != '' or stringCache != ' ':
                    # Gør den midlertidige string permanent, og tilføj
                    snippetDictionary.append([f"snippet{variableCounter}"])
                    variableCounter += 1
                stringCache = ""
            elif re.search("\"", story_file[charCounterTotal]) != None:
                # Spring selve gåseøjnene over, og overgå derefter til en ny variabel.
                # Bemærk at den tidligere elif for nye linjers while loop betyder at gåseøjne efter \n overspringes
                # så vi undgår for mange variableCounter switches.
                charCounterTotal += 1
                # Tildel værdi 1 for dialog snippet
                globals()[f"snippet{variableCounter}"] = (1,str(stringCache))
                if stringCache != '' or stringCache != ' ':
                    snippetDictionary.append([f"snippet{variableCounter}"])
                    variableCounter += 1
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
            


