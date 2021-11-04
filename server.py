from flask import Flask, render_template, request, redirect
from users_model import User


app = Flask(__name__)
@app.route("/display")
def index():
    users = User.get_all()
    print(users)
    return render_template("display.html", users=users)

@app.route("/create1")
def create():
    return render_template("create.html")


@app.route("/create", methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)

    return redirect("/display")
            
if __name__ == "__main__":
    app.run(debug=True)