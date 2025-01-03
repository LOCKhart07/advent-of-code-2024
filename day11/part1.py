"""AoC_Year2024_Day11_Part1"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"

import math


def get_length_of_digits(num):
    return int(math.floor(math.log10(num))) + 1


def is_even_digits(num):
    if num == 0:
        return False

    if get_length_of_digits(num) % 2 == 0:
        return True
    return False


def split_a_number_in_half(num):
    partition = 10 ** int(get_length_of_digits(num) / 2)
    return [num // partition, num % partition]


def deal_with_zero():
    return [1]


def multiply_by_2024(num):
    return [num * 2024]


def count_len_for_numbers(nums, current_iteration):
    # print(current_iteration, nums)
    # print("---------------", current_iteration, nums)

    len_of_nums = len(nums)
    if current_iteration >= NUMBER_OF_ITERATIONS:
        return len_of_nums

    elif len_of_nums == 1:
        num = nums[0]
        if num == 0:
            # return 1
            return count_len_for_numbers([1], current_iteration + 1)

        if is_even_digits(num):
            # a, b = split_a_number_in_half(num)
            return count_len_for_numbers(
                split_a_number_in_half(num), current_iteration + 1
            )

        return count_len_for_numbers([num * 2024], current_iteration + 1)
    else:
        sums = 0
        for i in nums:
            # print("---------------", current_iteration, i)
            sums += count_len_for_numbers([i], current_iteration)
        return sums


NUMBER_OF_ITERATIONS = 25

with open(INPUT_PATH, "r") as f:
    numbers = [int(i) for i in f.read().strip().split()]
print(numbers)
print()
print(count_len_for_numbers(numbers, 0))
