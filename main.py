# Создаем родительский класс "преподаватели" с указанными атрибутами имя, фамилия, закрепленные курсы
class Mentor:
    def __init__(self, name, surname, courses_attached=None):
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached if courses_attached is not None else []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

# Создаем дочерний класс "лекторы", который принимает атрибуты экземпляра с их значением параметра из родительского
# класса "преподаватели"
class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached=None):
        super().__init__(name, surname, courses_attached)
        self.grades = {}

    def __str__(self):
        average_grade = self._calculate_average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}"

    def _calculate_average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_count if total_count != 0 else 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_average_grade() < other._calculate_average_grade()

# Создаем класс "эксперты, проверяющие домашние задания", который принимает атрибуты экземпляра с их значением параметра
# из родительского класса "преподаватели"
class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached=None):
        super().__init__(name, surname, courses_attached)

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
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        average_grade = self._calculate_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}")

    def _calculate_average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_count if total_count != 0 else 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_average_grade() < other._calculate_average_grade()

# Создаем экземпляры классов
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

# Reviewer выставляет оценки студенту
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

# Выводим информацию о студенте и проверяющем
print(best_student)
print(cool_reviewer)
