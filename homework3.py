class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        average_grade = sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values())
        in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        return (f"У студентов: \n"
                f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {average_grade:.1f}\n"
                f"Курсы в процессе изучения: {in_progress}\n"
                f"Завершенные курсы: {finished}")

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        average_grade = sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values())
        return (f"У лекторов: \n"
                f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {average_grade:.1f}")

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"У проверяющих: \n"
                f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")


# Создаем экземпляр студента
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

# Создаем экземпляр лектора
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

# Создаем экземпляр проверяющего
some_reviewer = Reviewer('Another', 'Person')
some_reviewer.courses_attached += ['Python']

# Проверяющий выставляет оценки студенту
some_reviewer.rate_hw(some_student, 'Python', 9.9)
some_reviewer.rate_hw(some_student, 'Python', 9.9)
some_reviewer.rate_hw(some_student, 'Python', 9.9)

# Студент выставляет оценки лектору
some_student.rate_lecturer(some_lecturer, 'Python', 9.9)
some_student.rate_lecturer(some_lecturer, 'Python', 9.9)
some_student.rate_lecturer(some_lecturer, 'Python', 9.9)

# Выводим информацию о проверяющем
print(some_reviewer)
print()

# Выводим информацию о лекторе
print(some_lecturer)
print()

# Выводим информацию о студенте
print(some_student)
print()
