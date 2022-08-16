from datetime import datetime
from flask_wtf import FlaskForm as Form
from wtforms import (
    StringField,
    SelectField,
    SelectMultipleField,
    DateTimeField,
    BooleanField
)
from wtforms.validators import DataRequired, AnyOf, URL, Optional
from fake_enums import state_choices, genre_choices
from validators import is_valid_phone


class ShowForm(Form):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired(
            message='Please check the format of the date you entered')],
        default=datetime.today()
    )


class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=state_choices
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=genre_choices
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL(message='Invalid facebook URL'), Optional()]
    )
    website_link = StringField(
        'website_link', validators=[URL(message='Invalid website URL'), Optional()]
    )

    seeking_talent = BooleanField('seeking_talent')

    seeking_description = StringField(
        'seeking_description'
    )

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        if not is_valid_phone(self.phone.data):
            self.phone.errors.append('Use a valid phone number format')
            return False
        if not set(self.genres.data).issubset(dict(genre_choices).keys()):
            self.genres.errors.append('Please choose valid genres')
            return False
        if set(self.state.data) not in list(dict(state_choices).keys()):
            self.state.errors.append('Please choose valid state')
            return False

        return True


class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=state_choices
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link', validators=[URL(message='Invalid image URL'), Optional()]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=genre_choices
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL(message='Invalid facebook URL'), Optional()]
    )

    website_link = StringField(
        'website_link', validators=[URL(message='Invalid web URL'), Optional()]
    )

    seeking_venue = BooleanField('seeking_venue')

    seeking_description = StringField(
        'seeking_description'
    )

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        if not is_valid_phone(self.phone.data):
            self.phone.errors.append('Use a valid phone number format')
            return False
        if not set(self.genres.data).issubset(dict(genre_choices).keys()):
            self.genres.errors.append('Please choose valid genres')
            return False
        if str(self.state.data) not in list(dict(state_choices).keys()):
            self.state.errors.append('Please choose valid state')
            return False

        return True
