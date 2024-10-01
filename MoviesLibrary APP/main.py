from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

##CREATE DATABASE

class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-movies-collection.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    movie_type: Mapped[str] = mapped_column(String(250), unique=False, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(movie).order_by(movie.title))
        all_movies = result.scalars().all()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_movie = movie(title=request.form["title"], movie_type=request.form["movie_type"], rating=request.form["rating"])
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route('/edit' , methods=["GET", "POST"])
def edit_rating():
    if request.method == "POST":
        #UPDATE RECORD
        movie_id = request.form["id"]
        movie_to_update = db.get_or_404(movie, movie_id)
        movie_to_update.rating = request.form["rating"]
        movie_to_update.title = request.form["name"]
        movie_to_update.movie_type = request.form["movie_type"]
        db.session.commit()
        return redirect(url_for('home'))
    movie_id = request.args.get('id')
    movie_selected = db.get_or_404(movie, movie_id)
    return render_template("edit.html", movie=movie_selected)


if __name__ == "__main__":
    app.run(debug=True)
