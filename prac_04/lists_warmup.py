
# numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = [3, 1, 4, 1, 5, 9]
# numbers[3:4] = [1]
# 5 in numbers = true
# 7 in numbers = false
# "3" in numbers = false
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[-1] = 1
numbers[0] = 'ten'
print(numbers[2:])

if 9 in numbers:
    print("9 is in numbers!")