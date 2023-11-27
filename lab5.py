"""
Making Class Student
"""
class Student:
    """
    Class Студент
    """
    def __init__(self, name, surname, rating):
        """
        Short info about student
        """
        self.name = name
        self.surname = surname
        self.rating = rating
        self.points = {}

    def __repr__(self):
        """
        returns "Student"
        """
        return "Student"

    def add_to_points(self, **kwargs):
        """
        Adds subject and his mark for student
        """
        for subject, point in kwargs.items():
            self.points[subject] = point

    def average_point(self):
        """
        calculates Average point of all Marks
        """
        values = len(self.points)
        if values == 0:
            return 0
        total = sum(self.points.values())
        average_score = total / values
        return average_score

    def get_info(self):
        """
        Prints all student`s info
        """
        print(f"Name - {self.name} ")
        print(f"Surname - {self.surname} ")
        print(f"Rating - {self.rating}")
        print(f"Points - {self.points}")


class Group:
    """
    Gruop of Students
    """
    def __init__(self, students):
        """
        Group list 
        """
        self.students = []
        self.student = students
    def add_student(self, student):
        """
        Method adds student
        """
        if isinstance(student, Student):
            self.students.append(student)
        else:
            print("This is not a student")
    def remove_student(self,student):
        """
        Method removes student
        """
        if student in self.students:
            self.students.remove(student)
            print(f"{student} where removed from the group.")

    def get_students(self):
        """
        Show all students in group
        """
        students = []
        for element in self.students:
            students.append(element.get_info())
        return students

student_1 = Student("Andrew", "Bringe", 54)
student_1.add_to_points(Math = 8, IT = 11, English = 9)
average = student_1.average_point()

student_2 = Student("Tim", "Johns", 82)
student_2.add_to_points(Math = 7, IT = 9, English = 8)

group = Group([])
group.add_student(student_1)
group.add_student(student_2)



print("----------")
print(f"average point  - {average}")
print("----------")
print(group.get_students())
print("----------")


print(group.remove_student(student_2) )
print(group.get_students())

print(group.remove_student(student_2) )
print(group.get_students())
