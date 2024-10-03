from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import requests
import os

# Get env variables
load_dotenv()
URL = os.getenv("MOVIE_DB_SEARCH_URL")
MOVIE_SEARCH_URL = os.getenv("MOVIE_SEARCH_URL")
TOKEN = os.getenv("MOVIE_DB_API_KEY")
API_KEY = os.getenv("API_KEY")
APP_KEY = os.getenv("APP_KEY")
MOVIE_DB_IMAGE_URL = os.getenv("MOVIE_DB_IMAGE_URL")
headers = {"accept": "application/json", "Authorization": f"Bearer {TOKEN}"}

app = Flask(__name__)
app.config['SECRET_KEY'] = APP_KEY
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top_movies.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    list_num: Mapped[int] = mapped_column(Float)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


# Home page where all the movies from database are listed, order by your rating.
@app.route("/")
def home():
    with app.app_context():
        # result = db.session.execute(db.select(Movie).order_by(Movie.id))  #  ORDER BY ID
        # result = db.session.execute(db.select(Movie).order_by(desc(Movie.rating)))  #  ORDER BY RATING DESCENDING
        result = db.session.execute(db.select(Movie).order_by(Movie.rating))  # ORDER BY RATING ASCENDING
        all_movies = result.scalars().all()
        display_id = 1
        for movie in all_movies:
            movie.list_num = display_id
            display_id += 1
    return render_template("index.html", movies=all_movies)


# Edit rating or review of a movie
@app.route("/edit", methods=["GET", "POST"])
def edit_movie():
    if request.method == "POST":
        movie_id = request.form["id"]
        movie_to_update = db.get_or_404(Movie, movie_id)
        movie_to_update.rating = request.form["new_rating"]
        movie_to_update.review = request.form["new_review"]
        db.session.commit()
        return redirect(url_for('home'))
    movie_id = request.args.get('id')
    movie_selected = db.get_or_404(Movie, movie_id)
    return render_template("edit.html", movie=movie_selected)


# Delete a movie from database
@app.route('/delete', methods=["GET", "POST"])
def delete_movie():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.filter_by(id=movie_id).first()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


# Add a new movie to the database
@app.route('/add', methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(URL, params={"query": movie_title}, headers=headers)
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


# Find the movie on the movie database TMDB
@app.route('/find', methods=["GET", "POST"])
def find_movie():
    movie_api_id = request.args.get('id')
    movie_api_url = f"{MOVIE_SEARCH_URL}/{movie_api_id}"
    response = requests.get(movie_api_url, params={"language": "en-US"}, headers=headers)
    data = response.json()
    print(data)
    new_movie = Movie(
        title=data["original_title"],
        list_num=0,
        year=data["release_date"].split("-")[0],
        img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
        description=data["overview"],
        rating=data["popularity"],
        review="Review it"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit_movie", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
