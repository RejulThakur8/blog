from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ["author"]
        # fields ="__all__"
        widgets = {
            'Category': forms.Select(attrs= {'class':'form-control','id':'category'}),
            'SubCategory': forms.Select(attrs= {'class':'form-control','id':'Subcategory'}),
            'SubSubcategory':forms.Select(attrs={'class':'form-control','id':'subsubcategory'}),
            'Title': forms.TextInput(attrs= {'class':'form-control','id':'title'}),
            'content':forms.Textarea(attrs={'class':'form-control','id':'content'}),
            'content1':forms.Textarea(attrs={'class':'form-control','id':'content1'}),
            'image':forms.FileInput(attrs={'class':'forms.control','type':'file','id':'image'}),
            'image1':forms.FileInput(attrs={'class':'forms.control','type':'file','id':'image1'})            
        }