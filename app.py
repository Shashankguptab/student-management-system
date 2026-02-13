from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn


# create table
def init_db():
    conn = get_db()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            course TEXT
        )
    """
    )
    conn.commit()
    conn.close()


init_db()


@app.route("/")
def index():
    conn = get_db()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("index.html", students=students)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]

        conn = get_db()
        conn.execute(
            "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
            (name, age, course),
        )
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
