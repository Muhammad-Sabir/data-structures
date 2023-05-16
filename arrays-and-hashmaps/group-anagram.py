strs = ["eat","tea","tan","ate","nat","bat"]

# solution 1

def groupAnagrams(strs):
    hashStrs = {}

    for i in range(len(strs)):
        sorterStr = "".join(sorted(strs[i]))

        if sorterStr in hashStrs:
            hashStrs[sorterStr].append( strs[i] )
        else:
            hashStrs[sorterStr] = [ strs[i] ]
    
    return list ( hashStrs.values() )

print(groupAnagrams(strs))