from django import forms
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comments',)
        widgets = {
            'comments': forms.TextInput(attrs={
                'class': 'flex-grow px-3 py-2 bg-gray-100 dark:bg-gray-700 rounded-md focus:outline-none focus:ring-2 focus:ring-neoblue dark:focus:ring-neopink transition-neo',
                'rows': 3,
            }),
        }
