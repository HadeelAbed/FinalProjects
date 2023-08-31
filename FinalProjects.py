import uuid
name = input("Enter your name ")
submission = input("Enter your submission")

class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()  # Generate a unique course ID
        self.course_name = course_name
        self.course_mark = course_mark

