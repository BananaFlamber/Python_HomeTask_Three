print("\033c")

list = [1,2,3,4,5,6,7,8,9]
print(list)

def odd_summ(list):
    result = 0
    # print(result)
    for i in range(len(list)):
        if i % 2 != 0:
            result += list[i]
            # print(result)
    return result

print(odd_summ(list))