from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask import session
import sys
import sqlite3

from helperfunctions.create_logger import create_logger
from helperfunctions.try_connection import is_sql_file

ADMIN = {"username": "admin", "password": "password"}

app = Flask(__name__)
app.secret_key = (
    "192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf"
)


def get_db_connection():
    conn = sqlite3.connect("hw13.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def home():
    try:
        if request.method == "POST":
            if (
                "username" in session
                and session["username"] == ADMIN["username"]
            ):
                if session["password"] == ADMIN["password"]:
                    return redirect(url_for("show_dashboard"))
            else:
                session["username"] = request.form["username"]
                session["password"] = request.form["password"]
                if (
                    "username" in session
                    and session["username"] == ADMIN["username"]
                ):
                    if session["password"] == ADMIN["password"]:
                        return redirect(url_for("show_dashboard"))
        elif request.method == "GET":
            if (
                "username" in session
                and session["username"] == ADMIN["username"]
            ):
                if session["password"] == ADMIN["password"]:
                    return redirect(url_for("show_dashboard"))
            else:
                return render_template("login.html")
    except Exception as e:
        e = str(sys.exc_info())
        create_logger("loginerrorlogger", "./logs/loginerror.log", e)
        return render_template("somethingwentwrong.html", error=e)


@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("password", None)
    return redirect(url_for("home"))


@app.route("/dashboard")
def show_dashboard():
    try:
        conn = get_db_connection()
        if session["password"] == ADMIN["password"]:

            students = conn.execute("SELECT * FROM students")
            quizzes = conn.execute("SELECT * FROM quizzes;")

            return render_template(
                "dashboard.html", students=students, quizzes=quizzes
            )
        else:
            return render_template("anonimizedstudentgrades.html")
    except Exception as e:
        e = str(sys.exc_info())
        create_logger("showstudentslogger", "./logs/dashboard.log", e)
        return render_template("somethingwentwrong.html", error=e)
    finally:
        if conn:
            conn.close()


@app.route("/student/add", methods=["GET", "POST"])
def student_add():
    try:
        if request.method == "POST":
            conn = get_db_connection()
            if (
                "username" in session
                and session["username"] == ADMIN["username"]
            ):
                if session["password"] == ADMIN["password"]:
                    student_firstname = request.form["firstname"]
                    student_lastname = request.form["lastname"]
                    student = (student_firstname, student_lastname)
                    conn.execute(
                        "INSERT INTO students(firstname, lastname) VALUES(?,?)",
                        student,
                    )
                    conn.commit()
                    return redirect(url_for("home"))
        else:
            return render_template("addstudents.html")
    except Exception as e:
        e = str(sys.exc_info())
        create_logger("addstudentlogger", "./logs/addstudent.log", e)
        return render_template("somethingwentwrong.html", error=e)


@app.route("/quiz/add", methods=["GET", "POST"])
def quiz_add():
    try:
        if request.method == "POST":
            conn = get_db_connection()
            if (
                "username" in session
                and session["username"] == ADMIN["username"]
            ):
                if session["password"] == ADMIN["password"]:
                    quiz_subject = request.form["quiz_subject"]
                    quiz_num_questions = int(request.form["num_questions"])
                    quiz_date = request.form["quiz_date"]
                    quiz = (
                        quiz_subject,
                        quiz_num_questions,
                        quiz_date,
                    )
                    conn.execute(
                        "INSERT INTO quizzes(quiz_subject, num_questions, quiz_date) VALUES(?, ?, ?)",
                        quiz,
                    )
                    conn.commit()
                    return redirect(url_for("home"))
        else:
            return render_template("addquiz.html")
    except Exception as e:
        e = str(sys.exc_info())
        create_logger("addquizlogger", "./logs/addquiz.log", e)
        return render_template("somethingwentwrong.html", error=e)


@app.route("/student/<id>")
def show_student_quiz_results(id):
    try:
        conn = get_db_connection()
        if "username" in session and session["username"] == ADMIN["username"]:
            if session["password"] == ADMIN["password"]:
                student_quiz_query = (
                    "SELECT * FROM student_results WHERE student_id=?"
                )
                student_quiz_result = conn.execute(student_quiz_query, id)
                return render_template(
                    "studentquizzresult.html", results=student_quiz_result
                )
            else:
                return redirect(url_for("home"))
        else:
            return redirect(url_for("home"))
    except Exception as e:
        e = str(sys.exc_info())
        create_logger("studentquizlogger", "./logs/studentquiz.log", e)
        return render_template("somethingwentwrong.html", error=e)


@app.route("/results/add", methods=["GET", "POST"])
def add_student_grade_results():
    try:
        if request.method == "POST":

            conn = get_db_connection()
            student_id = int(request.form["student"])
            quiz_id = int(request.form["quiz"])
            grade = int(request.form["grade"])
            student_grade = (student_id, quiz_id, grade)
            print(student_grade)
            conn.execute(
                "INSERT INTO student_results(student_id, quiz_id, grade) VALUES(?, ?, ?)",
                student_grade,
            )
            conn.commit()
            # conn.execute(student_quiz_query, student_grade)
            return redirect(url_for("home"))

        else:
            conn = get_db_connection()
            if (
                "username" in session
                and session["username"] == ADMIN["username"]
            ):
                if session["password"] == ADMIN["password"]:
                    students = conn.execute("SELECT * from students")
                    quizzes = conn.execute("SELECT * from quizzes")
                    return render_template(
                        "addstudentquizresult.html",
                        students=students,
                        quizzes=quizzes,
                    )
    except Exception as e:
        e = str(sys.exc_info())
        create_logger(
            "addstudentquizerrorlogger", "./logs/addstudentquizerror.log", e
        )
        return render_template("somethingwentwrong.html", error=e)


# @app.route("quiz/<id>/results")
# def login():
#     return render_template("login.html")


# @app.route("/showstudents")
# def showstudents():
#     try:
#         conn = get_db_connection()
#         students = conn.execute("SELECT id, firstname, lastname from students")
#         return render_template("dashboard.html", students=students)
#     except Exception as e:
#         e = str(sys.exc_info())
#         create_logger("showstudentslogger", "./logs/showstudents.log", e)
#         return render_template("somethingwentwrong.html", error=e)
#     finally:
#         if conn:
#             conn.close()
