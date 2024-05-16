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

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values())

    def __str__(self):
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
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values())

    def __str__(self):
        average_grade = self.average_grade()
        return (f"У лекторов: \n"
                f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {average_grade:.1f}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()

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

    def __str__(self):
        return (f"У проверяющих: \n"
                f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")

# Создаем экземпляры студентов
student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('John', 'Doe', 'male')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Введение в программирование']
student2.grades = {'Python': [9.9, 9.9, 9.9]}

# Создаем экземпляры лекторов
lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Jane', 'Smith')
lecturer2.courses_attached += ['Python']
lecturer2.grades = {'Python': [9.9, 9.9, 9.9]}

# Создаем экземпляры проверяющих
reviewer1 = Reviewer('Another', 'Person')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Second', 'Reviewer')
reviewer2.courses_attached += ['Git']

# Проверяющие выставляют оценки студентам
reviewer1.rate_hw(student1, 'Python', 9.9)
reviewer1.rate_hw(student1, 'Python', 9.9)
reviewer1.rate_hw(student1, 'Python', 9.9)

reviewer2.rate_hw(student2, 'Python', 9.9)
reviewer2.rate_hw(student2, 'Python', 9.9)
reviewer2.rate_hw(student2, 'Python', 9.9)

# Студенты выставляют оценки лекторам
student1.rate_lecturer(lecturer1, 'Python', 9.9)
student1.rate_lecturer(lecturer1, 'Python', 9.9)
student1.rate_lecturer(lecturer1, 'Python', 9.9)

student2.rate_lecturer(lecturer2, 'Python', 9.9)
student2.rate_lecturer(lecturer2, 'Python', 9.9)
student2.rate_lecturer(lecturer2, 'Python', 9.9)

# Выводим информацию о проверяющих
print(reviewer1)
print(reviewer2)
print()

# Выводим информацию о лекторах
print(lecturer1)
print(lecturer2)
print()

# Выводим информацию о студентах
print(student1)
print(student2)
print()

print('Сравнение лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания:')

# Сравниваем студентов
print(student1 > student2)
print(student1 < student2)
print()

# Сравниваем лекторов
print(lecturer1 > lecturer2)
print(lecturer1 < lecturer2)
print()

# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def average_student_grade(students, course):
    total_grades = 0
    count_grades = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            count_grades += len(student.grades[course])
    if count_grades == 0:
        return 0
    return total_grades / count_grades

# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def average_lecturer_grade(lecturers, course):
    total_grades = 0
    count_grades = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            count_grades += len(lecturer.grades[course])
    if count_grades == 0:
        return 0
    return total_grades / count_grades

# Пример использования функций
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print(f"Средняя оценка за домашние задания по курсу 'Python': {average_student_grade(students, 'Python'):.1f}")
print(f"Средняя оценка за лекции по курсу 'Python': {average_lecturer_grade(lecturers, 'Python'):.1f}")
