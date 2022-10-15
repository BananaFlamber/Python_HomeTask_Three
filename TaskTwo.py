print("\033c")

list_one = [1,2,3,4,5,6,7,8,9]
print(list_one)
list_two = []
def composition_list(list_one,list_two):
    index = -1
    for i in range(len(list_one)):
        while i < len(list_one)/2:
            result = list_one[i] * list_one[index]
            list_two.append(result)
            i += 1
            index = index - 1
        return list_two

print(composition_list(list_one,list_two))