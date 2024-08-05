def demonstrate_conversions():
    my_tuple = (1, 2, 3, 4)
    tuple_to_list = list(my_tuple)
    print("Tuple:", my_tuple)
    print("Converted to List:", tuple_to_list)

    my_string = "hello"
    string_to_list = list(my_string)
    print("\nString:", my_string)
    print("Converted to List:", string_to_list)

    my_list = [5, 6, 7, 8]
    list_to_tuple = tuple(my_list)
    print("\nList:", my_list)
    print("Converted to Tuple:", list_to_tuple)

    another_string = "world"
    string_to_tuple = tuple(another_string)
    print("\nString:", another_string)
    print("Converted to Tuple:", string_to_tuple)

    list_for_str = [9, 10, 11]
    list_to_str = str(list_for_str)
    print("\nList:", list_for_str)
    print("Converted to String:", list_to_str)

    tuple_for_str = (12, 13, 14)
    tuple_to_str = str(tuple_for_str)
    print("\nTuple:", tuple_for_str)
    print("Converted to String:", tuple_to_str)


demonstrate_conversions()
