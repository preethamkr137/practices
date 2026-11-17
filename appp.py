
from flask import Flask, render_template, request, redirect

appp = Flask(__name__)

problems = []

@appp.route("/")
def home():
    return render_template(
        "index.html",
        problems=problems
    )

@appp.route("/submit", methods=["POST"])
def submit():

    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()

    if title and description:

        problems.append({
            "title": title,
            "description": description
        })

    return redirect("/")

if __name__ == "__main__":
    appp.run(debug=True)
