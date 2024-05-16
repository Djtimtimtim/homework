# Задание № 1. Наследование
# Исходя из квиза к предыдущему занятию, у нас уже есть класс преподавателей и класс студентов
# (вы можете взять этот код за основу или написать свой). Студентов пока оставим без изменения,
# а вот преподаватели бывают разные, поэтому теперь класс Mentor должен стать родительским классом,
# а от него нужно реализовать наследование классов Lecturer (лекторы) и Reviewer
# (эксперты, проверяющие домашние задания). Очевидно, имя, фамилия и список закрепленных
# курсов логично реализовать на уровне родительского класса. А чем же будут специфичны дочерние классы?
# Об этом в следующих заданиях.

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        # Проверяем, что студент является экземпляром класса Student, курс есть в списке курсов у преподавателя
        # и курс есть в списке текущих курсов у студента
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            # Если курс уже есть в словаре оценок студента, добавляем оценку к списку
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                # Если курса нет в словаре оценок, создаем новый элемент со списком оценок
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
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

# Выводим оценки студента
print(best_student.grades)