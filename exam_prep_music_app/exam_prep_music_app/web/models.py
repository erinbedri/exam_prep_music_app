from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from exam_prep_music_app.web.validators import validate_username_chars


class Profile(models.Model):
    USERNAME_CHAR_MIN_LEN = 2
    USERNAME_CHAR_MAX_LEN = 15

    EMAIL_CHAR_MAX_LEN = 30

    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_CHAR_MAX_LEN,
        validators=[
            MinLengthValidator(USERNAME_CHAR_MIN_LEN),
            validate_username_chars,
        ]
    ),

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(AGE_MIN_VALUE)
        ]
    )


class Album(models.Model):
    ALBUM_NAME_CHAR_MAX_LEN = 30

    ARTIST_NAME_CHAR_MAX_LEN = 30

    GENRE_CHAR_MAX_LEN = 30

    GENRE_CHOICES = [
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other'),
    ]

    PRICE_MIN_VALUE = 0.0

    name = models.CharField(
        max_length=ALBUM_NAME_CHAR_MAX_LEN,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_NAME_CHAR_MAX_LEN,
    )

    genre = models.CharField(
        max_length=GENRE_CHAR_MAX_LEN,
        choices=GENRE_CHOICES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image = models.URLField(
        verbose_name='Image URL:'
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(PRICE_MIN_VALUE)
        ]
    )
