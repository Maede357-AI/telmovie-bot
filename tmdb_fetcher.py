import requests
import random

API_KEY = "97028365ee9698086f5a065ed556ab18"
GENRE_MAP = {
    "عاشقانه": 10749,
    "اکشن": 28,
    "ترسناک": 27,
    "درام": 18,
    "کمدی": 35,
    "علمی":878
}

def get_movie_by_genre(farsi_genre):
    genre_id = GENRE_MAP.get(farsi_genre)
    if not genre_id:
        return "ژانر واردشده پشتیبانی نمی‌شود!"

    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}&language=fa"

    response = requests.get(url)
    data = response.json()

    if "results" not in data or len(data["results"]) == 0:
        return "فیلمی پیدا نشد 😕"

    movie = random.choice(data["results"])
    title = movie["title"]
    overview = movie["overview"]

    return f"🎬 {title}\n📖 {overview}"
