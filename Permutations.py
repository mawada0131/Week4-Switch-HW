def Permutations_String(str): #1
    if len(str) == 1:
        return str
    if len(str) == 2:
        return [str,str[::-1]]
    else:
        result = []
        for c in str:
            for i in Permutations_String(str.replace(c,"")):
                result.append(c+i)
        return result
