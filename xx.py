def checkio(data):
    from collections import Counter
    nonunique = Counter(data) - Counter(set(data))
    return [x for x in data if x in nonunique]
print(checkio([1, 2, 3, 1, 3]))

