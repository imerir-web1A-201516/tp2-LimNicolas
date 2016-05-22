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


@app.route("/student/<name>/grades")
def student_grades(name):
    try:
        return json.dumps(students.get_grades_of_students(name))
    except ValueError as e:
        return deal_with_error(e)


@app.route("/student/<name>/grades/average")
def student_grades_average(name):
    try:
        return json.dumps(students.get_average_grades_of_student(name))
    except ValueError as e:
        return deal_with_error(e)


@app.route("/topic/<name>/grades")
def topic_grades(name):
    try:
        return json.dumps(students.get_grades_of_topic(name))
    except ValueError as e:
        return deal_with_error(e)


@app.route("/topic/<name>/grades/average")
def topic_grades_average(name):
    try:
        return json.dumps(students.get_average_grades_of_topic(name))
    except ValueError as e:
        return deal_with_error(e)


if __name__ == "__main__":
    app.debug = True
    app.run()
