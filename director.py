from genericpath import exists
import re
from unicodedata import name
from snippeter import *
from saidsynonyms import *


bøn = "I Faderen og Sønnen, og Helligåndens navn, Amen. Herre, den menneskelige intelligens kan aldrig sammenlignes med din, og endnu mindre kan de ringe efterligninger af intelligens vi producerer på vor maskiner. Alligevel beder jeg dig om at velsigne os med din skabelseskløgt, så vi kan producere et godt produkt til din ære. Ved Kristus vor Herre, amen."

# Derefter skal vi have vores liste af snippets
snippetDictionary = snippeter("examplestory.txt","")

# Kontroller historiens perspektiv ud fra første 20 snippets
isFirstPerson = False
for x in snippetDictionary[:20]:
    if x[0] == 0 and re.search(" I ",x[1]) != None:
        isFirstPerson = True
        break

narrator = "Discord" # Dette skal slettes en dag når vi får skabt prompten til at vælge hovedperson

# Her begynder beslutningsloopet

lineList = []
i = 0
for snippet in snippetDictionary:
    # Hvis det er et narrationstykke, er det ret simpelt
    if snippet[0] == 0:
        phraseCache = (narrator, x[1])
        lineList.append(phraseCache)
    # This is where the fun begins
    elif snippet[0] == 1:
        # Vi starter med at se om der er nogle ledetråde omkring sætningen
        snipScan = snippetDictionary[i:i+2]
        print(snipScan)
        phraseCache = saidChecker(snipScan)
        lineList.append(phraseCache)
    i = i + 1

        

print(lineList)

print(isFirstPerson)


#val str = narrator
#    if "i" is within the current_line in narration:
#        then str = "charactertag"
#    elif "i" does not exists within the scope of narration
#        then str = "narratortag"


#val str = charactertag
#    if line within director_log holds defined name
#        then str = ("charactertag"+(1))


#srefer to narratortag
#    narrator = 0


#refer to charactertag
#    characrer = (int+1)