def count_vowels():
    user_string = input("Enter a string: ").lower()
    vowels = 'aeiou'
    vowel_count = sum(1 for char in user_string if char in vowels)
    print("Number of vowels:", vowel_count)

count_vowels()
