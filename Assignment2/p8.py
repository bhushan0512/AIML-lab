def demonstrate_list_operations():
    sample_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    
    print("Original List:", sample_list)
    print("Element at index 0 (first element):", sample_list[0])
    print("Element at index 3 (fourth element):", sample_list[3])
    print("Element at index 6 (last element):", sample_list[6])

    print("\nSlicing Examples:")
    print("Elements from index 1 to 4 (exclusive):", sample_list[1:4])
    print("Elements from the start to index 3 (exclusive):", sample_list[:4])
    print("Elements from index 3 to the end:", sample_list[3:])
    print("Copy of the entire list:", sample_list[:])
    
    print("\nNegative Indexing Examples:")
    print("Element at index -1 (last element):", sample_list[-1])
    print("Element at index -3 (third from last):", sample_list[-3])
    print("Element at index -6 (sixth from last):", sample_list[-6])

    print("\nNegative Slicing Examples:")
    print("Elements from index -5 to -2 (exclusive):", sample_list[-5:-2])
    print("Elements from the start to index -3 (exclusive):", sample_list[:-3])
    print("Elements from index -4 to the end:", sample_list[-4:])


demonstrate_list_operations()
