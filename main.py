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
    print('----STARTING----')
    if request.method == "POST":
        print('request method is Post')
        selected_categories = request.form.getlist("category")
        print('selected categories:', selected_categories)
        return render_template("game.html", charade=getRandomCharade(selected_categories))
    return render_template("index.html", categories=categories.keys())

# def getInitialCharade(selected_categories):
#     return getRandomCharade(selected_categories)

def getRandomCharade(selected_categories):
    print('getting random charade')
    all_charades = [item for category in selected_categories for item in categories[category]]
    print('all charades:', all_charades)
    chosen = random.choice(all_charades)
    print('chosen:', chosen)
    if not all_charades:
        print('NOT all charades:', all_charades)
        all_charades = [item for category in categories.keys() for item in categories[category]]
        chosen = random.choice(all_charades)
        print('chosen:', chosen)
    return chosen

if __name__ == "__main__":
    app.run(debug=True)
