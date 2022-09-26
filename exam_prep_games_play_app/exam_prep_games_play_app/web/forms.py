from django import forms

from exam_prep_games_play_app.web.models import Profile, Game


class CreateProfileForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'category', 'rating', 'max_level', 'image', 'summary')
        labels = {
            'image': 'Image URL',
        }


class EditGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'category', 'rating', 'max_level', 'image', 'summary')
        labels = {
            'image': 'Image URL',
        }


class DeleteGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'category', 'rating', 'max_level', 'image', 'summary')

        title = forms.CharField(
            disabled=True,
        )

        category = forms.CharField(
            disabled=True,
        )

        rating = forms.FloatField(
            disabled=True,
        )

        max_level = forms.IntegerField(
            disabled=True,
        )

        image = forms.URLField(
            disabled=True,
        )

        summary = forms.CharField(
            disabled=True
        )

