'''

Anagrame:

- sunt cuvinte ca prin rearanjarea literelor lor rezulta cuvinte noi (citibil)
s1 = "fairy tales"
s2 = "rail safety"

Ex: se se creeze o functie ce primeste ca parametrii cele doua string-uri, s1 - s2 si
sa se verifice daca sunt sau nu anagrame.
'''
string1 = "fairy tales"
string2 = "rail safety"

def doua_stringuri(string1,string2):
    string1 = string1.lower()
    string2 = string2.lower()
    string1 = string1.replace(" ",'')
    string2 = string2.replace(" ", '')
    if len(string1)<len(string2):
        return "Nu exista"

    if sorted(string1) == sorted(string2):
        return "Sunt anagrame"
    else:
        return"Nu sunt anagrame"
print(doua_stringuri(string1,string2))
