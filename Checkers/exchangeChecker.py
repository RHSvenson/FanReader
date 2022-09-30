# Denne kontrollere hvorvidt sætningen hænger sammen med sidste sætning.
# Altså er der tale om en frem-og-tilbage samtale mellem de samme karaktere.
# Dette er en last-resort, da den kan være upålidelig.

def exchangeChecker(phrase, charTags):
    import re

    