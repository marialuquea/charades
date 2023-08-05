from flask import Flask, render_template, request, session
from flask_bootstrap import Bootstrap
import random

app = Flask(__name__)
app.secret_key = "my-super-secret-key"
bootstrap = Bootstrap(app)

categories = {
    "Famous People": [
        "Albert Einstein", "Leonardo da Vinci", "Oprah Winfrey", "Michael Jackson",
        "Marie Curie", "Nelson Mandela", "Elvis Presley", "Cleopatra",
        "William Shakespeare", "Amelia Earhart", "Mahatma Gandhi", "Queen Elizabeth II",
        "Walt Disney", "Isaac Newton", "Abraham Lincoln", "Marilyn Monroe",
        "Martin Luther King Jr.", "Mother Teresa", "Steve Jobs", "Pablo Picasso",
        "Winston Churchill", "Charles Darwin", "Jane Austen", "Napoleon Bonaparte",
        "Malala Yousafzai", "Bill Gates", "Leonardo DiCaprio", "Elon Musk", "J.K. Rowling",
        "Muhammad Ali", "Vincent van Gogh"
    ],
    "Movies": [
        "The Godfather", "Jurassic Park", "Avatar", "Star Wars",
        "Toy Story", "Titanic", "Harry Potter", "The Lord of the Rings",
        "Spider-Man", "Frozen", "Finding Nemo", "The Lion King",
        "Inception", "Forrest Gump", "Pulp Fiction", "The Matrix",
        "The Shawshank Redemption", "Avengers: Endgame", "Guardians of the Galaxy", "Jaws",
        "Back to the Future", "E.T. the Extra-Terrestrial", "The Dark Knight", "The Sound of Music",
        "Casablanca", "The Wizard of Oz", "The Terminator", "Ghostbusters", "Indiana Jones",
        "The Great Gatsby", "Pirates of the Caribbean"
    ],
    "TV Shows": [
        "Friends", "Stranger Things", "Game of Thrones", "The Office",
        "Breaking Bad", "The Simpsons", "The Crown", "Black Mirror",
        "FRIENDS", "The Big Bang Theory", "Family Guy", "Westworld",
        "Sherlock", "The Walking Dead", "The Mandalorian", "Grey's Anatomy",
        "The X-Files", "The Sopranos", "Lost", "Modern Family",
        "Mindhunter", "The Witcher", "The Handmaid's Tale", "Dexter",
        "Suits", "Vikings", "The Wire", "Doctor Who", "Stranger Things",
        "South Park", "Friends"
    ],
    "Books": [
        "To Kill a Mockingbird", "1984", "Harry Potter and the Sorcerer's Stone",
        "The Great Gatsby", "Pride and Prejudice", "The Catcher in the Rye",
        "The Lord of the Rings", "The Hunger Games", "The Da Vinci Code", "Animal Farm",
        "Brave New World", "The Hobbit", "Fahrenheit 451", "The Alchemist", "The Giver",
        "Twilight", "War and Peace", "The Little Prince", "The Picture of Dorian Gray",
        "Gone with the Wind", "The Chronicles of Narnia", "Frankenstein", "The Shining",
        "Wuthering Heights", "Lord of the Flies", "The Fault in Our Stars",
        "Alice's Adventures in Wonderland", "One Hundred Years of Solitude", "Moby-Dick",
        "Jane Eyre", "The Odyssey"
    ],
    "Objects": [
        "Cell Phone", "Sunglasses", "Bicycle", "Camera",
        "Coffee Mug", "Umbrella", "Wallet", "Backpack",
        "Watch", "Headphones", "Laptop", "Book", "Guitar", "Keys", "Shoes",
        "Television", "Microwave", "Chair", "Table", "Car", "Knife", "Fork",
        "Cup", "Plate", "Bottle", "Pen", "Pencil", "Computer Mouse", "Remote Control",
        "Bike Helmet", "Headphones"
    ],
    "Actions": [
        "Dancing", "Running", "Singing", "Cooking",
        "Painting", "Jumping", "Laughing", "Sleeping",
        "Eating", "Reading", "Swimming", "Playing Guitar",
        "Writing", "Drawing", "Biking", "Hiking",
        "Shopping", "Talking", "Sleeping", "Working Out",
        "Watching TV", "Texting", "Driving", "Studying",
        "Skiing", "Gardening", "Meditating", "Running",
        "Singing", "Playing Chess"
    ],
    "Countries": [
        "United States", "China", "India", "Brazil",
        "Russia", "Japan", "Germany", "United Kingdom",
        "France", "Canada", "Australia", "South Korea",
        "Italy", "Spain", "Mexico", "Netherlands",
        "Argentina", "Turkey", "Saudi Arabia", "Indonesia",
        "Egypt", "Switzerland", "Sweden", "Singapore",
        "Norway", "Denmark", "Ireland", "New Zealand",
        "Greece", "Austria", "Belgium"
    ],
    "F1 Drivers": [
        "Lewis Hamilton", "Sebastian Vettel", "Fernando Alonso", "Kimi Räikkönen",
        "Max Verstappen", "Daniel Ricciardo", "Nico Rosberg", "Michael Schumacher",
        "Carlos Sainz Jr.", "Valtteri Bottas", "Sergio Perez", "Esteban Ocon",
        "Lando Norris", "Romain Grosjean"
    ],
    "Famous AI People": [
        "Elon Musk", "Andrew Ng", "Yoshua Bengio", "Geoff Hinton",
        "Fei-Fei Li", "Demis Hassabis", "Yann LeCun", "Sebastian Thrun",
        "Jeff Dean", "Ian Goodfellow"
    ]
}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_categories = request.form.getlist("category")
        session["selected_categories"] = selected_categories
        print('selected categories:', selected_categories)
        return render_template("game.html", charade=getRandomCharade(selected_categories))
    return render_template("index.html", categories=categories.keys())

@app.route("/game", methods=["POST"])
def game():
    selected_categories = session.get("selected_categories")
    print('YAY WE GOT SOME CATEGORIES', selected_categories)
    if not selected_categories:
        return "Please select categories first."

    charade = getRandomCharade(selected_categories)
    return render_template("game.html", charade=charade)

def getRandomCharade(selected_categories):
    all_charades = [item for category in selected_categories for item in categories[category]]
    if not all_charades:
        print('CATEGORIES NOT FOUND IN SESSION')
        all_charades = [item for category in categories.keys() for item in categories[category]]
        chosen = random.choice(all_charades)
    else:
        chosen = random.choice(all_charades)
    return chosen

if __name__ == "__main__":
    app.run(debug=True)
