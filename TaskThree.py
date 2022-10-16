
numbers_list = [0.39,1.2,0.9,12,4.1]
print(numbers_list)

temp_list = []

def decimal_value (list1, list2):
    for i in range(len(list1)):
        list2.append(round(list1[i] % 1,2))
        
    return(list2)

print(decimal_value(numbers_list,temp_list))

# print(temp_list)

# def find_max(list):
    
# def find_min(list):
    