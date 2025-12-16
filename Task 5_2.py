numbers_list = []
for number in range(1, 11):
    numbers_list.append(number)
print(f"Original list: {numbers_list}")

first_five = numbers_list[0:5]
print(f"Extracted first five elements: {first_five}")

reversed_list = first_five[::-1]
print(f"Reversed extracted elements: {reversed_list}")