
from xml.dom.minidom import CharacterData


def director():
    from genericpath import exists
    import re
    from unicodedata import name
    from snippeter import snippeter
    #from utils.Cleaners import charTagsGen


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
    lastChars = []
    from Checkers.saidChecker import saidChecker
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
        # Kontroller efter saidafter, hvis den er positiv og der er en karakter forsynet, så ret
        # tidligere sætning til dette.
        # saidafter værdier er alle ting som characterafter, og indikerer at der var en direkte
        # sætning der siger hvem der taler, såsom "She said".
        elif phraseCache["Parameters"] != None:
            # Characterafter er den mest sikre, og her kan vi bare rette til den fundne character værdi.
            if phraseCache["Parameters"][0] == "characterafter":
                lineList[i-1] = (
                    # Parameters[1] er den fundne karakters navn.
                    phraseCache["Parameters"][1],
                    lineList[i-1]["Sentence"],
                    lineList[i-1]["Parameters"]
                )
                # Det er vigtigt for andre funktioner at vi lige gemmer hvem den sidstnævnte karakter er.
                # Vi finder entriet fra chartags så vi har alt data ved hånden.
                # Vi gemmer de sidste 3 karaktere, ikke mere.
                if lastChars != None:
                    lastChars[2] = lastChars[1]
                    lastChars[1] = lastChars[0]
                lastChars[0] = charTags[phraseCache["Parameters"][1]]
            # Efter det er pronounafter, som er let at spotte og også ret sikker.
            # Denne vil næsten altid referer til den sidst-nævnte karakter af det køn, så dette
            # går vi også ud fra.
            elif phraseCache["Parameters"][0] == "pronounafter":
                if lastChars == None:
                    print("ERROR: No characters encountered, cannot utilize pronounafter.")
                else:
                    # Loop igennem vores sidstnævnte karakterer, tag den første med rigtig køn
                    for character in lastChars:
                        if charTags[character]["Gender"] == "Male" and phraseCache["Parameters"][1] == "lastmale":
                            lineList[i-1][0] = character
                            break
                        elif charTags[character]["Gender"] == "Female" and phraseCache["Parameters"][1] == "lastfemale":
                            lineList[i-1][0] = character
                            break
            elif phraseCache["Parameters"][0] == "addressafter":
                if lastChars == None:
                    print("ERROR: No characters encountered, cannot utilize addresafter.")
                    # TODO: Tilføj addresschecker


                    
            

        
        
        # Efter vi har brugt saidCheckers parametre, videregiver vi phrasen til endFocusChecker.
        # Dette er fordi mange andre funktioner bedre kan benytte endFocus' værdier.

        # TODO: Tilføj endFocusChecker

        # endFocus indikatorer gives videre til exchangeChecker.


        # Til sidst tildeler vi narrator til narration stykker. Vi skal stadig bruge
        # parameters herfra, derfor kører de stadig igennem hele maskineriet.
        if snippet[0] == 0:
            phraseCache = {
                "Character": narrator, 
                "Sentence": phraseCache["Sentence"], 
                "Parameters": phraseCache["Parameters"]
            }
        ## Indsættelse til sidst
        lineList.append(phraseCache)
        
        # Tæller variabel, til at holde styr på hvor vi er i listen.
        i += 1

            

    for line in lineList:
        print(line)