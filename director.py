
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
    
    # Enormt vigtig variabel. Ideelt vil denne hentes fra en API værdi, men kan alternativt manuelt udpejes.
    from DataTools.nameScanner import nameScanner
    charTags = nameScanner(
        snippetList=snippetDictionary,
        universe = "MLPFiM"
    )

    narrator = "Narrator" # Dette skal slettes en dag når vi får skabt prompten til at vælge hovedperson

    # Linelist er variablen som opbevarer den resultatet af vores script.
    # TODO: Efterbehandl denne
    lineList = []

    # Loopet benytter en i variabel som tæller.
    # Dette er LOOPET. Her sker næsten alt.
    i = 0
    for snippet in snippetDictionary:

        # Alle snippets gennemgår alle checks.

        # saidChecker er altid først, da den er mest pålidelig. De andre bygger videre på dens return.
        phraseCache = saidChecker(
            snippet = snippet, 
            dictionary = "Ordbøger/saidSynonyms.txt", 
            charTags = charTags
        )

        if i < 4:
            phraseCache = phraseCache
        # Hvis der var en saidBefore i tidligere sætning, så springer vi alt det her over, da vi allerede kender svaret.
        elif lineList[i-1]["Parameters"] != None and lineList[i-1]["Parameters"][0] == "saidbefore":
            phraseCache = {
                # lineList indexet her henter karakterstykket fra Parameter indexet fra sidste phraseCache.
                "Character": lineList[i-1]["Parameters"][1],
                "Sentence": phraseCache["Sentence"],
                "Parameters": phraseCache["Parameters"]
            }
        elif phraseCache["Parameters"] != None:
            if phraseCache["Parameters"][0] == "saidafter":
                # Hvis der var en saidAfter, så sæt tidligere linje til (karakter, samme linje, samme data)
                lineList[i-1] = (
                    phraseCache["Parameters"][1],
                    # lineList indexene her referer til sætningne inden nuværende i loopet.
                    lineList[i-1]["Sentence"],
                    lineList[i-1]["Parameters"]
                )


        
        print(phraseCache)
        if snippet[0] == 0:
            phraseCache = {
                "Character": narrator, 
                "Sentence": phraseCache["Sentence"], 
                "Parameters": phraseCache["Parameters"]
            }
        ## Indsættelse til sidst
        lineList.append(phraseCache)
        

        i += 1

            

    for line in lineList:
        print(line)