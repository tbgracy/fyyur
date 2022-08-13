from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

venue_genres = db.Table('venue_genres',
                        db.Column('venue_id', db.Integer, db.ForeignKey(
                            'Venue.id'), primary_key=True),
                        db.Column('genre_id', db.Integer, db.ForeignKey(
                            'Genre.id'), primary_key=True),
                        )

artist_genres = db.Table('artist_genres',
                         db.Column('artist_id', db.Integer, db.ForeignKey(
                             'Artist.id'), primary_key=True),
                         db.Column('genre_id', db.Integer, db.ForeignKey(
                             'Genre.id'), primary_key=True),
                         )


class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.relationship(
        'Genre', secondary=venue_genres, backref=db.backref('venues', lazy=True))
    facebook_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='venue', lazy=True)


class Genre(db.Model):
    __tablename__ = 'Genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<id: {self.id}, name: {self.name}>"


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.relationship(
        'Genre', secondary=artist_genres, backref=db.backref('artists', lazy=True))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    shows = db.relationship('Show', backref='artist', lazy=True)
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(500))


class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey(
        'Artist.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<id: {self.id}, venue_id: {self.venue_id}, artist_id: {self.artist_id}, start_time: {self.start_time}>"

