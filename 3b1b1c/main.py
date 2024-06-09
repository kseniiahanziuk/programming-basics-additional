def process_file():
    students_data = {}
    with open("students.txt", "r") as file:
        for line in file:
            data = line.split()
            name = data[0]
            grades = []
            for grade in data[1:]:
                grades.append(int(grade))
            students_data[name] = grades
    return students_data


def statistics(students_data):
    student_stats = {}
    for name, grades in students_data.items():
        average_grade = sum(grades) / len(grades)
        highest_grade = max(grades)
        lowest_grade = min(grades)
        student_stats[name] = {"Average": average_grade, "Highest grade": highest_grade,
                               "Lowest grade": lowest_grade}

    group_grades = [grade for grades in students_data.values() for grade in grades]
    group_average = sum(group_grades) / len(group_grades)
    highest_overall_grade = max(group_grades)
    lowest_overall_grade = min(group_grades)

    frequency_dictionary = {}
    for grade in group_grades:
        if grade in frequency_dictionary:
            frequency_dictionary[grade] += 1
        else:
            frequency_dictionary[grade] = 1
    max_frequency = max(frequency_dictionary.values())
    mode = ", ".join(str(grade) for grade, frequency in frequency_dictionary.items() if frequency == max_frequency)
    return student_stats, group_average, highest_overall_grade, lowest_overall_grade, mode


def write_stats_to_file(student_stats, group_average, highest_overall_grade, lowest_overall_grade, mode):
    with open("statistics.txt", "w") as file:
        for name, stats in student_stats.items():
            file.write(f"Student: {name}\n"
                       f"Average grade: {stats['Average']}\n"
                       f"Highest grade: {stats['Highest grade']}\n"
                       f"Lowest grade: {stats['Lowest grade']}\n\n"
                       f"_________________________________________\n")

        file.write(f"Group statistics:\n\n"
                   f"Average grade: {group_average}\n"
                   f"Highest grade: {highest_overall_grade}\n"
                   f"Lowest grade: {lowest_overall_grade}\n"
                   f"Mode: {mode}")


def main():
    students_data = process_file()
    student_stats, group_average, highest_overall_grade, lowest_overall_grade, mode = statistics(students_data)
    write_stats_to_file(student_stats, group_average, highest_overall_grade, lowest_overall_grade, mode)


main()
