import json
import students
from flask import Flask
app = Flask(__name__)


def deal_with_error(error):
    return 'ERROR: ' + error.message


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/students/list")
def students_list():
    try:
        return json.dumps(students.get_all_students_names())
    except ValueError as e:
        return deal_with_error(e)


@app.route("/student/<student>/grades")
def student_grades(student):
    try:
        return json.dumps(students.get_grades_of_students(student))
    except ValueError as e:
        return deal_with_error(e)


@app.route("/student/<student>/grades/average")
def student_grades_average(student):
    try:
        return json.dumps(students.get_average_grades_of_student(student))
    except ValueError as e:
        return deal_with_error(e)


if __name__ == "__main__":
    app.debug = True
    app.run()
