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
    student_grades = get_student_by(name)['grades']
    if len(student_grades) == 0:
        raise ValueError('Student has no grades')

    return student_grades


def get_grades_of_topic(name):
    grades = []
    for student in students:
        for grade in student['grades']:
            if grade['topic'] == name:
                grades += [grade]

    if len(grades) == 0:
        raise ValueError('Topic has no grades')

    return grades


def generate_average_of_grades(grades):
    grades_count = len(grades)
    grades_sum = 0.0
    for grade in grades:
        grades_sum += grade['mark']

    return grades_sum / grades_count


def get_average_grades_of_student(name):
    student_grades = get_grades_of_students(name)
    return generate_average_of_grades(student_grades)


def get_average_grades_of_topic(name):
    topic_grades = get_grades_of_topic(name)
    return generate_average_of_grades(topic_grades)
