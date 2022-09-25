from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    AGE_MIN_VALUE = 12

    PASSWORD_MAX_LEN = 30

    FIRST_NAME_MAX_LEN = 30

    email = models.EmailField()

    age = models.IntegerField(
        validators=[
            MinValueValidator(AGE_MIN_VALUE),
        ]
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=FIRST_NAME_MAX_LEN,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=FIRST_NAME_MAX_LEN,
    )

    picture = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Game(models.Model):
    TITLE_MAX_LEN = 30

    CATEGORY_CHOICES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other'),
    )

    CATEGORY_MAX_LEN = max([len(c[1]) for c in CATEGORY_CHOICES])

    RATING_MIN = 0.1
    RATING_MAX = 5

    MAX_LEVEL_MIN_VALUE = 1

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        unique=True,
    )

    category = models.CharField(
        max_length=CATEGORY_MAX_LEN,
        choices=CATEGORY_CHOICES,
    )

    rating = models.FloatField(
        validators=[
            MinValueValidator(RATING_MIN),
            MaxValueValidator(RATING_MAX),
        ]
    )

    max_level = models.IntegerField(
        validators=[
            MinValueValidator(MAX_LEVEL_MIN_VALUE)
        ]
    )

    image = models.URLField()

    summary = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.title}'
