
def bubble(input_list):
    for e in range(0, len(input_list)):

        for i in range(0, len(input_list)):
            if i < len(input_list) - 1 and input_list[i + 1] < input_list[i]:
                storage_var = input_list[i + 1]
                input_list[i+1] = input_list[i]
                input_list[i] = storage_var

    return input_list    


# print([5, 87, 3, 325, 2, 53, 23, 1, 63, 32, 12, 63, 23, 632])
# print(bubble([5, 87, 3, 325, 2, 53, 23, 1, 63, 32, 12, 63, 23, 632]))
# print("\n")

# print([89, 59, 296, 6, 294, 49, 271, 228, 281, 135, 8, 175, 122, 190, 184])
# print(bubble([89, 59, 296, 6, 294, 49, 271, 228, 281, 135, 8, 175, 122, 190, 184]))
# print("\n")

# print([89, 59, 296, 6, 294, 49, 271, 228, 281, 135, 8, 175, 122, 190, 184, ])
# print(bubble([89, 59, 296, 6, 294, 49, 271, 228, 281, 135, 8, 175, 122, 190, 184]))
# print("\n")

# print([12, 252, 158, 111, 82, 124, 167, 116, 197, 66, 129, 249, 134, 74, 274])
# print(bubble([12, 252, 158, 111, 82, 124, 167, 116, 197, 66, 129, 249, 134, 74, 274]))
# print("\n")

# print([12, 252, 158, 111, 82, 124, 167, 116, 197, 66, 129, 249, 134, 74, 274, ])
# print(bubble([12, 252, 158, 111, 82, 124, 167, 116, 197, 66, 129, 249, 134, 74, 274, ]))
# print("\n")
