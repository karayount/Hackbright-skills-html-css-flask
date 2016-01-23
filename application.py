from flask import Flask, render_template, request

app = Flask(__name__)

app.secret_key = "something-you-would-never-guess-in-14-lifetimes"


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route("/application-form")
def show_application_form():
    """Show the application form."""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def show_submitted_application():
    """Show the submitted application with user-entered data."""

    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    desired_salary = request.form.get("salary")
    job_title = request.form.get("position")

    return render_template("application-response.html",
                           first=first_name,
                           last=last_name,
                           salary=desired_salary,
                           position=job_title)


if __name__ == "__main__":
    app.run(debug=True)
