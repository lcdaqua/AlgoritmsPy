def descending_order(num):
    nums = []
    result = 0

    if num > 0:
        while num != 0:
            nums.append(num % 10)
            num = num // 10

    nums.sort()
    nums.reverse()

    for i in range (0, len(nums)):
        result = (result * 10) + nums[i]

    return result