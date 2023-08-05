from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import random

app = Flask(__name__)
bootstrap = Bootstrap(app)

categories = {
    "Famous People": ["Albert Einstein", "Leonardo da Vinci", "Oprah Winfrey", "Michael Jackson"],
    "Movies": ["The Godfather", "Jurassic Park", "Avatar", "Star Wars"],
    "TV Shows": ["Friends", "Stranger Things", "Game of Thrones", "The Office"],
    # Add more categories and items as desired
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_categories = request.form.getlist("category")
        return render_template("game.html", charade=getInitialCharade(selected_categories))
    return render_template("index.html", categories=categories.keys())

def getInitialCharade(selected_categories):
    return getRandomCharade(selected_categories)

def getRandomCharade(selected_categories):
    all_charades = [item for category in selected_categories for item in categories[category]]
    if not all_charades:
        return "Please select at least one category."
    return random.choice(all_charades)

if __name__ == "__main__":
    app.run(debug=True)
