# merging two lists in single list and Finding an duplicate elements from list 

list1 = [1,2,2,1,3,4,4]
list2 = [2,3,3,4,2,3,5,6]
list3 = []

for i in list1:
    if(i not in list3):
        list3.append(i)
for i in list2:
    if(i not in list3):
        list3.append(i)
        
print("list1 = ",list1)
print("list2 = ", list2)
print("list3 = ", list3)
