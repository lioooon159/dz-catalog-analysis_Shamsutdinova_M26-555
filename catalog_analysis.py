import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]}, # noqa: E501
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies):
    total = 0
    for movie in movies:
        total += movie["rating"]
    average = total / len(movies)
    return round(average, 1)


def catalog_age_stats(movies, current_year=2026):
    ages_movies = [current_year - m["year"] for m in movies]
    old_m = max(ages_movies)
    young_m = min(ages_movies)
    aver_m = math.ceil(sum(ages_movies) / len(ages_movies))
    return old_m, young_m, aver_m


def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


def rating_tier(rating):
    if rating >= 7:
        return "шедевр" if rating >= 9 else "хорошо"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"

def non_comedian(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def masterpiece(movies):
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9:
            print(f"Шедевр: {movies[i]['title']}")
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count_long = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count_long += 1
    return count_long

if __name__ == "__main__":
    print(f"Каталог загружен: {len(movies)} фильмов")
    print(f"Средняя оценка по каталогу: {average_rating(movies)}")
    stats = catalog_age_stats(movies)
    print(
        f"самый старый фильм в годах: {stats[0]}, "
        f"самый новый фильм в годах: {stats[1]}, "
        f"среднее {stats[2]}"
    )
    print(f"Длительность фильма: {duration_in_hours(155)}")
    print("Не комедии:")
    non_comedian(movies)
    masterpiece(movies)
    masterpiece(movies[:7])
    print(f"Фильмов с длительностью > 120 мин: {count_long_movies(movies)}")

    