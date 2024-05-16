# Задание № 2. Атрибуты и взаимодействие классов.
# В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания.
# Теперь это могут делать только Reviewer (реализуйте такой метод)! А что могут делать лекторы? Получать оценки
# за лекции от студентов :) Реализуйте метод выставления оценок лекторам у класса Student (оценки по 10-балльной шкале,
# хранятся в атрибуте-словаре у Lecturer, в котором ключи – названия курсов, а значения – списки оценок). Лектор при этом
# должен быть закреплен за тем курсом, на который записан студент.


""" Нам нужно добавить метод для выставления оценок студентам в класс Reviewer и метод для выставления оценок лекторам 
в класс Student.

- Добавим метод rate_hw в класс Reviewer, чтобы только проверяющие могли выставлять оценки за домашние задания.
- Добавим метод rate_lecturer в класс Student, чтобы студенты могли выставлять оценки лекторам."""

class Student:
    def __init__(self, name, surname, gender):
        # Инициализация атрибутов студента
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []  # Список завершенных курсов
        self.courses_in_progress = []  # Список курсов в процессе обучения
        self.grades = {}  # Словарь оценок по курсам

    def rate_lecturer(self, lecturer, course, grade):
        # Метод для выставления оценки лектору
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]  # Добавляем оценку к списку оценок
            else:
                lecturer.grades[course] = [grade]  # Создаем новый элемент со списком оценок
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        # Инициализация атрибутов ментора
        self.name = name
        self.surname = surname
        self.courses_attached = []  # Список курсов, закрепленных за ментором

class Lecturer(Mentor):
    def __init__(self, name, surname):
        # Инициализация атрибутов лектора
        super().__init__(name, surname)
        self.grades = {}  # Словарь оценок по курсам

class Reviewer(Mentor):
    def __init__(self, name, surname):
        # Инициализация атрибутов проверяющего
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        # Метод для выставления оценки студенту за домашнюю работу
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]  # Добавляем оценку к списку оценок
            else:
                student.grades[course] = [grade]  # Создаем новый элемент со списком оценок
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
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

# Студент выставляет оценки лектору
best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 8)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)

# Выводим оценки студента и лектора
print(best_student.grades)
print(cool_lecturer.grades)