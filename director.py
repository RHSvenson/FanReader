
def director():
    from genericpath import exists
    import re
    from unicodedata import name
    from snippeter import snippeter
    #from utils.Cleaners import charTagsGen
    from Checkers.saidChecker import saidChecker


    bøn = "I Faderen og Sønnen, og Helligåndens navn, Amen. Herre, den menneskelige intelligens kan aldrig sammenlignes med din, og endnu mindre kan de ringe efterligninger af intelligens vi producerer på vor maskiner. Alligevel beder jeg dig om at velsigne os med din skabelseskløgt, så vi kan producere et godt produkt til din ære. Ved Kristus vor Herre, amen."

    # Derefter skal vi have vores liste af snippets
    snippetDictionary = snippeter("examplestory.txt","")

    # Kontroller historiens perspektiv ud fra første 20 snippets
    isFirstPerson = False
    for x in snippetDictionary[:20]:
        if x[0] == 0 and re.search(" I ",x[1]) != None:
            isFirstPerson = True
            break

    narrator = "Narrator" # Dette skal slettes en dag når vi får skabt prompten til at vælge hovedperson

    # Enormt vigtig variabel. Ideelt vil denne hentes fra en API værdi, men kan alternativt manuelt udpejes.
    from utils.Cleaners import charTagsGen
    charTagsPath = "exampletags.txt"
    charTags = charTagsGen(charTagsPath)

    # Linelist er variablen som opbevarer den resultatet af vores script.
    # TODO: Efterbehandl denne
    lineList = []

    # Loopet benytter en i variabel som tæller.
    i = 0
    for snippet in snippetDictionary:
        # Hvis det er et narrationstykke, er det ret simpelt
        if snippet[0] == 0:
            phraseCache = (narrator, snippet[1])
            lineList.append(phraseCache)
        # This is where the fun begins
        elif snippet[0] == 1:
            # Vi caller alle vores grammatisk tjekfunktioner til at opveje hvorvidt
            # vi har at gøre med den ene karakter eller anden.
            snipScan = snippetDictionary[i-1:i+1]
            # saidChecker er den stærkeste af dem alle. Den tager prioritet,
            # da den næsten altid har ret.
            phraseCache = saidChecker(
                snippets = snipScan, 
                dictionaryPath = "Ordbøger/saidSynonyms.txt", 
                charTags = charTags,
                debug = False )

            if phraseCache != "F":
                lineList.append((phraseCache, snippet[1]))
            else:
                lineList.append(("Unknown", snippet[1]))

        i += 1

            

    print(lineList)
    print(isFirstPerson)