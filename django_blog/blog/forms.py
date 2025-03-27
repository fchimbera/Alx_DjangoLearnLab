from django import forms
from .models import Post, Comment

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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Leave a commen here:', # Custom label for the content field
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}), # Custom widget for the content field
        }
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("Comment content cannot be empty.")
        if len(content) > 500:  # Example rule for a maximum character limit
            raise forms.ValidationError("Comment content is too long (maximum 500 characters).")
        return content