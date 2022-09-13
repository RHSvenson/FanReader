from genericpath import exists
import re
from unicodedata import name
from snippeter import *


with open ("exampletags.txt") as tags:
    # Omdan dokument til string
    tags = tags.read()
    # Find alle tags markeret som karakterer
    # Dette kræver et specifikt layout i listen. Vi har ingen API access endnu, så det er svært at forudsige hvordan denne reelt vil se ud.
    charTags = re.findall("(?<=Character=\")[\w\d\s]+(?=\")", tags)
    
    # Derefter skal vi have vores liste af snippets
    snippetDictionary = snippeter("examplestory.txt","")

    # Kontroller historiens perspektiv ud fra første 20 snippets
    for x in snippetDictionary[:20]:
        if x[0] == 0 and re.search(" I ",x[1]) != None:
            isFirstPerson = True
            break

    print(isFirstPerson)

    print(charTags)



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