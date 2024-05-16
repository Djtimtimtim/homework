# Задание № 3. Полиморфизм и магические методы
#
# 1. Перегрузите магический метод str у всех классов.
#
# У проверяющих он должен выводить информацию в следующем виде:
# print(some_reviewer)
# Имя: Some
# Фамилия: Buddy
#
# У лекторов:
# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9
#
# А у студентов так:
# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование
#
# 2. Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и
# студентов по средней оценке за домашние задания.


"""Нам нужно перегрузить магический метод __str__ у всех классов (Student, Lecturer, Reviewer) и реализовать 
возможность сравнения студентов и лекторов по средней оценке.

Перегрузим метод __str__ для всех классов.
Реализуем методы для вычисления средней оценки.
Добавим методы сравнения для студентов и лекторов.

"""

# Класс Student представляет студента
class Student:
    def __init__(self, name, surname, gender):
        self.name = name  # Имя студента
        self.surname = surname  # Фамилия студента
        self.gender = gender  # Пол студента
        self.finished_courses = []  # Список завершенных курсов
        self.courses_in_progress = []  # Список курсов, которые студент сейчас проходит
        self.grades = {}  # Оценки по курсам

    # Метод для выставления оценок лекторам
    def rate_lecturer(self, lecturer, course, grade):
        # Проверяем, что lecturer - это лектор, курс в процессе у студента и закреплен за лектором
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]  # Добавляем оценку к уже существующим
            else:
                lecturer.grades[course] = [grade]  # Создаем новый список оценок для курса
        else:
            return 'Ошибка'  # Возвращаем ошибку, если что-то не так

    # Метод для вычисления средней оценки за домашние задания
    def get_average_grade(self):
        total_grades = sum([sum(grades) for grades in self.grades.values()])
        total_count = sum([len(grades) for grades in self.grades.values()])
        return total_grades / total_count if total_count != 0 else 0

    # Перегружаем магический метод __str__
    def __str__(self):
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.get_average_grade():.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

    # Перегружаем операторы сравнения
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() == other.get_average_grade()

# Класс Mentor представляет ментора (наставника)
class Mentor:
    def __init__(self, name, surname):
        self.name = name  # Имя ментора
        self.surname = surname  # Фамилия ментора
        self.courses_attached = []  # Список курсов, за которые отвечает ментор

    # Перегружаем магический метод __str__
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

# Класс Lecturer представляет лектора и наследует от класса Mentor
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Оценки за лекции

    # Метод для вычисления средней оценки за лекции
    def get_average_grade(self):
        total_grades = sum([sum(grades) for grades in self.grades.values()])
        total_count = sum([len(grades) for grades in self.grades.values()])
        return total_grades / total_count if total_count != 0 else 0

    # Перегружаем магический метод __str__
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.get_average_grade():.1f}")

    # Перегружаем операторы сравнения
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() == other.get_average_grade()

# Класс Reviewer представляет проверяющего и наследует от класса Mentor
class Reviewer(Mentor):
    # Метод для оценки домашки студента
    def rate_hw(self, student, course, grade):
        # Проверяем, что student - это студент, курс есть у ментора и студент его проходит
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]  # Добавляем оценку к уже существующим
            else:
                student.grades[course] = [grade]  # Создаем новый список оценок для курса
        else:
            return 'Ошибка'  # Возвращаем ошибку, если что-то не так

# Создаем студента
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']  # Добавляем курс, который студент сейчас проходит
some_student.finished_courses += ['Введение в программирование']  # Добавляем завершенный курс

# Создаем лектора
some_lecturer = Lecturer('Cool', 'Lecturer')
some_lecturer.courses_attached += ['Python']  # Закрепляем курс за лектором

# Создаем проверяющего
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']  # Закрепляем курс за проверяющим

# Проверяющий оценивает домашку студента
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 8)

# Студент оценивает лектора
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 9)
some_student.rate_lecturer(some_lecturer, 'Python', 8)

# Выводим информацию о студенте, лекторе и проверяющем
print(some_student)
print(some_lecturer)
print(some_reviewer)

# Сравниваем студентов и лекторов
another_student = Student('John', 'Doe', 'male')
another_student.courses_in_progress += ['Python']
another_student.finished_courses += ['Введение в программирование']
some_reviewer.rate_hw(another_student, 'Python', 7)
some_reviewer.rate_hw(another_student, 'Python', 6)
some_reviewer.rate_hw(another_student, 'Python', 5)

print(some_student > another_student)  # True, если средняя оценка best_student выше
print(some_lecturer == some_lecturer)  # True, если средние оценки равны




