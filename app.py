from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Royal@580",
    "database": "student_db",
}


def get_connection():
    return mysql.connector.connect(**db_config)


@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return render_template("index.html", students=students)


@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["name"]
    age = request.form["age"]
    course = request.form["course"]

    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, course))
    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/delete/<int:id>")
def delete_student(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/edit/<int:id>")
def edit_student(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cursor.fetchone()
    conn.close()

    return render_template("edit.html", student=student)


@app.route("/update/<int:id>", methods=["POST"])
def update_student(id):
    name = request.form["name"]
    age = request.form["age"]
    course = request.form["course"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s",
        (name, age, course, id),
    )

    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
