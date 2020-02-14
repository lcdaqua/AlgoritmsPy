def sum(massive):
    if len(massive) == 0:
        return 0
    else:
        massiveX = [massive[i+1] for i in range(len(massive)-1)]
        return massive[0] + sum(massiveX)