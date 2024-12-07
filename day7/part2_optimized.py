import itertools

with open("input.txt", "r") as f:

    calibration_sum = 0
    while line := f.readline():

        result, numbers = line.split(":")
        result = int(result)
        numbers = [int(n) for n in numbers.strip().split()]

        def check_permutation(permutation):
            running_sum = numbers[0]
            for index, operator in enumerate(permutation):
                if operator == "+":
                    running_sum += numbers[index + 1]
                elif operator == "*":
                    running_sum *= numbers[index + 1]
                else:
                    running_sum = int(str(running_sum) + str(numbers[index + 1]))

                if running_sum > result:
                    return False

            if running_sum == result:
                return True
            else:
                return False

        for permutation in itertools.product(["*", "+", "||"], repeat=len(numbers) - 1):
            if check_permutation(permutation):
                calibration_sum += result
                break

    print(calibration_sum)
