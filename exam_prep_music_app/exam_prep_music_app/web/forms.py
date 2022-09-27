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


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image', 'price')


class DeleteAlbumForm(forms.ModelForm):
    name = forms.CharField(
        disabled=True,
    )

    artist = forms.CharField(
        disabled=True,
    )

    genre = forms.CharField(
        disabled=True,
    )

    description = forms.CharField(
        disabled=True,
    )

    image = forms.URLField(
        disabled=True,
    )

    price = forms.FloatField(
        disabled=True,
    )

    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image', 'price')


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()


