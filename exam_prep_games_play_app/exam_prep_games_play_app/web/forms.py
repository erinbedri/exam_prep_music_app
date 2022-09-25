from django import forms

from exam_prep_games_play_app.web.models import Profile


class CreateProfileForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
