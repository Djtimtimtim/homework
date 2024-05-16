"""Задание № 1. Наследование
Исходя из квиза к предыдущему занятию, у нас уже есть класс преподавателей и класс студентов
(вы можете взять этот код за основу или написать свой). Студентов пока оставим без изменения, а вот преподаватели
бывают разные, поэтому теперь класс Mentor должен стать родительским классом, а от него нужно реализовать наследование
классов Lecturer (лекторы) и Reviewer (эксперты, проверяющие домашние задания). Очевидно, имя, фамилия и список
закрепленных курсов логично реализовать на уровне родительского класса. А чем же будут специфичны дочерние классы?
Об этом в следующих заданиях."""

"""Нам нужно создать два новых класса Lecturer и Reviewer, которые будут наследовать от класса Mentor."""

# Класс Student представляет студента
class Student:
    def __init__(self, name, surname, gender):
        self.name = name  # Имя студента
        self.surname = surname  # Фамилия студента
        self.gender = gender  # Пол студента
        self.finished_courses = []  # Список завершенных курсов
        self.courses_in_progress = []  # Список курсов, которые студент сейчас проходит
        self.grades = {}  # Оценки по курсам

# Класс Mentor представляет ментора (наставника)
class Mentor:
    def __init__(self, name, surname):
        self.name = name  # Имя ментора
        self.surname = surname  # Фамилия ментора
        self.courses_attached = []  # Список курсов, за которые отвечает ментор

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

# Класс Lecturer представляет лектора и наследует от класса Mentor
class Lecturer(Mentor):
    pass  # Пока что ничего нового не добавляем

# Класс Reviewer представляет проверяющего и наследует от класса Mentor
class Reviewer(Mentor):
    pass  # Пока что ничего нового не добавляем

# Создаем студента
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']  # Добавляем курс, который студент сейчас проходит

# Создаем ментора
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']  # Закрепляем курс за ментором

# Ментор оценивает домашку студента
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

# Выводим оценки студента
print(best_student.grades)
