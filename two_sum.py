# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.
def two_sum(num, target):
    offsets = []
    seen = {}

    for i in range(len(num)):
        complement = target - num[i]

        # If complement is seen before
        if complement in seen:
            offsets.append((seen[complement], i))

        # Store current and its index
        seen[num[i]] = i

    return offsets

num = [3,2,1,4,5,6,7,8,9,3,7,3]
target = 6

print(two_sum(num, target))