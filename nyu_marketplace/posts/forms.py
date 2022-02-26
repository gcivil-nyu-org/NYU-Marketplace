from django import forms
from .models import Post

#CHOICES = [('item1', 'item 1'),
              # ('item2', 'item 2')]

class PostModelForm(forms.ModelForm):
    #postal_code = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Post
        fields = ('name', 'description', 'option')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'option': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

