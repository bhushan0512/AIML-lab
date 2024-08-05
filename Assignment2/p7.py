def demonstrate_dict_methods():
    my_dict = dict(a=1, b=2, c=3)
    print("Original Dictionary:", my_dict)

    my_dict.clear()
    print("\nAfter clear():", my_dict)
    
    my_dict = dict(a=1, b=2, c=3)
    
    copied_dict = my_dict.copy()
    print("\nCopied Dictionary:", copied_dict)
    
    keys = ['x', 'y', 'z']
    new_dict = dict.fromkeys(keys, 0)
    print("\nNew Dictionary from keys with default value 0:", new_dict)
    
    value_of_a = my_dict.get('a')
    print("\nValue associated with key 'a':", value_of_a)
    
    items = my_dict.items()
    print("\nDictionary items:", list(items))
    
    keys = my_dict.keys()
    print("\nDictionary keys:", list(keys))
    
    values = my_dict.values()
    print("\nDictionary values:", list(values))
    
    removed_value = my_dict.pop('b', 'Not Found')
    print("\nRemoved value associated with key 'b':", removed_value)
    print("Dictionary after pop():", my_dict)
    
    popped_item = my_dict.popitem()
    print("\nRemoved item:", popped_item)
    print("Dictionary after popitem():", my_dict)
    
    default_value = my_dict.setdefault('d', 4)
    print("\nValue of key 'd' (default value if not present):", default_value)
    print("Dictionary after setdefault():", my_dict)
    
    update_dict = {'e': 5, 'f': 6}
    my_dict.update(update_dict)
    print("\nDictionary after update():", my_dict)


demonstrate_dict_methods()
