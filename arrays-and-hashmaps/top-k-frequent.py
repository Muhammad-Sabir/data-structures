#solution 1
# WRONGGGG
def topKFrequent(nums, k):
    hashNums = {}
    returnList = []
    
    for num in nums:
        hashNums[str(num)] = 1 + hashNums.get(str(num), 0)

    for x in hashNums:
        returnList.append( int(x) )

    return sorted(returnList)[0:k]

print(topKFrequent([1, 4, 2, 2, 2, 3], 1))