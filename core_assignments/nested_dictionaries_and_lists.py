# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)
students[0]["last_name"] = "Bryant"
print(students)
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
z[0]["y"]= 30
print(z)

# 2. Iterate Through a List of Dictionaries
students = [
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    # for i in some_list:
    #     # print(i)
    #     output = ""
    #     for key, value in i.items():
    #         output += f"{key} - {value}, "
    #     print(output)

    for i in some_list:
        print(f'first_name - {i['first_name']}, last_name - {i['last_name']}')

iterateDictionary(students)

# 3. Get Values From a List of Dictionaries
students = [
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    # for some_list in students:
    #     # print(some_list)
    #     for val in some_list.values():
    #         print(val)
    for i in range(len(some_list)):
        print(some_list[i][key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# 4. Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    # for each in some_dict:
    #     print(len(some_dict[each]), each.upper())
    #     for index in some_dict[each]:
    #         print(index)
    #     # for key, val in some_dict.items():
    #     #     print(len(key), key)
    #     #     print(val)
    
    for key in some_dict.keys():
        print(len(some_dict[key]), key.upper())
        for i in some_dict[key]:
            print(i)
        print()

printInfo(dojo)