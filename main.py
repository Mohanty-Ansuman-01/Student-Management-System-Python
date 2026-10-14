class InvalidStudentIDError(Exception):
    pass
class InvalidMarksError(Exception):
    pass
class AttendanceShortageError(Exception):
    pass
class DuplicateStudentError(Exception):
    pass
class Student:
    def __init__(self):
        self.students = {}
    def register_student(self):
        try:
            student_id = input("Enter Student ID (Example: STU101): ")
            name = input("Enter Student Name: ")
            if not student_id.startswith("STU") or len(student_id) <= 3:
                raise InvalidStudentIDError("Invalid Student ID! ID must start with STU")
            if student_id in self.students:
                raise DuplicateStudentError("Student ID already exists!")
            if name.strip() == "":
                print("Student name cannot be empty!")
                return
        except InvalidStudentIDError as e:
            print(e)
        except DuplicateStudentError as e:
            print(e)
        else:
            self.students[student_id] = {"name": name,"marks": None,"attendance": None,"grade": None}
            print("Student registered successfully!")
    def enter_marks(self):
        try:
            student_id = input("Enter Student ID: ")
            if student_id not in self.students:
                raise InvalidStudentIDError("Invalid Student ID! Student not found!")
            marks = float(input("Enter Student Marks (0-100): "))
            if marks < 0 or marks > 100:
                raise InvalidMarksError("Invalid Marks! Marks must be between 0 and 100")
        except ValueError:
            print("Please enter valid marks!")
        except InvalidStudentIDError as e:
            print(e)
        except InvalidMarksError as e:
            print(e)
        else:
            self.students[student_id]["marks"] = marks
            print("Marks entered successfully!")
    def calculate_grade(self):
        try:
            student_id = input("Enter Student ID: ")
            if student_id not in self.students:
                raise InvalidStudentIDError("Invalid Student ID! Student not found!")
            marks = self.students[student_id]["marks"]
            if marks is None:
                print("Please enter marks first!")
                return
            if marks >= 90:
                grade = "A+"
            elif marks >= 80:
                grade = "A"
            elif marks >= 70:
                grade = "B"
            elif marks >= 60:
                grade = "C"
            elif marks >= 50:
                grade = "D"
            else:
                grade = "F"
        except InvalidStudentIDError as e:
            print(e)
        else:
            self.students[student_id]["grade"] = grade
            print("Student Grade:", grade)
    def check_attendance(self):
        try:
            student_id = input("Enter Student ID: ")
            if student_id not in self.students:
                raise InvalidStudentIDError("Invalid Student ID! Student not found!")
            attendance = float(input("Enter Attendance Percentage: "))
            if attendance < 0 or attendance > 100:
                print("Attendance must be between 0 and 100!")
                return
            self.students[student_id]["attendance"] = attendance
            if attendance < 75:
                raise AttendanceShortageError("Attendance shortage! Minimum 75% attendance required.")
        except ValueError:
            print("Please enter valid attendance!")
        except InvalidStudentIDError as e:
            print(e)
        except AttendanceShortageError as e:
            print(e)
        else:
            print("Attendance is sufficient!")
    def student_report(self):
        try:
            student_id = input("Enter Student ID: ")
            if student_id not in self.students:
                raise InvalidStudentIDError("Invalid Student ID! Student not found!")
        except InvalidStudentIDError as e:
            print(e)
        else:
            details = self.students[student_id]
            print("\n------ STUDENT REPORT CARD ------")
            print("Student ID:", student_id)
            print("Student Name:", details["name"])
            print("Marks:", details["marks"])
            print("Grade:", details["grade"])
            print("Attendance:", details["attendance"])
            if details["attendance"] is None:
                print("Attendance Status: Not Updated")
            elif details["attendance"] < 75:
                print("Attendance Status: Shortage")
            else:
                print("Attendance Status: Sufficient")
    def all_student_reports(self):
        print("\n------ ALL STUDENT REPORT CARDS ------")
        if self.students == {}:
            print("No students registered!")
        else:
            for student_id, details in self.students.items():
                print("\n------------------------------")
                print("Student ID:", student_id)
                print("Student Name:", details["name"])
                print("Marks:", details["marks"])
                print("Grade:", details["grade"])
                print("Attendance:", details["attendance"])
                if details["attendance"] is None:
                    print("Attendance Status: Not Updated")
                elif details["attendance"] < 75:
                    print("Attendance Status: Shortage")
                else:
                    print("Attendance Status: Sufficient")
                print("------------------------------")
# Create Student Object
s1 = Student()
while True:
    print("\n------ STUDENT MANAGEMENT SYSTEM ------")
    print("1. Register Student")
    print("2. Enter Marks")
    print("3. Calculate Grade")
    print("4. Check Attendance")
    print("5. Student Report Card")
    print("6. All Student Reports")
    print("7. Exit")
    try:
        choice = int(input("Enter your choice (1-7): "))
        if choice == 1:
            s1.register_student()
        elif choice == 2:
            s1.enter_marks()
        elif choice == 3:
            s1.calculate_grade()
        elif choice == 4:
            s1.check_attendance()
        elif choice == 5:
            s1.student_report()
        elif choice == 6:
            s1.all_student_reports()
        elif choice == 7:
            s1.all_student_reports()
            print("Thank you for using Ansu Student Management System!")
            break
        else:
            print("Invalid choice! Please try again.")
    except ValueError:
        print("Please enter a valid number!")