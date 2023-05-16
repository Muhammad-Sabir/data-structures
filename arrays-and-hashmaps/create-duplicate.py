# solution 1

def containsDuplicate(nums):
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if (nums[i] == nums[j]):
                return True

    return False


print(containsDuplicate([1, 1, 2, 56]))

# solution 2

def containsDuplicate2(nums):
    if(len(nums) != len(set(nums))):
        return True

    return False


print(containsDuplicate2([1, 1, 2, 56]))

# solution 3

def containsDuplicate3(nums):
    templist = []

    for i in range(len(nums)):
        if(nums[i] in templist):
            return True

        templist.append(nums[i])

    return False


print(containsDuplicate3([1, 1, 2, 56]))

# solution 4

def containsDuplicate4(nums):
    hashList = {}

    for i in range(len(nums)):
        if str(nums[i]) in templist:
            return True
        else:
            templist[str(nums[i])] = i

    return False

print(containsDuplicate4([1, 1, 2, 56]))