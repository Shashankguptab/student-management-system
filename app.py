import mysql.connector

# database connection
conn = mysql.connector.connect(
    host="localhost", user="root", password="Royal@580", database="student_db"
)

cursor = conn.cursor()

# create table
cursor.execute(
    """
create table if not exists students (
    id int auto_increment primary key,
    name varchar(50),
    age int,
    course varchar(50)
)
"""
)


# add student
def add_student():
    name = input("enter name: ")
    age = int(input("enter age: "))
    course = input("enter course: ")

    query = "insert into students (name, age, course) values (%s, %s, %s)"
    cursor.execute(query, (name, age, course))
    conn.commit()
    print("student added successfully")


# view students
def view_students():
    cursor.execute("select * from students")
    data = cursor.fetchall()

    print("\n--- student list ---")
    for row in data:
        print(row)


# update student
def update_student():
    student_id = int(input("enter student id to update: "))
    new_name = input("enter new name: ")
    new_age = int(input("enter new age: "))
    new_course = input("enter new course: ")

    query = """
    update students
    set name=%s, age=%s, course=%s
    where id=%s
    """
    cursor.execute(query, (new_name, new_age, new_course, student_id))
    conn.commit()
    print("student updated successfully")


# delete student
def delete_student():
    student_id = int(input("enter student id to delete: "))

    query = "delete from students where id=%s"
    cursor.execute(query, (student_id,))
    conn.commit()
    print("student deleted successfully")


# main menu
while True:
    print("\n1. add student")
    print("2. view students")
    print("3. update student")
    print("4. delete student")
    print("5. exit")

    choice = input("enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("invalid choice")

conn.close()
