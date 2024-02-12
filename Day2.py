# Given an array of integers, return a new array such that each element at index i of the new array is the product of
# all the numbers in the original array except the one at i
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

import numpy as np


def table_multiplier(numbers):
    multiplied_value = 1
    for num in numbers:
        multiplied_value *= num
    new_table = [multiplied_value / x for x in numbers]
    return new_table


def table_multiplier_numpy(nums):
    product = np.prod(nums)
    new_array = np.full_like(nums, product)
    new_array = new_array / nums
    return new_array


def without_division(numeros):
    length = len(numeros)
    new_list = [1 for _ in numeros]
    product = 1
    for i in range(length):
        new_list[i] *= product
        product *= numeros[i]
    product = 1
    for i in range(length - 1, -1, -1):
        new_list[i] *= product
        product *= numeros[i]
    return new_list


numbers = [1, 2, 3, 4, 5]
numbers2 = [3, 2, 1]
print(table_multiplier(numbers))
print(table_multiplier(numbers2))

num_array = np.array([1, 2, 3, 4, 5])
num_array_2 = np.array([3, 2, 1])
print(table_multiplier_numpy(num_array))
print(table_multiplier_numpy(num_array_2))

print(without_division(numbers))
print(without_division(numbers2))
