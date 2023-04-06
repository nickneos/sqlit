from flask import Flask, flash, redirect, render_template, request, session
from sqlit import sqlit

# Configure application
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        input = request.form.get("in")
        output = sqlit(input)
        return render_template("index.html", output=output)
    # User reached route via GET (as by clicking a link or via redirect)
    else: 
        return render_template("index.html", output=None)



