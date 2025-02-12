from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('image', 'caption', 'hashtags')
        widgets = {
            'caption': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 bg-gray-100 dark:bg-gray-700 rounded-md focus:outline-none focus:ring-2 focus:ring-neoblue dark:focus:ring-neopink transition-neo',
                'rows': 3,
            }),
            'hashtags': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 bg-gray-100 dark:bg-gray-700 rounded-md focus:outline-none focus:ring-2 focus:ring-neoblue dark:focus:ring-neopink transition-neo',
            }),
        }
