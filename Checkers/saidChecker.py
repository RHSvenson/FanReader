# Funktion anvendt til at kontrollere tilstedeværelsen af
# sætninger som "I said" omkring en snippet
def saidChecker(snippets, dictionaryPath, charTags, debug=False):
    import re
    with open(dictionaryPath) as file:
        saidSynonyms = file.read()
    for analysisObject in snippets:
        for character in charTags:
            if debug == False:
                if re.search(str(character)+" "+saidSynonyms,analysisObject[1]) != None:
                    return str(character)
                    break
                elif re.search(saidSynonyms+" "+str(character), analysisObject[1]) != None:
                    return str(character)
                    break
                elif re.search(saidSynonyms+" "+"I", analysisObject[1]) != None:
                    return "Main"
                    break
                elif re.search("I"+" "+saidSynonyms, analysisObject[1]) != None:
                    return "Main"
                    break
                else:
                    return "F"
                    break
            elif debug == True:
                print(str(character)+" "+saidSynonyms)
                print(str(character))
                print(analysisObject[1])
                print(saidSynonyms)
                if re.search(str(character)+" "+saidSynonyms,analysisObject[1]) != None:
                    return str(character)
                    break
                elif re.search(saidSynonyms+" "+str(character), analysisObject[1]) != None:
                    return str(character)
                    break
                elif re.search(saidSynonyms+" "+"I", analysisObject[1]) != None:
                    return "Main"
                    break
                elif re.search("I"+" "+saidSynonyms, analysisObject[1]) != None:
                    return "Main"
                    break
                else:
                    return "F"
                    break