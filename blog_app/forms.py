from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields ="__all__"
        widgets = {
            'Category': forms.Select(attrs= {'class':'form-control','id':'category'}),
            'SubCategory': forms.Select(attrs= {'class':'form-control','id':'Subcategory'}),
            'Title': forms.TextInput(attrs= {'class':'form-control','id':'title'}),
            'content':forms.Textarea(attrs={'class':'form-control','id':'content'}),
            'content1':forms.Textarea(attrs={'class':'form-control','id':'content1'}),
            '{{request.user.username}}':forms.TextInput(attrs={'class':'form-control','id':'author'}),
            'image':forms.FileInput(attrs={'class':'forms.control','type':'file','id':'image'})            
        }