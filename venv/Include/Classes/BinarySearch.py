def bindary_search(list):
    low = 0
    high = len(list)-1
    count = 0;

    while low <= high:
        mid = round((low + high) / 2)
        guess = list[mid-1]
        high = mid
        if mid == low and mid == high:
            count = count + 1
            print(count)
            return mid
        elif mid != low or mid != high:
            count = count + 1