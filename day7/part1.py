import itertools

with open("input.txt", "r") as f:

    calibration_sum = 0
    while line := f.readline():
        # print(f"testing:     {line}")
        result, numbers = line.split(":")
        result = int(result)
        numbers = [int(n) for n in numbers.strip().split()]
        # print(f"{result}    {numbers}")

        # possible_permutations = [
        #     i for i in itertools.permutations(["*", "+"], len(numbers) - 1)
        # ]

        possible_permutations = [
            i for i in itertools.product(["*", "+"], repeat=len(numbers) - 1)
        ]
        for permutation in possible_permutations:

            running_sum = numbers[0]
            for index, operator in enumerate(permutation):
                # print(operator)
                if operator == "+":
                    running_sum += numbers[index + 1]
                else:  # *
                    running_sum *= numbers[index + 1]

            # print(permutation, "  |", running_sum, "|     |", result, "|")
            if running_sum == result:
                # print("-----------------------------------")
                calibration_sum += result
                break

        # print(possible_permutations)

    print(calibration_sum)
