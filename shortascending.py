def short_accending(list1):
    for i in range(0,len(list1)):
        min_index=i
        for j in range(i+1,len(list1)):
            if list1[j]<list1[min_index]:
                min_index=j
        list1[i],list1[min_index]=list1[min_index],list1[i]

    return list1
list1=[13,1,3,5,2,4,9,7,6,8,10,12,11]

print(short_accending(list1))

