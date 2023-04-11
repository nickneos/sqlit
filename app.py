from flask import Flask, flash, redirect, render_template, request, session
from sqlit import sqlit

# Configure application
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        input = request.form.get("in")
        if request.form.get("delimitter") == "tab":
            delimitter = "\t"
        if request.form.get("delimitter") == "comma":
            delimitter = ","
        output = sqlit(input, delimitter)
        return render_template("index.html", output=output, delimitter=delimitter)
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("index.html", output=None)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


