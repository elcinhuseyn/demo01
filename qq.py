a=[8, 14, 7, 7, 15, 3, 5, 9, 12, 1, 7, 9, 11, 9, 14, 13, 5, 12, 8, 6]
new_list = []

while a:
    minimum = a[0]  # arbitrary number in list 
    for x in a: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    a.remove(minimum)    

print(new_list)
