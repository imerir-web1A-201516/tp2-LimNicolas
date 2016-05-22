students = [
  {"name": "John", "grades": [{"topic": "French", "mark": 12}, {"topic": "Math", "mark": 16}]},
  {"name": "Jane", "grades": [{"topic": "French", "mark": 18}, {"topic": "Math", "mark": 9}]},
  {"name": "Toto", "grades": [{"topic": "French", "mark": 8}, {"topic": "Math", "mark": 5}]}
]


def get_student_by(name):
    for student in students:
        if student['name'] == name:
            return student

    raise ValueError('Student cannot be found')


def get_all_students_names():
    output = []
    for student in students:
        output += [student['name']]
    return output


def get_grades_of_students(name):
    return get_student_by(name)['grades']


def get_average_grades_of_student(name):
    student_grades = get_grades_of_students(name)
    if len(student_grades) == 0:
        raise ValueError('Student has no grades')

    grades_count = len(student_grades)
    grades_sum = 0.0
    for grade in student_grades:
        grades_sum += grade['mark']

    return grades_sum / grades_count
