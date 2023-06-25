## Dada una lista de strings implemente una funcion que regrese una lista de tuplas de andgramas.
# Ejemglos: ["apa", "oso","paa","soo"]->["apa,"paa",("oso","soo)]
# ["mama","mimi","momo""maam","oomm"]->[("mama","maam"),("mimi"),("momo","oomm")] [""] -> [("")]

# Defaultdict is a container like dictionaries present in the module collections.
# a sub-class of the dictionary class that returns a dictionary-like object.
from collections import defaultdict

# function that will build anagrams out of a list or tuple.
def bldAnagrams(strs):
    #will store our list as object.
    lstAnagrams = defaultdict(list)

    #sort our list and format 
    for str in strs:
        sortStr = ''.join(sorted(str))
        lstAnagrams[sortStr].append(str)

    # return tuples with the anagrams 
    tuples = [tuple(values) for values in lstAnagrams.values()]
    return tuples

dataSet = ["mama","mimi","momo","maam","oomm"]
tupleList = bldAnagrams(dataSet)
print(tupleList)


