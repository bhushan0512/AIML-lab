def demonstrate_list_vs_tuple():
    my_list = [1, 2, 3, 4, 5]
    my_tuple = (1, 2, 3, 4, 5)
    
    print("Original List:", my_list)
    my_list.append(6)
    print("List after append:", my_list)
    my_list[0] = 10
    print("List after modification:", my_list)
    my_list.remove(4)
    print("List after removal:", my_list)
    
    print("\nOriginal Tuple:", my_tuple)
    try:
        my_tuple[0] = 10
    except TypeError as e:
        print("!!!Error modifying tuple!!!\n", e)
    
    print("Count of 2 in tuple:", my_tuple.count(2))
    print("Index of 3 in tuple:", my_tuple.index(3))

    a, b, c, d, e = my_tuple
    print("Unpacked values:", a, b, c, d, e)

demonstrate_list_vs_tuple()
