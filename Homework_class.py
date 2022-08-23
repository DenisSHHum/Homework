class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    # Средняя оценка студента
    def __average_rate(self):
        self.midl_rate = [grade for grades in self.grades.values() for grade in grades]
        if self.midl_rate:
            self.midl_grade = (sum(self.midl_rate) / len(self.midl_rate))
            return self.midl_grade
        else:
            return ("No grades")

    # Информация о студенте
    def __str__(self):
        return (
            f"Имя : {self.name} \nФамилия : {self.surname} \nСредний балл : {self.__average_rate()} \nИзучаемые курсы :{self.courses_in_progress} \nЗавершенные курсы : {self.finished_courses} ")

    # Сравнение оценок
    def __eq__(self, other):
        if not isinstance(other, Student):
            print("Ошибка")
            return
        elif isinstance(self, Student):
            return self.__average_rate() == other.__average_rate

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Ошибка")
            return
        elif isinstance(self, Student):
            return self.__average_rate() < other.__average_rate

    def __gt__(self, other):
        if not isinstance(other, Student):
            print("Ошибка")
            return
        elif isinstance(self, Student):
            return self.__average_rate() > other.__average_rate


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    # Средняя оценка лектора
    def __average_rate(self):
        self.midl_rate = [grade for grades in self.grades.values() for grade in grades]
        if self.midl_rate:
            self.midl_grade = (sum(self.midl_rate) / len(self.midl_rate))
            return self.midl_grade
        else:
            return ("No grades")

    # Информация о лекторе
    def __str__(self):
        return (
            f"Имя Лектора : {self.name} \nФамилия Лектора : {self.surname} \nСредний балл : {self.__average_rate()}")

    # Сравнение оценок (Лекторов)

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка")
            return
        elif isinstance(self, Lecturer):
            return self.__average_rate() == other.__average_rate

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка")
            return
        elif isinstance(self, Lecturer):
            return self.__average_rate() < other.__average_rate

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка")
            return
        elif isinstance(self, Lecturer):
            return self.__average_rate() > other.__average_rate


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"ФИО проверяющего: {self.name} {self.surname}"


# Список участников

Student_the_first = Student("Игорь", "Орлов", "мужчина")
Student_the_first.courses_in_progress += ["Python", "Java"]
Student_the_first.finished_courses += ["Git"]

Student2 = Student("Юля", "Сергеева", "женщина")
Student2.courses_in_progress += ["Python", "Java"]
Student2.finished_courses += ["Git"]

Reviewer1 = Reviewer("Остап", "Пупкин")
Reviewer1.courses_attached += ["Java", "Python", "Git"]
Reviewer2 = Reviewer("Жан", "Жак")
Reviewer2.courses_attached += ["Java", "Python", "Git"]

Reviewer1.rate_hw(Student2, "Java", 5)
Reviewer1.rate_hw(Student2, "Java", 7)
Reviewer1.rate_hw(Student2, "Java", 9)

Reviewer1.rate_hw(Student_the_first, "Java", 8)
Reviewer1.rate_hw(Student_the_first, "Java", 9)
Reviewer1.rate_hw(Student_the_first, "Java", 8)

Reviewer2.rate_hw(Student2, "Python", 10)
Reviewer2.rate_hw(Student2, "Python", 10)
Reviewer2.rate_hw(Student2, "Python", 10)

Reviewer2.rate_hw(Student_the_first, "Python", 7)
Reviewer2.rate_hw(Student_the_first, "Python", 7)
Reviewer2.rate_hw(Student_the_first, "Python", 6)
Reviewer2.rate_hw(Student_the_first, "Python", 8)
Reviewer2.rate_hw(Student_the_first, "Python", 10)

Lector1 = Lecturer("Владимир", "Федоров")
Lector1.courses_attached += ["Java", "Python"]

Student_the_first.rate_lc(Lector1, "Java", 8)
Student_the_first.rate_lc(Lector1, "Java", 5)
Student_the_first.rate_lc(Lector1, "Java", 6)

Student2.rate_lc(Lector1, "Python", 7)
Student2.rate_lc(Lector1, "Python", 10)
Student2.rate_lc(Lector1, "Python", 9)

Lector2 = Lecturer("Алла", "Борисовна")
Lector2.courses_attached += ["Java", "Python"]

Student_the_first.rate_lc(Lector2, "Java", 6)
Student_the_first.rate_lc(Lector2, "Java", 7)
Student_the_first.rate_lc(Lector2, "Java", 10)

Student2.rate_lc(Lector2, "Python", 7)
Student2.rate_lc(Lector2, "Python", 8)
Student2.rate_lc(Lector2, "Python", 6)

print(f'{Student_the_first} {Student2}')

print(f'{Lector1} {Lector2}')

print(f'{Reviewer1} {Reviewer2}')