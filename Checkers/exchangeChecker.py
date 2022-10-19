# Denne kontrollere hvorvidt sætningen hænger sammen med sidste sætning.
# Altså er der tale om en frem-og-tilbage samtale mellem de samme karaktere.
# Dette er en løbende checker, som kører først og tilbagegiver et status argument til sætningen
# som så kan benyttes af andre funktioner.
# Bemærk at den ikke giver sit return hvis der allerede er en gyldig Said værdi fra saidChecker,
# dette er fordi saidChecker er meget mere nøjagtig end alt andet.

def exchangeChecker(phrase, charTags):
    import re

    