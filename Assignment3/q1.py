def print_initials():
    full_name = input("Enter your full name (first name middle name last name): ")
    name_parts = full_name.split()
    initials = [part[0].upper() + '.' for part in name_parts]
    print(' '.join(initials))

print_initials()
