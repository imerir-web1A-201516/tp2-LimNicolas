students = [
  {"name": "John", "grades": [{"topic": "French", "mark": 12}, {"topic": "Math", "mark": 16}]},
  {"name": "Jane", "grades": [{"topic": "French", "mark": 18}, {"topic": "Math", "mark": 9}]},
  {"name": "Toto", "grades": [{"topic": "French", "mark": 8}, {"topic": "Math", "mark": 5}]}
]


def get_student_by(name):
    for student in students:
        if student['name'] == name:
            return student

    return None


def get_all_students_names():
    output = []
    for student in students:
        output += [student['name']]
    return output


def get_grades_of_students(name):
    student = get_student_by(name)
    if student is None:
        return 'ERROR: Student cannot be found'

    return student['grades']
