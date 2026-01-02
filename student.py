def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg < 90:
        return "A"
    elif 65 <= avg < 80:
        return "B"
    elif 50 <= avg < 65:
        return "C"
    elif 40 <= avg < 50:
        return "D"
    else:
        return "F"

def print_grade_table():
    print("===== GRADING CRITERIA =====")
    print("+------------+---------+")
    print("| Marks (%)  | Grade   |")
    print("+------------+---------+")
    print("| 90 - 100   |   S     |")
    print("| 80 - 89    |   A     |")
    print("| 65 - 79    |   B     |")
    print("| 50 - 64    |   C     |")
    print("| 40 - 49    |   D     |")
    print("| Below 40   |   F     |")
    print("+------------+---------+")

def main():
    # 🔹 TAKE INPUT FROM USER
    name = input("Enter Student Name: ")
    department = input("Enter Department: ")
    semester = input("Enter Semester: ")

    marks1 = int(input("Enter Marks 1: "))
    marks2 = int(input("Enter Marks 2: "))
    marks3 = int(input("Enter Marks 3: "))

    average = (marks1 + marks2 + marks3) / 3
    grade = calculate_grade(average)

    # ✅ PRINT TABLE FIRST
    print("\n")
    print_grade_table()

    # ✅ THEN PRINT STUDENT DETAILS
    print("\n===== STUDENT DETAILS =====")
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"Semester   : {semester}")
    print(f"Average    : {average:.2f}")
    print(f"Grade      : {grade}")

if __name__ == "__main__":
    main()
