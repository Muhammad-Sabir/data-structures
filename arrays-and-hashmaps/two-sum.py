# solution 1

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j == i: continue
            
            if nums[i] + nums[j] == target:
                return [i, j]

print(twoSum([1, 1, 5, 8, 4, 3], 2))

# solution 2

def twoSum2(nums, target):
    hashSum = {}

    for i in range(len(nums)):
        if str(target - nums[i]) in hashSum:
            return [int( hashSum[str(target - nums[i])] ), i]
        
        hashSum[ str(nums[i]) ] = i

print(twoSum2([1, 1, 5, 8, 4, 3, 5], 10))