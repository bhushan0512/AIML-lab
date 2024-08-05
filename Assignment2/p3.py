def merge_lists(list1, list2):
    merged_list_1 = list1 + list2
    
    merged_list_2 = list1.copy()
    merged_list_2.extend(list2)
    
    merged_list_3 = [*list1, *list2]
    
    return merged_list_1, merged_list_2, merged_list_3

def main():
    list1 = input("Enter the first list of numbers (comma-separated): ")
    list1 = list(map(int, list1.split(',')))
    
    list2 = input("Enter the second list of numbers (comma-separated): ")
    list2 = list(map(int, list2.split(',')))
    
    merged_list_1, merged_list_2, merged_list_3 = merge_lists(list1, list2)
    
    print("Merged List using '+':", merged_list_1)
    print("Merged List using 'extend()':", merged_list_2)
    print("Merged List using list unpacking:", merged_list_3)

main()
