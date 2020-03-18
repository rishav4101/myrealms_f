from django import forms
from .models import *
from django.forms import Textarea, ModelForm

class PostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ('title','body','image')
        widgets = {
            'body': Textarea(attrs={'rows':5}),
        }

    def save(self, user_id, commit=True):
        form = super(PostForm, self).save(commit=False)
        form.name = User.objects.get(pk=user_id)
        if commit:
            form.save()
            return form

class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ('body',)
