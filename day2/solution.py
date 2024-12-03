def check_report(report: list[int], deep=False) -> bool:
    if report[0] < report[1]:
        asc = True
    elif report[0] > report[1]:
        asc = False
    else:
        if deep:
            return False
        else:
            new_report = report.copy()
            new_report.pop(0)
            return check_report(new_report, deep=True)

    for i in range(len(report) - 1):
        d = abs(report[i] - report[i + 1])
        if d > 3 or d == 0:
            if deep:
                return False
            else:
                new_report = report.copy()
                new_report.pop(i)
                return check_report(new_report, deep=True)
        if asc:
            if report[i] > report[i + 1]:
                if deep:
                    return False
                else:
                    new_report = report.copy()
                    new_report.pop(i)
                    return check_report(new_report, deep=True)
        else:
            if report[i] < report[i + 1]:
                if deep:
                    return False
                else:
                    new_report = report.copy()
                    new_report.pop(i)
                    return check_report(new_report, deep=True)
        return True


def first_part(reports: list[list[int]]) -> int:
    accum = 0
    for report in reports:
        if check_report(report):
            print(report)
            accum += 1

    return accum


if __name__ == "__main__":
    reports = []
    with open("input.txt", "r") as input:
        for line in input.readlines():
            report = []
            for number in line.split(" "):
                report.append(int(number))
            reports.append(report)

    print(first_part(reports=reports))
    # print(second_part(first_list=first_list, second_list=second_list))
