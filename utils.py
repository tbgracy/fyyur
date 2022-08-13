import dateutil.parser
import babel


def set_genres(genres, model):
    print(genres)
    for genre in genres:
        stored_genre = Genre.query.filter_by(name=genre).first()
        if stored_genre:
            model.genres.append(stored_genre)
        else:
            model.genres.append(Genre(name=genre))
    print(model.genres)
    return model


def format_datetime(value, format='medium'):
    date = dateutil.parser.parse(value)
    if format == 'full':
        format = "EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
        format = "EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format, locale='en')
