nums = [3, 12, 53, 18, 91]
nums2 = map(lambda x: 2*x+1, nums)
print(list(nums2))
nums3 = filter(lambda z: (-z < -20), nums)
print(list(nums3))

# Here is a weird way to define a function
anonFn = lambda x, y: max(x / y, y / x)
print(anonFn(35, 12))