# Implement your function below.
def is_rotation(list1, list2):
    print("Is Rotation")
    # if the lengths differ they cannot be rotations
    print(len(list1))
    print(len(list2))
    if len(list1) != len(list2):
        return False
        
    # both lists are empty, so they must be rotations of each other
    if len(list1) < 1:
        return True
    first_item_list1 = list1[0]
    index = 0
    list2_index = 0
    while index < len(list2):
        print("First Loop")
        if first_item_list1 == list2[index]:
            list2_index = index
            break
        index += 1
        
    index = 0
    while index < len(list1):
        if list2[list2_index] != list1[index]:
            return False
        index = (index + 1)
        list2_index = (list2_index + 1) % len(list2)
    return True

if __name__ == '__main__':
    # NOTE: The following input values will be used for testing your solution.
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2a = [4, 5, 6, 7, 8, 1, 2, 3]
    #print(is_rotation(list1, list2a))
    list2b = [4, 5, 6, 7, 1, 2, 3]
    #print(is_rotation(list1, list2b))
    list2c = [4, 5, 6, 9, 1, 2, 3]
    #print(is_rotation(list1, list2c))

    list2d = [4, 6, 5, 7, 1, 2, 3]
    print(is_rotation(list1, list2d)) 

    list2e = [4, 5, 6, 7, 0, 2, 3]
    print(is_rotation(list1, list2e))

    list2f = [1, 2, 3, 4, 5, 6, 7]
    print(is_rotation(list1, list2f)) 

    list2g = [7, 1, 2, 3, 4, 5, 6]
    print(is_rotation(list1, list2g)) 
