from flask import Flask, render_template, request, redirect
from users_model import User


app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route("/users")
def display():
    users = User.get_all()
    print(users)
    return render_template("users.html", users=users)

@app.route("/user/new")
def create():
    return render_template("users_new.html")


@app.route("/user/create", methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    user_id = User.save(data)

    return redirect( f'/show/{user_id}')

@app.route("/show/<int:id>")
def show_user(id):
    data = {
        "id":id
    }
    user=User.get_user(data)
    return render_template("showuser.html", user=user)

@app.route("/edit/<int:id>")
def edit_user(id):
    data = {
        "id":id
    }
    user=User.get_user(data)
    return render_template("edituser.html", user=user)

@app.route("/edituser/<int:id>", methods=["POST"])
def edit_user_db(id):
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
        "id":id
    }
    User.edit_user(data)
    return redirect("/")

@app.route("/delete/<int:id>")
def delete_user(id):
    data = {
        "id":id
    }
    User.delete_user(data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)