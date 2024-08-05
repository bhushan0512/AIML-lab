def lcm_two_numbers(a, b):
    if a < b:
        a, b = b, a
    multiple = a
    while multiple % b != 0:
        multiple += a
    return multiple

def lcm_multiple(numbers):
    lcm_result = lcm_two_numbers(numbers[0], numbers[1])
    
    for num in numbers[2:]:
        lcm_result = lcm_two_numbers(lcm_result, num)
    
    return lcm_result

def main():
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))

    if len(numbers) < 2:
        print("!!!Please enter at least two numbers!!!")
        return

    lcm_result = lcm_multiple(numbers)
    print("LCM:", lcm_result)

main()