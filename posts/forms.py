from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile

from .models import Post
from .humanize import naturalsize


class PostModelForm(forms.ModelForm):
    #postal_code = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    # max_upload_limit = 2 * 1024 * 1024
    # max_upload_limit_text = naturalsize(max_upload_limit)
    #
    # # Call this 'picture' so it gets copied from the form to the in-memory model
    # # It will not be the "bytes", it will be the "InMemoryUploadedFile"
    # # because we need to pull out things like content_type
    # picture = forms.FileField(required=False, label='File to Upload <= ' + max_upload_limit_text)
    # upload_field_name = 'picture'
    #
    # def clean(self):
    #     cleaned_data = super().clean()
    #     pic = cleaned_data.get('picture')
    #     if pic is None:
    #         return
    #     if len(pic) > self.max_upload_limit:
    #         self.add_error('picture', "File must be < " + self.max_upload_limit_text + " bytes")
    #
    # # Convert uploaded File object to a picture
    # def save(self, commit=True):
    #     print("save called")
    #     instance = super(PostModelForm, self).save(commit=False)
    #
    #     # We only need to adjust picture if it is a freshly uploaded file
    #     f = instance.picture  # Make a copy
    #     print(f.content_type)   ####object has no attribute 'content_type'
    #     if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
    #         bytearr = f.read()
    #         instance.content_type = f.content_type
    #         print("content_type save called")
    #         instance.picture = bytearr  # Overwrite with the actual image data
    #
    #     if commit:
    #         instance.save()
    #         self.save_m2m()
    #     #print("image saved")
    #
    #     return instance

    class Meta:
        model = Post
        fields = ('name', 'option', 'price', 'category', 'description', 'picture', 'location')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                            'type': "itemName",
                                            'id': "inputItemName",
                                            'placeholder': "Please Enter Item Name"}),
            'option': forms.RadioSelect(attrs={'class': 'form-check-inline',
                                          'id': 'inputOption'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                            'type': "itemName",
                                            'id': "inputDescription",
                                            'rows' : 3}),
            'price': forms.TextInput(attrs={'class': 'form-control',
                                            'type': "itemPrice",
                                            'id': "inputItemPrice",
                                            'placeholder': "Please Enter Item Price",
                                            'onkeyup': "value=value.replace(/^\D*(\d*(?:\.\d{0,2})?).*$/g, '$1')"}),
            'category': forms.Select(attrs={'class': 'form-select col-sm-9',
                                            'id': 'inputCategory'}),
            'location': forms.TextInput(attrs={'class': 'form-control',
                                           'type': "itemLocation",
                                           'id': "inputItemLocation",
                                           'placeholder': "Please Enter Item Location"}),
        }