from django import forms
from .models import *
from django.forms import Textarea, ModelForm

class PostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ('title','body','image','created_by')
        widgets = {
            'body': Textarea(attrs={'rows':10}),
        }

    def save(self, user_id, commit=True):
        form = super(PostForm, self).save(commit=False)
        form.name = User.objects.get(pk=user_id)
        if commit:
            form.save()
            return form

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': Textarea(attrs={'rows':3}),
        }


class ContactForm(forms.Form):
    class Meta: 
        model = Contact
        exclude = ('user', 'replied')

    def save(self, user_id):
        form = super(ContactForm, self)
        form.user = User.objects.get(pk=user_id)
        form.save()
        return form
