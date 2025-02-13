from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
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

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError("Image is required!")
        if image.size > 5 * 1024 * 1024:  # 5MB dan katta bo‘lsa
            raise forms.ValidationError("Image size must be less than 5MB.")
        if not image.content_type.startswith("image"):
            raise forms.ValidationError("Invalid image format!")
        return image

    def clean_caption(self):
        caption = self.cleaned_data.get('caption')
        if not caption:
            raise forms.ValidationError("Caption cannot be empty!")
        if len(caption) < 5:
            raise forms.ValidationError("Caption must be at least 5 characters long.")
        return caption

    def clean_hashtags(self):
        hashtags = self.cleaned_data.get('hashtags')
        if hashtags and not hashtags.startswith("#"):
            raise forms.ValidationError("Hashtags must start with '#' symbol.")
        if hashtags and len(hashtags) > 255:
            raise forms.ValidationError("Hashtags must be less than 255 characters.")
        return hashtags

    def clean(self):
        cleaned_data = super().clean()
        caption = cleaned_data.get("caption")
        hashtags = cleaned_data.get("hashtags")

        if caption and hashtags and caption.lower() in hashtags.lower():
            raise forms.ValidationError("Caption and hashtags should not be identical!")

        return cleaned_data