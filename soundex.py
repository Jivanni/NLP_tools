# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
'''
The Soundex code for a name consists of a letter followed by three numerical digits: the letter is the first letter of the name, and the digits encode the remaining consonants. Consonants at a similar place of articulation share the same digit so, for example, the labial consonants B, F, P, and V are each encoded as the number 1.

The correct value can be found as follows:

1.Retain the first letter of the name and drop all other occurrences of a, e, i, o, u, y, h, w.

2. Replace consonants with digits as follows (after the first letter):
    b, f, p, v → 1
    c, g, j, k, q, s, x, z → 2
    d, t → 3
    l → 4
    m, n → 5
    r → 6
3. If two or more letters with the same number are adjacent in the original name (before step 1), only retain the first letter; also two letters with the same number separated by 'h' or 'w' are coded as a single number, whereas such letters separated by a vowel are coded twice. This rule also applies to the first letter.

4.If you have too few letters in your word that you can't assign three numbers, append with zeros until there are three numbers. If you have four or more numbers, retain only the first three.

Using this algorithm, both "Robert" and "Rupert" return the same string "R163" while "Rubin" yields "R150". "Ashcraft" and "Ashcroft" both yield "A261". "Tymczak" yields "T522" not "T520" (the chars 'z' and 'k' in the name are coded as 2 twice since a vowel lies in between them). "Pfister" yields "P236" not "P123" (the first two letters have the same number and are coded once as 'P'), and "Honeyman" yields "H555".

'''


# %%
import re


# %%
pairs = {
("a", "e", "i", "o", "u", "y"): "0",
("b", "f", "p", "v"):"1",
("c", "g", "j", "k", "q", "s", "x", "z"):"2",
("d", "t"):"3",
("l"):"4",
("m","n"):"5",
("r"):"6",
("h","w"):"h"
}


# %%
# This checks if the each character of the surname is in the dictionary and returns the touple containing said character for substitution
def isindict(value): 
    for tup in pairs.keys():
        if value in tup:
            return tup


# %%
# This function applyes a frist substitution corresponding roughly to steps 1 and 2 of the algorithm
def substitution(surname):
    for index in range(0,len(surname)):
        if isindict(surname[index]):
            surname[index] = pairs[isindict(surname[index])]
    return surname


# %%
# This applyes step 3 of the algorith to the name
def del_adiacent_and_xhx(surname):
    surname_stringify = "".join(surname)
    
    # removes any duplicate adiacent letters with the same number
    p = r'(\d)\1'
    del1 = re.sub(p, "", surname_stringify)
    
    # removes all digit\h or w\digit sequences, w are all normalised to h for simplicity by the function "substitution"
    p2 = r'(\d)h\1'
    del2 = re.sub(p2, "\1", del1)
    
    # cleans up the string removing h and 0s
    p3 = r"[h0]"
    cleanup = re.sub(p3,"",del2)
    return cleanup


# %%
def Soundex(name):
    namelist = list(name.lower())
    
    substituted_surname = substitution(namelist)

    beforefinalcleanup = del_adiacent_and_xhx(substituted_surname)
    
    final = name[0]+ beforefinalcleanup[1:]

    return f"'{name}' encoded in Soundex is: '{final.ljust(4,'0')}'."