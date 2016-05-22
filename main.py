import json
import students
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/students/list")
def students_list():
    return json.dumps(students.get_all_students_names())


@app.route("/student/<student>/grades")
def student_grades(student):
    return json.dumps(students.get_grades_of_students(student))


if __name__ == "__main__":
    app.debug = True
    app.run()
