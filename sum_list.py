# Summing up a list of Number using Recursive Function

def list_sum(list):

    num_list = list
    print(str(num_list[0]) + ' is added to total')
    if len(num_list) == 1:
        return num_list[0]
    else:
        print('Remaining Items In List - ' + str(num_list[1:]))
        return num_list[0] + list_sum(num_list[1:])


print('The Total is ' + str(list_sum([1,23,4,5,6,73,2,2,31,3])))