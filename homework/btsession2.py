nums = [16, 2, 4, 2, 128, 64, 16, 7, 1, 64, 32, 16, 5, 8]
con = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] * nums[j] == 256:
            if nums[i] not in con and i!=j:
                con.append(nums[i]) 
                con.append(nums[j])
                print(nums[i], i, nums[j], j)