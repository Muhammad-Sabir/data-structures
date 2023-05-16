# solution 1

def isAnagram(s, t):
    if(sorted(s) == sorted(t)):
        return True
    return False

print(isAnagram("hola", "aloh"))
print(isAnagram("hola", "allh"))

# solution 2

def isAnagram2(s, t):
    if (len(s) != len(t)):
        return False

    hashS = {}
    hashT = {}

    for i in range(len(s)):
        if s[i] not in hashS:
            hashS[s[i]] = 1
        else: 
            hashS[s[i]] += 1

        if t[i] not in hashT:
            hashT[t[i]] = 1
        else: 
            hashT[t[i]] += 1

    return hashS == hashT

print(isAnagram2("hill", "hlil"))

# solution 3

def isAnagram3(s, t):
        if len(s) != len(t):
            return False

        hashS, hashT = {}, {}

        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
        return hashS == hashT

print(isAnagram3("hill", "hlil"))