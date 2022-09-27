# Generated by Django 4.1.1 on 2022-09-27 08:42

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import exam_prep_music_app.web.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=15, validators=[django.core.validators.MinLengthValidator(2), exam_prep_music_app.web.validators.validate_username_chars]),
            preserve_default=False,
        ),
    ]
