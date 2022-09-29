
from xml.dom.minidom import CharacterData


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
        # Alle snippets gennemgår alle checks.

        # saidChecker er altid først, da den er mest pålidelig. De andre bygger videre på dens return.
        phraseCache = saidChecker(snippet = snippet, dictionary="Ordbøger/saidSynonyms.txt", charTags=charTags)

        # Hvis der var en saidBefore i tidligere sætning, så springer vi alt det her over, da vi allerede kender svaret.
        if lineList[i-1][2][0] == "saidBefore":
            lineList.append(lineList[i-1[2][1]], phraseCache[1], phraseCache[2])
            break
        
        if phraseCache[2] != None:
            if phraseCache[2] == "saidAfter":
                # Hvis der var en saidAfter, så sæt tidligere linje til (karakter, samme linje, samme data)
                lineList[i-1] = (phraseCache[0], lineList[i-1][1], lineList[i-1][2])


        


        ## Indsættelse til sidst
        lineList.append(phraseCache)
        

        i += 1

            

    print(lineList)
    print(isFirstPerson)