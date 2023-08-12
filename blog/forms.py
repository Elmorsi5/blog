from django import forms
from .models import Comment

# Dajngo has two classes to built forms: [Form, ModelForm]
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,widget=forms.Textarea)


# We use ModelForm in the case of an existing model: Comment is an existing model
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']