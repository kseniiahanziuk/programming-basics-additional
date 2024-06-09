def process_file():
    students_data = {}
    with open("students.txt", "r") as file:
        for line in file:
            name, grade = line.split()
            students_data[name] = int(grade)
    return students_data


def statistics(students_data):
    group_average = sum(students_data.values()) / len(students_data)
    highest_grade = max(students_data.values())
    lowest_grade = min(students_data.values())

    frequency_dictionary = {}
    for grade in students_data.values():
        if grade in frequency_dictionary:
            frequency_dictionary[grade] += 1
        else:
            frequency_dictionary[grade] = 1
    max_frequency = max(frequency_dictionary.values())
    mode = ", ".join(str(grade) for grade, frequency in frequency_dictionary.items() if frequency == max_frequency)
    return group_average, highest_grade, lowest_grade, mode


def write_stats_to_file(group_average, highest_grade, lowest_grade, mode):
    with open("statistics.txt", "w") as file:
        file.write(f"Average grade: {group_average}\n"
                   f"Highest grade: {highest_grade}\n"
                   f"Lowest grade: {lowest_grade}\n"
                   f"Mode: {mode}")


def main():
    students_data = process_file()
    group_average, highest_grade, lowest_grade, mode = statistics(students_data)
    write_stats_to_file(group_average, highest_grade, lowest_grade, mode)


main()
