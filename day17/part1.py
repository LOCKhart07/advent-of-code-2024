"""AoC_Year2024_Day17_Part1"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"

import re

pattern = r"[A-Z]\w+ (\w): (\d+)"


register_hm = {}
with open(INPUT_PATH, "r") as f:
    while line := f.readline().strip():
        # print(line)
        register, value = re.findall(pattern, line)[0]
        register_hm[register] = int(value)
        # print(register, value)

    while line := f.readline().strip():
        # print(line)
        instructions = [int(i) for i in line.removeprefix("Program: ").split(",")]
        # print(numbers)
        # register, value = re.findall(pattern, line)[0]
        # value = int(value)
        # print(register, value)


def get_value_of_operand(operand, is_literal):
    if is_literal == "literal":
        return operand
    return {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: register_hm["A"],
        5: register_hm["B"],
        6: register_hm["C"],
        7: ValueError,
    }[operand]


OUT = []


def perform_instruction(instruction, operand):

    def adv(o):
        global instruction_pointer
        global register_hm
        instruction_pointer = instruction_pointer + 2
        register_hm["A"] = int(register_hm["A"] / 2 ** get_value_of_operand(o, "combo"))

    def bxl(o):
        global instruction_pointer
        global register_hm
        instruction_pointer = instruction_pointer + 2
        register_hm["B"] = register_hm["B"] ^ get_value_of_operand(o, "literal")

    def bst(o):
        global instruction_pointer
        global register_hm
        instruction_pointer = instruction_pointer + 2
        register_hm["B"] = get_value_of_operand(o, "combo") % 8

    def jnz(o):
        global instruction_pointer
        global register_hm
        # print("trying to jump:", register_hm["A"], get_value_of_operand(o, "literal"))
        if register_hm["A"] == 0:
            instruction_pointer = instruction_pointer + 2
        else:
            instruction_pointer = get_value_of_operand(o, "literal")

    def bxc(o):
        global instruction_pointer
        global register_hm
        instruction_pointer = instruction_pointer + 2
        register_hm["B"] = register_hm["B"] ^ register_hm["C"]

    def out(o):
        global instruction_pointer
        global register_hm
        instruction_pointer = instruction_pointer + 2
        # print("outointg")
        OUT.append(str(get_value_of_operand(o, "combo") % 8))

    def bdv(o):
        global instruction_pointer
        global register_hm
        instruction_pointer = instruction_pointer + 2
        register_hm["B"] = int(register_hm["A"] / 2 ** get_value_of_operand(o, "combo"))

    def cdv(o):
        global instruction_pointer
        global register_hm
        instruction_pointer = instruction_pointer + 2
        register_hm["C"] = int(register_hm["A"] / 2 ** get_value_of_operand(o, "combo"))

    INSTRUCTION_HM = {
        0: adv,
        1: bxl,
        2: bst,
        3: jnz,
        4: bxc,
        5: out,
        6: bdv,
        7: cdv,
    }

    INSTRUCTION_HM[instruction](operand)


instruction_pointer = 0

import time

# print(register_hm)
# print(instructions)

while instruction_pointer < len(instructions):
    # print(instructions[instruction_pointer])
    # print(
    #     instruction_pointer,
    #     instructions[instruction_pointer],
    #     instructions[instruction_pointer + 1],
    # )
    perform_instruction(
        instructions[instruction_pointer], instructions[instruction_pointer + 1]
    )
    # time.sleep(1)

",".join(OUT)
