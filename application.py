from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route("/application-form")
def fill_out_application_form():
    """Load the application form and accepts and sends the submission
    to another page that will fill out a print statement.
    """
    return render_template("application-form.html")

@app.route("/application")
def print_form():

    first_name = request.args.get("firstname")
    last_name = request.args.get("lastname")
    salary_req = request.args.get("salaryreq")    
    job = request.args.get("jobtitle")

    return render_template("application-response.html",
                            firstname=first_name,
                            lastname=last_name,
                            salaryreq=salary_req,
                            job=job)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

