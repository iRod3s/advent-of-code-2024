import re
import operator

def first_part(input: str) -> int:
    operations: list[str] = re.findall(r"mul\([0-9]+\,[0-9]+\)", input)
    accum = 0
    for operation in operations:
        op1, op2 = operation.removeprefix("mul(").removesuffix(")").split(",")
        accum += (int(op1) * int(op2))

    return accum

def second_part(input: str) -> int:

    do_indexes = [{"type":"do", "value": x.start()} for x in re.finditer(r"do\(\)", input)]
    dont_indexes = [{"type": "dont", "value": x.start()} for x in re.finditer(r"don't\(\)", input)]

    merged_indexes = []
    merged_indexes.extend(do_indexes)
    merged_indexes.extend(dont_indexes)
    sorted_indexes = sorted(merged_indexes, key=operator.itemgetter('value'))

    valid_sections: list[str] = []

    start_pos = 0
    is_active = True

    for index in sorted_indexes:
        if is_active:
            if index["type"] == "dont":
                valid_sections.append(input[start_pos:index["value"]])
                start_pos = index["value"]
                is_active = False
        else:
            if index["type"] == "do":
                start_pos = index["value"]
                is_active = True

    if is_active:
        valid_sections.append(input[start_pos:len(input)])

    curated_input = "".join(valid_sections)

    return first_part(input=curated_input)


if __name__ == "__main__":
    reports = []
    with open("input.txt", "r") as input:
        s = input.read()

    print(first_part(input=s))
    print(second_part(input=s))
