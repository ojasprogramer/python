def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(smallest_num_in_list([1000, 423, 732, 934]))

# This program can help you in finding small numbers froma a given list in the code(But why u need this program are blind?)

