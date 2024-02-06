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