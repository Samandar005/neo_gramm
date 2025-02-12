from .models import CustomUser, UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'fullname', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-3 py-2 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-neoblue dark:focus:ring-neopink transition-neo',
            }),
            'fullname': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-neoblue dark:focus:ring-neopink transition-neo',
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'w-full px-3 py-2 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-neoblue dark:focus:ring-neopink transition-neo',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'w-full px-3 py-2 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-neoblue dark:focus:ring-neopink transition-neo',
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use. Please choose another one.")
        return email

    def clean_fullname(self):
        fullname = self.cleaned_data.get('fullname')
        if not re.match(r'^[A-Za-z\s]+$', fullname):
            raise ValidationError("Full name should only contain letters and spaces.")
        return fullname


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'autofocus': True,
        'class': 'w-full px-3 py-2 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-neoblue dark:focus:ring-neopink transition-neo'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-3 py-2 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-neoblue dark:focus:ring-neopink transition-neo'
    }))


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image', 'bio')
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'hidden'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-neoblue dark:focus:ring-neopink transition-neo',
                'rows': 3,
            }),
        }

    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if len(bio) > 500:
            raise ValidationError("Bio must not exceed 500 characters.")
        return bio

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if not image:
            return image

        if image.size > 5 * 1024 * 1024:
            raise ValidationError("Image file size must be less than 5MB.")

        valid_extensions = ['image/jpeg', 'image/png', 'image/gif']
        if image.content_type not in valid_extensions:
            raise ValidationError("Only JPEG, PNG, and GIF images are allowed.")

        return image
