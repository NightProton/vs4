def print_positive(input_list):
    positive = [num for num in input_list if num > 0]
    print(positive)

list1 = [12, -7, 5, 64, -14]
print("Input:", list1, "Output:", end=" ")
print_positive(list1)

list2 = [12, 14, -95, 3]
print("Input:", list2, "Output:", end=" ")
print_positive(list2)
