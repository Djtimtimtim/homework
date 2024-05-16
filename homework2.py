"""Задание № 2. Атрибуты и взаимодействие классов.
В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания.
Теперь это могут делать только Reviewer (реализуйте такой метод)! А что могут делать лекторы? Получать оценки
за лекции от студентов :) Реализуйте метод выставления оценок лекторам у класса Student (оценки по 10-балльной шкале,
хранятся в атрибуте-словаре у Lecturer, в котором ключи – названия курсов, а значения – списки оценок). Лектор при этом
должен быть закреплен за тем курсом, на который записан студент."""

""" Нам нужно добавить метод для выставления оценок студентам в класс Reviewer и метод для выставления оценок лекторам 
в класс Student.

- Добавим метод rate_hw в класс Reviewer, чтобы только проверяющие могли выставлять оценки за домашние задания.
- Добавим метод rate_lecturer в класс Student, чтобы студенты могли выставлять оценки лекторам."""

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

# Класс Mentor представляет ментора (наставника)
class Mentor:
    def __init__(self, name, surname):
        self.name = name  # Имя ментора
        self.surname = surname  # Фамилия ментора
        self.courses_attached = []  # Список курсов, за которые отвечает ментор

# Класс Lecturer представляет лектора и наследует от класса Mentor
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Оценки за лекции

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
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']  # Добавляем курс, который студент сейчас проходит

# Создаем лектора
cool_lecturer = Lecturer('Cool', 'Lecturer')
cool_lecturer.courses_attached += ['Python']  # Закрепляем курс за лектором

# Создаем проверяющего
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']  # Закрепляем курс за проверяющим

# Проверяющий оценивает домашку студента
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)

# Студент оценивает лектора
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 8)

# Выводим оценки студента и лектора
print(best_student.grades)
print(cool_lecturer.grades)
