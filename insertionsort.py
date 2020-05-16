def insertionsort(list):
    for i in range(1,len(list)):
        key = list[i]
        j = i - 1
        while(j>=0 and key < list[j]):
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    return list

list = [19,2,31,45,6,11,121,27]
insertionsort(list)
print(list)