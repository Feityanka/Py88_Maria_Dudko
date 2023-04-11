def baz():
    var = False
    return [int(var), int(not var), len(str(var))+len(str(var))]


numbers = baz()
print(numbers)