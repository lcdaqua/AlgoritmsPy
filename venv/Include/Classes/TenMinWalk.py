def is_valid_walk(walk):

    result = {}
    result["ns"] = 0
    result["we"] = 0

    for i in range (0, len(walk)):
        if (walk[i] == "n"):
            result["ns"] = result.get("ns") + 1
        elif (walk[i] == "s"):
            result["ns"] = result.get("ns") - 1
        elif (walk[i] == "e"):
            result["we"] = result.get("we") + 1
        else:
            result["we"] = result.get("we") - 1

    if len(walk) == 10 and result.get("ns") == 0 and result.get("we") == 0:
        return True
    else:
        return False