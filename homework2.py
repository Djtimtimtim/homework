# Задание № 2. Атрибуты и взаимодействие классов.
# В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания.
# Теперь это могут делать только Reviewer (реализуйте такой метод)!
# А что могут делать лекторы? Получать оценки за лекции от студентов :)
# Реализуйте метод выставления оценок лекторам у класса Student (оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer,
# в котором ключи – названия курсов, а значения – списки оценок).
# Лектор при этом должен быть закреплен за тем курсом, на который записан студент.

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

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

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

# Создаем экземпляр студента
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

# Создаем экземпляр лектора
cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

# Создаем экземпляр проверяющего
cool_reviewer = Reviewer('Another', 'Person')
cool_reviewer.courses_attached += ['Python']

# Проверяющий выставляет оценки студенту
cool_reviewer.rate_hw(best_student, 'Python', 9.9)
cool_reviewer.rate_hw(best_student, 'Python', 9.9)
cool_reviewer.rate_hw(best_student, 'Python', 9.9)

# Студент выставляет оценки лектору
best_student.rate_lecturer(cool_lecturer, 'Python', 9.9)
best_student.rate_lecturer(cool_lecturer, 'Python', 9.9)
best_student.rate_lecturer(cool_lecturer, 'Python', 9.9)

# Выводим оценки студента
print(best_student.grades)

# Выводим оценки лектора
print(cool_lecturer.grades)
