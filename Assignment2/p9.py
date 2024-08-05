def find_second_largest_and_smallest(arr):
    if len(arr) < 2:
        return "Array must have at least two distinct elements."

    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
        
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num > smallest:
            second_smallest = num

    if second_largest == float('-inf'):
        second_largest = "Not available"
    if second_smallest == float('inf'):
        second_smallest = "Not available"
    
    return second_largest, second_smallest
    
def main():
    arr = [12, 45, 23, 67, 34, 89, 23, 45]
    second_largest, second_smallest = find_second_largest_and_smallest(arr)

    print("Second Largest:", second_largest)
    print("Second Smallest:", second_smallest)


main()