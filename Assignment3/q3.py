def exchange_characters():
    user_string = input("Enter a string: ")
    if len(user_string) < 2:
        print("String must be at least 2 characters long.")
        return
    new_string = user_string[-1] + user_string[1:-1] + user_string[0]
    print("String with first and last characters exchanged:", new_string)

exchange_characters()
