def check_odd_or_even():
    try:
        number = int(input("Enter a number: "))
        
        if number % 2 == 0:
            print("The number is even.")
            return
        print("The number is odd.")

    except ValueError:
        print("Please enter a valid integer.")

check_odd_or_even()