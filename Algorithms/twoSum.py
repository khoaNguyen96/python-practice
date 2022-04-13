def twoSum(nums, target):
    # Create hash map to track the add up value that needed to reach the target and the index of that value 
    hash_table = {}
    # Iterate through the list
    for i in range(len(nums)):
        if nums[i] in hash_table:
            return [hash_table[nums[i]], i]
        else:
            hash_table[target-nums[i]] = i
    return None

# The function has the BigO time is O(N)
