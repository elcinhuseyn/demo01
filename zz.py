def checkio(data):
    newlist=[]
    for i in data:
        if data.count(i) > 1:
            newlist.append(i)
    return data

print(checkio([1, 2, 3, 1, 3]))

