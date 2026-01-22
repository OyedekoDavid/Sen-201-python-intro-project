def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"


def display_result(student_name, score):
    grade = calculate_grade(score)
    print("\n--- Student Result ---")
    print("Name:", student_name)
    print("Score:", score)
    print("Grade:", grade)


# Main Program
student_name = input("Enter student name: ")
score = int(input("Enter student score: "))

display_result(student_name, score)
