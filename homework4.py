""""Задание № 4. Полевые испытания
Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:

для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
(в качестве аргументов принимаем список студентов и название курса);
для подсчета средней оценки за лекции всех лекторов в рамках курса
(в качестве аргумента принимаем список лекторов и название курса)."""

"""нам нужно создать по два экземпляра каждого класса, вызвать все созданные методы и реализовать две функции 
для подсчета средней оценки за домашние задания и лекции.

Создадим по два экземпляра каждого класса.
Вызовем все методы для этих экземпляров.
Реализуем функции для подсчета средней оценки за домашние задания и лекции."""

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

    # Перегружаем магический метод __str__
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def average_student_grade(students, course):
    total_grades = 0
    total_count = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_count += len(student.grades[course])
    return total_grades / total_count if total_count != 0 else 0

# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def average_lecturer_grade(lecturers, course):
    total_grades = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            total_count += len(lecturer.grades[course])
    return total_grades / total_count if total_count != 0 else 0

# Создаем студентов
student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Введение в программирование']

student2 = Student('John', 'Doe', 'male')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Введение в программирование']

# Создаем лекторов
lecturer1 = Lecturer('Cool', 'Lecturer')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Awesome', 'Lecturer')
lecturer2.courses_attached += ['Python']

# Создаем проверяющих
reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Another', 'Reviewer')
reviewer2.courses_attached += ['Python']

# Проверяющие оценивают домашку студентов
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)

reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 6)
reviewer2.rate_hw(student2, 'Python', 5)

# Студенты оценивают лекторов
student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 8)

student2.rate_lecturer(lecturer2, 'Python', 7)
student2.rate_lecturer(lecturer2, 'Python', 6)
student2.rate_lecturer(lecturer2, 'Python', 5)

# Выводим информацию о студентах, лекторах и проверяющих
print("Информация о студентах:")
print(student1)
print(student2)

print("\nИнформация о лекторах:")
print(lecturer1)
print(lecturer2)

print("\nИнформация о проверяющих:")
print(reviewer1)
print(reviewer2)

# Подсчитываем средние оценки
average_student_python = average_student_grade([student1, student2], 'Python')
average_lecturer_python = average_lecturer_grade([lecturer1, lecturer2], 'Python')

print(f"\nСредняя оценка за домашние задания по курсу Python: {average_student_python:.1f}")
print(f"Средняя оценка за лекции по курсу Python: {average_lecturer_python:.1f}")
