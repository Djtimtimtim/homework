# Создаем родительский класс "преподаватели" с указанными атрибутами имя, фамилия, закрепленные курсы
class Mentor:
    def __init__(self, name, surname, courses_attached=None):
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached if courses_attached is not None else []  # Такая конструкция необходима
        # для предотвращения изменения объектов при их многократном создании

# Создаем дочерний класс "лекторы", который принимает атрибуты экземпляра с их значением параметра из родительского
# класса "преподаватели"
class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached=None):
        super().__init__(name, surname, courses_attached)
        self.grades = {}  # Словарь для хранения оценок по курсам

# Создаем класс "эксперты, проверяющие домашние задания", который принимает атрибуты экземпляра с их значением параметра
# из родительского класса "преподаватели"
class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached=None):
        super().__init__(name, surname, courses_attached)

    # Метод rate_hw позволяет выставлять оценки студентам за домашние задания.
    # Проверяется, что курс есть в списке курсов, закрепленных за Reviewer, и в списке курсов, которые изучает студент.
    def rate_hw(self, student, course, grade):
        if course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Добавляем класс студенты, как показано в задании №1
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}  # Словарь для хранения оценок по курсам

    # Метод rate_lecturer добавляет возможность студентам выставлять оценки лекторам за лекции
    # Проверяется, что курс есть в списке курсов, которые изучает студент, и в списке курсов,
    # закрепленных за лектором.
    def rate_lecturer(self, lecturer, course, grade):
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

# Создаем экземпляры классов
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

# Reviewer выставляет оценки студенту
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

# Выводим оценки студента
print(best_student.grades)  # Вывод: {'Python': [10, 10, 10]}
