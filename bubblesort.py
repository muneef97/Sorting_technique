def bubblesort(list):
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if(list[j]>list[j+1]):
                list[j],list[j+1] = list[j+1],list[j]
    return list

list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)