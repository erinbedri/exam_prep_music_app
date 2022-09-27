from django import forms

from exam_prep_music_app.web.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')


class CreateAlbumForm(forms.ModelForm):
    name = forms.CharField(
        label='Album Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Album Name',
            }
        )
    )

    artist = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Artist',
            }
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Description',
            }
        )
    )

    image = forms.CharField(
        label='Image URL',
        widget=forms.URLInput(
            attrs={
                'placeholder': 'Image URL',
            }
        )
    )

    price = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Price',
            }
        )
    )


    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image', 'price')