import uuid
name = input("Enter your name ")
submission = input("Enter your submission")

class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()  # Generate a unique course ID
        self.course_name = course_name
        self.course_mark = course_mark

class Student:
    total_students = 0  # Static variable to keep track of total student count

    def __init__(self, student_name, student_age, student_number):
        self.student_id = uuid.uuid4()  # Generate a unique student ID
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []  # List to store enrolled courses

    def enroll_course(self, course):
        self.courses_list.append(course)

    def get_student_details(self):
        return self.__dict__

    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course: {course.course_name}, Mark: {course.course_mark}")

    def get_student_average(self):
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list) if len(self.courses_list) > 0 else 0


students_list = []
