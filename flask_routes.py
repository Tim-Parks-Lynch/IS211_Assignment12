from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask import session
from flask import flash
import sys
import sqlite3

from helperfunctions.create_logger import create_logger
from helperfunctions.try_connection import is_sql_file

ADMIN = {"username": "admin", "password": "password"}

app = Flask(__name__)
app.secret_key = (
    "192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf"
)


def authenticated_flag(username, password):
    if username and username == ADMIN["username"]:
        if password and password == ADMIN["password"]:
            return True
        return False
    else:
        return False


def get_db_connection():
    conn = sqlite3.connect("hw13.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "authenticated_user" in session and session["authenticated_user"]:
            return redirect(url_for("show_dashboard"))
        else:
            try:
                username = request.form["username"]
                password = request.form["password"]
                session["authenticated_user"] = authenticated_flag(
                    username, password
                )

                if session["authenticated_user"]:
                    return redirect(url_for("show_dashboard"))
                else:
                    flash("Incorrect Username or Password")
                    return render_template("login.html")
            except Exception as e:
                e = str(sys.exc_info())
                create_logger("loginerrorlogger", "./logs/loginerror.log", e)
                return render_template("somethingwentwrong.html", error=e)
    else:
        if "authenticated_user" in session and session["authenticated_user"]:
            return redirect(url_for("show_dashboard"))
        else:
            return render_template("login.html")


@app.route("/logout")
def logout():
    if "authenticated_user" in session:
        session.pop("authenticated_user", None)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


@app.route("/dashboard")
def show_dashboard():
    if "authenticated_user" in session and session["authenticated_user"]:
        try:
            conn = get_db_connection()
            students = conn.execute("SELECT * FROM students")
            quizzes = conn.execute("SELECT * FROM quizzes;")

            return render_template(
                "dashboard.html", students=students, quizzes=quizzes
            )

        except Exception as e:
            e = str(sys.exc_info())
            create_logger("showstudentslogger", "./logs/dashboard.log", e)
            return render_template("somethingwentwrong.html", error=e)

        finally:
            if conn:
                conn.close()
    else:
        return redirect(url_for("home"))


@app.route("/student/add", methods=["GET", "POST"])
def student_add():
    if "authenticated_user" in session and session["authenticated_user"]:
        if request.method == "POST":
            try:
                error = None
                conn = get_db_connection()
                student_firstname = request.form["firstname"]
                student_lastname = request.form["lastname"]
                student = (student_firstname, student_lastname)

                if not student_firstname or not student_firstname.strip():
                    error = "First name can not be empty"
                if not student_lastname or not student_lastname.strip():
                    error = "Last name can not be empty"
                if error:
                    flash(error)
                    return redirect(url_for("student_add"))

                conn.execute(
                    "INSERT INTO students(firstname, lastname) VALUES(?,?)",
                    student,
                )
                conn.commit()
                return redirect(url_for("home"))

            except Exception as e:
                e = str(sys.exc_info())
                create_logger("addstudentlogger", "./logs/addstudent.log", e)
                return render_template("somethingwentwrong.html", error=e)
        else:
            return render_template("addstudents.html")
    else:
        return redirect(url_for("home"))


@app.route("/quiz/add", methods=["GET", "POST"])
def quiz_add():
    if "authenticated_user" in session and session["authenticated_user"]:
        if request.method == "POST":
            # try:
            error = None
            conn = get_db_connection()
            quiz_subject = request.form["quiz_subject"]
            quiz_num_questions = int(request.form["num_questions"])
            quiz_date = request.form["quiz_date"]
            quiz = (
                quiz_subject,
                quiz_num_questions,
                quiz_date,
            )

            if not quiz_subject or not quiz_subject.strip():
                error = "Quiz Subject can not be empty"
            if quiz_num_questions < 1:
                error = "Number of Questions can not be less than 1"
            if not quiz_date:
                error = "Quiz Date can not be empty"
            if error:
                flash(error)
                return redirect(url_for("quiz_add"))

            conn.execute(
                "INSERT INTO quizzes(quiz_subject, num_questions, quiz_date) VALUES(?, ?, ?)",
                quiz,
            )
            conn.commit()
            return redirect(url_for("home"))

        # except Exception as e:
        #     e = str(sys.exc_info())
        #     create_logger("addquizlogger", "./logs/addquiz.log", e)
        #     return render_template("somethingwentwrong.html", error=e)
        else:
            return render_template("addquiz.html")
    else:
        return redirect(url_for("home"))


@app.route("/student/<id>")
def show_student_quiz_results(id):
    if "authenticated_user" in session and session["authenticated_user"]:
        try:
            conn = get_db_connection()
            student_quiz_query = (
                "SELECT * FROM student_results WHERE student_id=?"
            )
            student_quiz_result = conn.execute(student_quiz_query, id)
            return render_template(
                "studentquizzresult.html", results=student_quiz_result
            )

        except Exception as e:
            e = str(sys.exc_info())
            create_logger("studentquizlogger", "./logs/studentquiz.log", e)
            return render_template("somethingwentwrong.html", error=e)
    else:
        return redirect(url_for("home"))


@app.route("/results/add", methods=["GET", "POST"])
def add_student_grade_results():
    if "authenticated_user" in session and session["authenticated_user"]:
        if request.method == "POST":
            try:
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
                return redirect(url_for("home"))

            except Exception as e:
                e = str(sys.exc_info())
                create_logger(
                    "addstudentquizerrorlogger",
                    "./logs/addstudentquizerror.log",
                    e,
                )
                return render_template("somethingwentwrong.html", error=e)
        else:
            conn = get_db_connection()
            students = conn.execute("SELECT * from students")
            quizzes = conn.execute("SELECT * from quizzes")
            return render_template(
                "addstudentquizresult.html",
                students=students,
                quizzes=quizzes,
            )
    else:
        return redirect(url_for("home"))


@app.route("/quiz/<id>/results")
def anonimized_quiz_results(id):
    try:
        conn = get_db_connection()
        quiz_query = "SELECT * FROM student_results WHERE quiz_id=?"
        quiz_result = conn.execute(quiz_query, id)
        return render_template(
            "anonimizedquizgrades.html", students=quiz_result
        )
    except:
        e = str(sys.exc_info())
        create_logger("showstudentslogger", "./logs/showstudents.log", e)
        return render_template("somethingwentwrong.html", error=e)


app.run(debug=True)
