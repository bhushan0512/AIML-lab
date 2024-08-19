def count_characters():
    user_string = input("Enter a string: ")
    uppercase_count = sum(1 for char in user_string if char.isupper())
    lowercase_count = sum(1 for char in user_string if char.islower())
    digit_count = sum(1 for char in user_string if char.isdigit())
    print("Number of uppercase letters:", uppercase_count)
    print("Number of lowercase letters:", lowercase_count)
    print("Number of digits:", digit_count)

count_characters()
