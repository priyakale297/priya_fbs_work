li = [10, 20, 60, 40, 50, 60, 70]

element_to_remove = int(input("Enter the element to remove from the list: "))

updated_list = [num for num in li if num != element_to_remove]
print("Original List:", li)
print(f"List after removing all occurrences of {element_to_remove}:", updated_list)
