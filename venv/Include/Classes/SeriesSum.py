def series_sum(n):
    sum = 0.00
    for i in range (1, n+1):
        sum = sum + (1 / (1 + (3 * (i - 1))))

    finalSum = str(format(sum, ".2f"))
    return finalSum