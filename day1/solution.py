def first_part(first_list: list[int], second_list: list[int]) -> int:
    accum = 0
    first_list.sort()
    second_list.sort()

    for i in range(len(first_list)):
        accum += abs(first_list[i] - second_list[i]) 

    return accum

def second_part(first_list: list[int], second_list: list[int]) -> int:
    occurences_dict = dict()

    for element in second_list:
        if element in occurences_dict:
            occurences_dict[element] = occurences_dict[element] + 1
        else:
            occurences_dict[element] = 1

    accum = 0

    for element in first_list:
        if element in occurences_dict:
            accum += element * occurences_dict[element]

    return accum

if __name__ == "__main__":
    first_list = []
    second_list = []
    with open("input.txt", "r") as input:
        for line in input.readlines():
            e1, e2 = line.split(" ", 1)
            first_list.append(int(e1))
            second_list.append(int(e2))

    print(first_part(first_list=first_list, second_list=second_list))
    print(second_part(first_list=first_list, second_list=second_list))