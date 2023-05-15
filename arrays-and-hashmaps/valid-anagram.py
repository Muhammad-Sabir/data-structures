# solution 1

def isAnagram(s, t):
    if(sorted(s) == sorted(t)):
        return True
    return False

print(isAnagram("hola", "aloh"))
print(isAnagram("hola", "allh"))