# create a program that will ask the users name, age, and reddit username. have it told them the information back,
# in the format: your name is (blank), you are (blank) years old, and your username is (blank) for extra credit,
# have the program log this information in a file to be accessed later.

def display_n_save(name, age, username):
    print(f'Your name is {name}, you are {age} years old, and your username is {username}')
    file = open("user.txt", "w")
    file.write(f'Your name is {name}, you are {age} years old, and your username is {username}')


# name = input("Enter name: ")
# age = input("Enter age: ")
# username = input("Enter username: ")

# display_n_save(name, age, username)


########################################################################################################################

# given a list of numbers, return whether any two sums to k. For example, given [10, 15, 3, 7] and k of 17
# return true since 10 + 7 is 17.

def check_numbers(k, numbers):
    for index, number in enumerate(numbers):
        for number2 in numbers[index + 1:]:
            if number + number2 == k:
                return True

    return False


def another_approach(k, numbers):
    numbers_before = set()

    for number in numbers:
        target = k - number
        if target in numbers_before:
            return True

        numbers_before.add(number)

    return False


numbers = [10, 15, 3, 7]
k = 17
print(check_numbers(k, numbers))
print(another_approach(k, numbers))
