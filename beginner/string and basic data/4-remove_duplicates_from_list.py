def remove_duplicates_from_list(list: list):
    i = 0
    while i< len(list):
        j = i + 1
        while j < len(list):
            if list[i] == list[j]:
                list.pop(j)
            else :
                j += 1
        i+=1
    return list


list1 = ['item1', 'item2', 'item2', 'item3']
list2 = [ 1, 2, 3, 3, 4]

new_list1 = remove_duplicates_from_list(list1)
new_list2 = remove_duplicates_from_list(list2)

print(new_list1)
print(new_list2)