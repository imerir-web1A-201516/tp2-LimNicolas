import json
import students
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/students/list")
def students_list():
    return json.dumps(students.get_all_names())


if __name__ == "__main__":
    app.debug = True
    app.run()
