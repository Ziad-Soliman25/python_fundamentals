# 1. Countdown
def countdown(num):
    empty_list = []
    for i in range(num, -1, -1):
        empty_list.append(i)
    # print(empty_list)
    return empty_list

print(countdown(5))

# 2. Print and Return
def print_and_return(list):
    print(list[0])
    return(list[1])

print(print_and_return([1,2]))

# 3. First Plus Length
def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))

# 4. Values Greater than Second
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    new_list = []
    count = 0
    for i in range(len(list)):
        if list[i] > list[1]:
            new_list.append(list[i])
            count += 1
    print(count)
    return new_list

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# 5. This Length, That Value
def length_and_value(num1, num2):
    list = []
    for i in range(num1):
        list.append(num2)
    return list

print(length_and_value(4,7))
print(length_and_value(6,2))
