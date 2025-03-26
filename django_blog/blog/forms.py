from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Fields to be included in the form

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Automatically set the author based on the logged-in user if available
        if 'author' in self.initial:
            instance.author = self.initial['author']
        if commit:
            instance.save()
        return instance
