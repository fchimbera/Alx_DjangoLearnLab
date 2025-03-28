from django import forms
from .models import Post, Comment
from django.forms import TextInput
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include the 'tags' field
        widgets = {
            'tags': TagWidget(attrs={'placeholder': 'Add tags separated by commas'}),  # Use TagWidget for tags
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Automatically set the author based on the logged-in user if available
        if 'author' in self.initial:
            instance.author = self.initial['author']
        if commit:
            instance.save()
            self.save_m2m()  # Save many-to-many data (tags)
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

class TagWidget(forms.Form):
    tags = forms.CharField(
    max_length=100,
    required=False,
    widget=forms.TextInput(attrs={'placeholder': 'Add tags separated by commas'}),
    label='Tags'
)
    class Meta:
        widgets = {
            'tags': forms.TextInput(attrs={'class': 'tag-widget', 'placeholder': 'Enter tags'}),
        }

