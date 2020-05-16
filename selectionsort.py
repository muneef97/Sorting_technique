def selectionsort(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if(list[i]>list[j]):
                list[i], list[j] = list[j], list[i]
    return list

list = [19,2,31,45,6,11,121,27]
selectionsort(list)
print(list)