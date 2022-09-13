# Snippeter er programmet ansvarlig for at inddele historien i "snippets" som så kan tilddeles forskellige karakterer
import re
import time


def snippeter(file):
    with open(file) as story_file:
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

        # Kontorlelement, håndterer vi en sætning?
        sentenceOngoing = False

        # Vi starter med at skippe alt hvad der ikke er alfanumerisk, for at undgå titelformatering mm
        print("Starter scanning...")

        # Så længe vi ikke har nogen alfanumerisk karakter, så springer vi bare over.
        #while re.search("\w|\"", story_file[charCounterTotal]) == None:
        #    charCounterTotal += 1
        # Hovedløkke, denne danner en ny streng for hver "adskiller". Typisk et \n eller "
        # Så længe den totale mængde karakterer talt er under den totale mængde i tekst filen, fortsætter vi.
        print("Startloop færdig.")
        while charCounterTotal < len(story_file)-1:
                # Kontroller altid først om vi har at gøre med gåseøjne eller andre sætningsindikatorer.
                if re.search("\"",story_file[charCounterTotal]) != None:
                    # Hvis der allerede er en sætning igang, afslut denne og indlem cache i liste.
                    if sentenceOngoing == True:
                        stringCache = re.sub("\"", "", stringCache)
                        globals()[f"snippet{variableCounter}"] = (1,str(stringCache))
                        sentenceOngoing = False
                    # Ellers så påbegynd en ny sætning, og afslut tidligere narration
                    else:
                        stringCache = re.sub("\"", "", stringCache)
                        globals()[f"snippet{variableCounter}"] = (0,str(stringCache))
                        sentenceOngoing = True
                    if stringCache != "":
                        snippetDictionary.append([f"snippet{variableCounter}"])
                        variableCounter += 1

                    # Nulstil og videre
                    stringCache = ""
                    charCounterTotal += 1
                    # Bemærk at vi springer gåseøjet over. Vi vil ikke have den med i vores snippet.
                # Enter og andre paragraf seperatorer springer vi let og elegant over.
                elif re.search("[\n\r]",story_file[charCounterTotal]):
                    # Indlem først den nuværende string, og så spring over til næste paragraf.
                    if stringCache != "" and stringCache != " ":
                        stringCache = re.sub("\"", "", stringCache)
                        globals()[f"snippet{variableCounter}"] = (0,str(stringCache))
                        snippetDictionary.append([f"snippet{variableCounter}"])
                        variableCounter += 1
                    stringCache = ""
                    while re.search("[\n\r]", story_file[charCounterTotal]) != None:
                        charCounterTotal += 1
                # Hvis der ikke er nogen sætningsindikatorer, så kontrollerer vi efter alfanumeriske.
                elif re.search("[\w\ \,\.\:\;'\?\!-—\(\)]", story_file[charCounterTotal]):
                    stringCache += story_file[charCounterTotal]
                    charCounterTotal += 1
                else:
                    print("Fejl, ukendt karakter:", story_file[charCounterTotal])
                    charCounterTotal += 1





        print(snippetDictionary)
        print(charCounterTotal)
        i = 0
        while i <= variableCounter:
            print({i}, globals()[f"snippet{i}"])
            i += 1
            
snippeter("examplestory.txt")

