class Student:
    def __init__(self, name, surname, gender):
        # Инициализация атрибутов студента
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        # Оценка лектора студентом
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        # Расчет средней оценки студента
        if not self.grades:
            return 0
        return sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values())

    def __str__(self):
        # Строковое представление информации о студенте
        average_grade = self.average_grade()
        in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        return (f"У студентов: \n"
                f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {average_grade:.1f}\n"
                f"Курсы в процессе изучения: {in_progress}\n"
                f"Завершенные курсы: {finished}")

    def __lt__(self, other):
        # Сравнение студентов по средней оценке (меньше)
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        # Сравнение студентов по средней оценке (больше)
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        # Инициализация атрибутов ментора
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        # Инициализация атрибутов лектора
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        # Расчет средней оценки лектора
        if not self.grades:
            return 0
        return sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values())

    def __str__(self):
        # Строковое представление информации о лекторе
        average_grade = self.average_grade()
        return (f"У лекторов: \n"
                f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {average_grade:.1f}")

    def __lt__(self, other):
        # Сравнение лекторов по средней оценке (меньше)
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        # Сравнение лекторов по средней оценке (больше)
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        # Инициализация атрибутов проверяющего
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        # Оценка домашнего задания студенту
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        # Строковое представление информации о проверяющем
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


print('Сравнение лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания:')

# Сравниваем студентов
another_student = Student('John', 'Doe', 'male')
another_student.courses_in_progress += ['Python']
another_student.finished_courses += ['Введение в программирование']
another_student.grades = {'Python': [9.9, 9.9, 9.9]}

print(some_student > another_student)
print(some_student < another_student)

# Сравниваем лекторов
another_lecturer = Lecturer('Jane', 'Smith')
another_lecturer.courses_attached += ['Python']
another_lecturer.grades = {'Python': [9.9, 9.9, 9.9]}

print(some_lecturer > another_lecturer)
print(some_lecturer < another_lecturer)
