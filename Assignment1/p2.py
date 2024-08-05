list1 = [2, 3, 5, 8, 3, 1, 4, 5,1, 9, 0]
print("List 2 consists of the values:", list1)
num = int(input("Enter the search element: ")) 
if num in list1:
    print("Hurrayyy!!! your search element do exist in the list")
else:
    print("Alas!!! your search element does exist in the list")