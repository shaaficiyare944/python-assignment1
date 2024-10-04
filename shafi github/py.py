class Student:
    def __init__(self, student_name, registration_number):  
        self.student_name = student_name
        self.registration_number = registration_number

    def display_student_info(self):
        print(f"Student Name: {self.student_name}")  
        print(f"Registration Number: {self.registration_number}")


student1 = Student("John Doe", "20240101")
student2 = Student("Jane Smith", "20240202")
student3 = Student("Alice Johnson", "20240303")
student4 = Student("Bob Brown", "20240404")


student1.display_student_info()
student2.display_student_info()
student3.display_student_info()
student4.display_student_info()
